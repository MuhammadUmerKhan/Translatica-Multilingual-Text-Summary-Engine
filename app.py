import streamlit as st  # Import Streamlit for UI
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer, BartForConditionalGeneration, BartTokenizer  # Import Hugging Face models
from PyPDF2 import PdfReader  # Import for PDF processing

# ----------------- SETTING UP THE PAGE ----------------- #
st.set_page_config(
    page_title="Multilingual Translator & Summarizer",  # Set page title
    page_icon="🌍",  # Set page icon
    layout="wide"  # Set layout to wide for better UI
)

# Title and description of the app
st.title("🌍 Multilingual Translation & Summarization")
st.write("Translate text between multiple languages or summarize content.")

# ----------------- LOADING PRETRAINED MODELS ----------------- #
@st.cache_resource  # Cache model loading to improve performance
def load_translation_model():
    """Loads the multilingual translation model."""
    model_name = "facebook/m2m100_418M"  # Using Facebook's M2M100 model (418M version)
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)  # Load tokenizer
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)  # Load model
    return tokenizer, model  # Return loaded tokenizer and model

@st.cache_resource  # Cache summarization model for efficiency
def load_summarization_model():
    """Loads the text summarization model."""
    model_name = "facebook/bart-large-cnn"  # Using Facebook's BART model for summarization
    tokenizer = BartTokenizer.from_pretrained(model_name)  # Load tokenizer
    model = BartForConditionalGeneration.from_pretrained(model_name)  # Load model
    return tokenizer, model  # Return loaded tokenizer and model

# Load models
translation_tokenizer, translation_model = load_translation_model()
summarize_tokenizer, summarize_model = load_summarization_model()

# ----------------- SUPPORTED LANGUAGES ----------------- #
# Dictionary mapping language names to model-supported language codes
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi"
}

# ----------------- TRANSLATION FUNCTION ----------------- #
def translate_text(text, src_lang, tgt_lang):
    """Translates text from source language to target language."""
    translation_tokenizer.src_lang = src_lang  # Set the source language
    encoded_text = translation_tokenizer(text, return_tensors="pt", truncation=True, max_length=512)  # Tokenize text

    # Generate translated text
    generated_tokens = translation_model.generate(
        **encoded_text, forced_bos_token_id=translation_tokenizer.get_lang_id(tgt_lang)
    )
    
    translated_text = translation_tokenizer.decode(generated_tokens[0], skip_special_tokens=True)  # Decode output
    return translated_text  # Return translated text

# ----------------- SUMMARIZATION FUNCTION ----------------- #
def summarize_text(text):
    """Summarizes the input text."""
    inputs = summarize_tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)  # Tokenize text
    summary_ids = summarize_model.generate(
        inputs.input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True
    )
    
    return summarize_tokenizer.decode(summary_ids[0], skip_special_tokens=True)  # Decode output and return summary

# ----------------- STREAMLIT USER INTERFACE ----------------- #

# Create tabs for translation and summarization
tab1, tab2 = st.tabs(["🌍 Translate", "📄 Summarize"])

# TRANSLATION TAB
with tab1:
    st.subheader("🔄 Multilingual Text Translation")  # Section heading
    input_text = st.text_area("Enter text to translate:", height=100)  # Input text field
    
    # Language selection for source and target
    col1, col2 = st.columns(2)
    with col1:
        src_lang = st.selectbox("Select source language:", list(LANGUAGES.keys()), index=0)
    with col2:
        tgt_lang = st.selectbox("Select target language:", list(LANGUAGES.keys()), index=1)

    # Translate button
    if st.button("Translate"):
        if input_text:
            if src_lang == tgt_lang:  # Check if source and target languages are the same
                st.warning("❌ Source and target languages must be different.")
            else:
                translated_text = translate_text(input_text, LANGUAGES[src_lang], LANGUAGES[tgt_lang])
                st.success("✅ Translation Complete!")
                st.text_area("Translated Text:", translated_text, height=100)  # Display translated text
        else:
            st.warning("Please enter text to translate.")  # Show warning if no input is provided

# SUMMARIZATION TAB
with tab2:
    st.subheader("📄 Text Summarization")  # Section heading
    
    # Radio buttons to select text input method
    summary_input_type = st.radio("Select input type:", ["Enter Text", "Upload PDF"], horizontal=True)
    
    # Text input option
    if summary_input_type == "Enter Text":
        text_to_summarize = st.text_area("Enter text for summarization:", height=200)
        
        # Summarize button
        if st.button("Summarize Text"):
            if text_to_summarize:
                summary = summarize_text(text_to_summarize)  # Call summarization function
                st.success("✅ Summarization Complete!")
                st.text_area("Summarized Text:", summary, height=100)  # Display summary
            else:
                st.warning("Please enter text to summarize.")  # Show warning if no input

    # PDF upload option
    elif summary_input_type == "Upload PDF":
        uploaded_file = st.file_uploader("📂 Upload a PDF document", type=["pdf"])  # Upload PDF
        
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)  # Read PDF
            extracted_text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])  # Extract text
            
            if extracted_text.strip():  # Check if text was extracted
                if st.button("Summarize PDF"):
                    summary = summarize_text(extracted_text[:4096])  # Limit input size for summarization
                    st.success("✅ Summarization Complete!")
                    st.text_area("Summarized Text:", summary, height=100)  # Display summary
            else:
                st.error("❌ Could not extract text from the uploaded PDF.")  # Show error if no text was extracted

# ----------------- FOOTER ----------------- #
st.markdown("---")
st.markdown("🔹 Built with 🤖 AI & Streamlit | Powered by **Hugging Face Models**")  # Footer text
