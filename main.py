import streamlit as st
from PIL import Image
import paddleocr
from paddleocr import PaddleOCR, draw_ocr

def main():
    st.title('Image 2 Text Extractor')

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write('')
        st.write('Extracted Text:')

        # Initialize PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        
        # Perform OCR
        result = ocr.ocr(image, cls=True)
        
        # Extract and display text
        for line in result:
            line_text = line[1][0]
            st.write(line_text)

if __name__ == '__main__':
    main()
