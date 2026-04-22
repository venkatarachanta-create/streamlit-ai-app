import streamlit as st
from textblob import TextBlob

# Title
st.title("AI Text Analyzer")

# Input box
text = st.text_area("Enter your text:")

# Button
if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        # Result
        if sentiment > 0:
            st.success("Positive 😊")
        elif sentiment < 0:
            st.error("Negative 😡")
        else:
            st.info("Neutral 😐")

        st.write(f"Sentiment Score: {sentiment}")
    else:
        st.warning("Please enter some text!")