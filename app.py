import streamlit as st
from dotenv import load_dotenv 
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs: # pdf is single document and pdf_docs is every pdf
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs",page_icon=":books:")
    st.header("Chat with PDFs :books:")
    st.text_input("Ask question")
    
    with st.sidebar:
        st.subheader("Documents")
        pdf_docs= st.file_uploader("Upload PDF",accept_multiple_files=True)
                
        if st.button("Process"):
            #get pdf text 
            raw_text= get_pdf_text(pdf_docs)
            st.write(raw_text)
            #get text chunks
            
            #create embeddings
            
        
if __name__ == "__main__":
    main()
        