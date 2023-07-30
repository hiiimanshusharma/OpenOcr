# import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing
from numpy import asarray
from streamlit_extras.switch_page_button import switch_page
import os
from google.cloud import vision_v1
import torch
torch.cuda.empty_cache()
st.set_page_config(page_title="OpenOCR", layout="wide")

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


#title
st.title("OpenOCR")

#subtitle
st.markdown("## Optical Character Recognition - Extract `Text` from  `Images`")

st.markdown("")

def extract_text_from_image(image):
    # Instantiates a client
    client = vision_v1.ImageAnnotatorClient()

    # Perform OCR (Optical Character Recognition) on the image
    response = client.text_detection(image=image)

    # Process the response and extract the text
    text_annotations = response.text_annotations
    if text_annotations:
        return text_annotations[0].description
    else:
        return "No text found in the image."

def main():
    # st.title("Text Extraction from Image using Google Cloud Vision API")
    st.write("Upload an image and let the magic happen!")

    # Allow the user to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Read the image file
        content = uploaded_file.read()

        # Perform text extraction
        image = vision_v1.Image(content=content)
        extracted_text = extract_text_from_image(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)

if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"openocr-394310-95d8b763df38.json"
    main()


st.markdown("Want to convert image formats")
# st.write('')
if st.button('Image Convertor'):
    switch_page('Image_Convertor')

st.markdown("Having Trouble")
# st.write('')
if st.button('Contact Me'):
    switch_page('Contact_Me')



st.write('')
if st.button('Return to Home'):
    switch_page('Home')


st.markdown("---")

st.markdown("## More About the technology")

st.markdown("""<p style='text-align: left; color: White;'>Optical character recognition (OCR) is sometimes referred to as text recognition. An OCR program extracts and repurposes data from scanned documents, camera images and image-only pdfs. OCR software singles out letters on the image, puts them into words and then puts the words into sentences, thus enabling access to and editing of the original content. It also eliminates the need for manual data entry.

OCR systems use a combination of hardware and software to convert physical, printed documents into machine-readable text. Hardware — such as an optical scanner or specialized circuit board — copies or reads text; then, software typically handles the advanced processing.

OCR software can take advantage of artificial intelligence (AI) to implement more advanced methods of intelligent character recognition (ICR), like identifying languages or styles of handwriting. The process of OCR is most commonly used to turn hard copy legal or historical documents into pdf documents so that users can edit, format and search the documents as if created with a word processor.</p>""", unsafe_allow_html=True)



st.caption("Made by Himanshu Sharma")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
