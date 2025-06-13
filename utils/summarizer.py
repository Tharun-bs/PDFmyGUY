from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load T5 model and tokenizer (only once)
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

def summarize_text(text, max_input_length=512, max_output_length=150):
    # Preprocess and truncate long input
    text = "summarize: " + text.strip().replace("\n", " ")
    inputs = tokenizer.encode(
        text,
        return_tensors="pt",
        max_length=max_input_length,
        truncation=True
    )

    # Generate summary
    summary_ids = model.generate(
        inputs,
        max_length=max_output_length,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
