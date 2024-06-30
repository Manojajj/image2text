import streamlit as st
from PIL import Image
import pytesseract

def main():
    st.title('Image 2 Text Extractor')

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write('')
        st.write('Extracted Text:')

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image)

        st.write(extracted_text)

if __name__ == '__main__':
    main()
