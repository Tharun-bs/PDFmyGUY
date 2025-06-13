import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load T5 model
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

# Extract text from PDF
def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Summarize text using T5 with mode
def summarize_text(text, mode="medium"):
    length_map = {
        "short": 50,
        "medium": 120,
        "detailed": 200
    }
    max_len = length_map.get(mode, 120)

    input_text = "summarize: " + text.strip().replace("\n", " ")
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
    summary_ids = model.generate(inputs, max_length=max_len, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    filename = None

    if request.method == "POST":
        file = request.files["pdf"]
        mode = request.form.get("mode", "medium")

        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            text = extract_text_from_pdf(path)
            summary = summarize_text(text, mode)

    return render_template("index.html", summary=summary, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
