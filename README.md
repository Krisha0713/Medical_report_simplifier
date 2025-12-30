👩‍💻 Author
Krishna Priya R
CSE Student | AI/ML Enthusiast

🩺 Medical Report Simplifier (NLP + ML + Flask)
An AI-powered web application that simplifies complex medical reports into easy-to-understand language using Natural Language Processing and Transformer-based models, helping patients and non-medical users better understand healthcare information.

🚀 Features
🧠 NLP-based medical text simplification
📄 Supports long medical reports
🔍 Medical term detection using NER
✂️ Sentence restructuring & jargon removal
📊 Readability-focused output
🧪 Transformer-based text generation
🌐 Simple web interface using Flask
🔐 No patient-identifiable data storage

🏗 Project Structure

medical_report_simplifier/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   └── simplifier_model/
│   ├── utils/
│   │   ├── preprocess.py
│   │   ├── simplify.py
│   │   └── ner.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── run.py
└── README.md


🧪 Input

Medical report text (copied or uploaded)

Clinical notes

Diagnostic summaries

Lab report explanations

📤 Output

Simplified medical explanation

Easy-to-read sentences

Reduced medical jargon

Preserved medical meaning

Patient-friendly language

🧠 ML Concepts Used

Natural Language Processing (NLP)

Text Simplification

Transformer Models (T5 / BERT-based)

Named Entity Recognition (NER)

Domain Adaptation (Medical NLP)

Readability Analysis

⚙️ Tech Stack

Python

Flask

spaCy / scispaCy

PyTorch

HTML / CSS / JavaScript

▶️ How to Run

1️⃣ Install dependencies

pip install flask torch transformers spacy scikit-learn


2️⃣ Run the application

python run.py
