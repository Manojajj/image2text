import streamlit as st
from PIL import Image
import boto3
from io import BytesIO

def main():
    st.title('Image 2 Text Extractor')

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write('')
        st.write('Extracted Text:')

        # Convert the image to bytes
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format=image.format)
        img_byte_arr = img_byte_arr.getvalue()

        # Initialize Textract client
        client = boto3.client('textract')

        # Call Amazon Textract
        response = client.detect_document_text(Document={'Bytes': img_byte_arr})

        # Extract detected text
        extracted_text = ""
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                extracted_text += item['Text'] + '\n'

        st.write(extracted_text)

if __name__ == '__main__':
    main()
