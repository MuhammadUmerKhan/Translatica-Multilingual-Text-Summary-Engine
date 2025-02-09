# 📝 Multilingual Text Translation & Summarization System

![Translation & Summarization](https://618media.com/wp-content/uploads/2024/02/claude-ai-s-language-translation-capabilities.webp)

In today's interconnected world, seamless communication across languages is crucial. This project provides a **Multilingual Text Translation & Summarization System** that allows users to translate text between multiple languages and summarize content efficiently. The system is built using state-of-the-art NLP models and deployed as a user-friendly web application.

This repository offers a complete solution for **text translation and summarization**, leveraging pre-trained models to deliver accurate and efficient results.

## ❤️ Table of Contents
- [Problem Statement](#problem-statement)
- [Methodology](#methodology)
- [Key Features](#key-features)
- [Usage Instructions](#usage-instructions)
- [Running the Project](#running-the-project)
- [Live Demo](#live-demo)
- [Future Plans](#future-plans)
- [License](#license)

---

## ❓ Problem Statement

Language barriers and lengthy documents often pose challenges for communication and information retrieval. Traditional translation tools may not support all languages effectively, and manual summarization is time-consuming.

This project aims to:
- 📝 **Translate text between multiple languages** using advanced NLP models.
- 📚 **Summarize large text documents** to extract key information.
- 🌐 **Provide an easy-to-use web interface** for real-time translation and summarization.

---

## 🛠️ Methodology

1. **Text Translation:**
   - Utilize **Facebook's M2M100 model** for multilingual translation.
   - Support translation between various language pairs.

2. **Text Summarization:**
   - Use **Facebook's BART-Large-CNN model** for abstractive summarization.
   - Handle long documents efficiently.

3. **User Interface:**
   - Build an interactive web application using **Streamlit**.
   - Provide dropdown selections for choosing languages.
   - Support text input and file uploads.

---

## 🚀 Key Features

- 🌐 **Multilingual Translation:** Translate text between multiple languages.
- 📚 **Text Summarization:** Extract concise summaries from long documents.
- 🏠 **User-Friendly Interface:** Simple UI for easy interaction.
- 💡 **Fast & Efficient:** Runs on Hugging Face Spaces with optimized models.
- 🗓 **File Upload Support:** Upload text files for summarization.

---

## 🚀 Usage Instructions

### 📂 Clone the Repository
```bash
git clone https://github.com/MuhammadUmerKhan/Multilingual-Text-Translation---Summarization-System.git
cd Multilingual-Translation-Summarization
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### ⬇️ Download Pretrained Models
```python
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer, BartForConditionalGeneration, BartTokenizer

# Load translation model
translation_model_name = "facebook/m2m100_418M"
translation_tokenizer = M2M100Tokenizer.from_pretrained(translation_model_name)
translation_model = M2M100ForConditionalGeneration.from_pretrained(translation_model_name)

# Load summarization model
summarization_model_name = "facebook/bart-large-cnn"
summarize_tokenizer = BartTokenizer.from_pretrained(summarization_model_name)
summarize_model = BartForConditionalGeneration.from_pretrained(summarization_model_name)
```

---

## 🏃‍ Running the Project

### 🌐 Start the Streamlit App
```bash
streamlit run app.py
```

Open your browser and navigate to:
```
http://localhost:8501/
```

---

## 🛡️ Future Plans

- 🌍 Expand support for more languages.
- 🌎 Improve summarization quality with newer transformer models.
- 🔗 Integrate speech-to-text for real-time translation.
- 🌐 Deploy as a browser extension or mobile app.
- ⚙️ **Try more advanced Large Language Models (LLMs)** to enhance translation and summarization quality, as our current model choices were limited due to computational constraints.

---

### Screenshots

1. **Translation Interference**  
   ![Question Answering](https://github.com/MuhammadUmerKhan/Multilingual-Text-Translation---Summarization-System/blob/main/imgs/ss2.png)

2. **Summarization Evidence**  
   ![Supporting Evidence](https://github.com/MuhammadUmerKhan/Multilingual-Text-Translation---Summarization-System/blob/main/imgs/ss1.png)

---

## 💖 Conclusion

This project demonstrates the power of **multilingual NLP models** for real-world applications. By combining translation and summarization in an easy-to-use web app, we enable seamless communication and knowledge extraction across languages.

---

📚 **Feel free to contribute, raise issues, or suggest improvements!**

📌 **License:** MIT License 🔒