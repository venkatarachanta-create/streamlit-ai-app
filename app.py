import streamlit as st
from textblob import TextBlob
import nltk

# Run only once (cached)
@st.cache_resource
def load_nltk():
    nltk.download('punkt')

load_nltk()

# UI
st.title("🤖 AI Text Analyzer")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("Positive 😊")
        elif sentiment < 0:
            st.error("Negative 😡")
        else:
            st.info("Neutral 😐")

        st.write(f"Score: {sentiment}")