# PDFmyGUY
PDFmyGUY is a smart PDF analyzer web application that uses machine learning to generate human-readable summaries from uploaded PDF files. It leverages state-of-the-art transformer models (like T5) to provide extractive or abstractive summaries in various formats (short, detailed, bullet points, etc.).
# 📄 PDFmyGUY — Smart PDF Analyzer

**PDFmyGUY** is a lightweight and powerful web-based PDF summarization tool powered by machine learning. Upload a PDF, choose your summary type, and let the model do the rest.

---

## 🚀 Features

- ✅ Upload PDF files (drag and drop or browse)
- 🧠 ML-powered text summarization using T5
- 📏 Choose summary mode: **Short**, **Medium**, or **Detailed**
- 📝 Choose format: **Paragraph** or **Bullet Points** *(future)*
- 🔄 Extractive vs Abstractive summaries *(future switchable)*
- 💾 Save summaries for future access *(admin interface optional)*
- 🌐 Simple Flask web app with minimal setup

---

## 🧰 Tech Stack

| Layer         | Technology                           |
|---------------|---------------------------------------|
| Backend       | Python, Flask                         |
| ML Model      | Hugging Face Transformers (`T5`)      |
| PDF Parser    | PyPDF2                                |
| UI            | HTML + Jinja2                         |
| Storage (opt) | SQLite (via SQLAlchemy or raw)        |

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdfmyguy.git
cd pdfmyguy
