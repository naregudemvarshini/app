import streamlit as st
import pdfplumber

st.set_page_config(page_title="ClauseWise Legal Analyzer")

st.title("ClauseWise: Legal Document Analyzer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], key="file_uploader")

extracted_text = ""

if uploaded_file:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"
    except Exception as e:
        st.error(f"Failed to extract text: {e}")

    st.subheader("Extracted Text Preview")
    st.text_area("Text:", extracted_text[:2000], height=250, key="text_preview")

    # FIX: UNIQUE KEY ADDED
    show_raw = st.sidebar.checkbox("Show raw text", value=False, key="raw_text_toggle")

    if show_raw:
        st.subheader("Raw Full Text")
        st.write(extracted_text)
