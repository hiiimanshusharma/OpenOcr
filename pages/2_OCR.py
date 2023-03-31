import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing
from streamlit_extras.switch_page_button import switch_page
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.set_page_config(page_title="OpenOCR", layout="wide")

#title
st.title("OpenOCR")

#subtitle
st.markdown("## Optical Character Recognition - Extract `Text` from  `Images`")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_data
def load_model():
    reader = ocr.Reader(['en','hi'],model_storage_directory='.')
    return reader

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner(" Processing "):


        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        sentence = " ".join(result_text)
        st.write(result_text)
        st.write(sentence)
    st.success("Here you go!")
    st.write("Upload an Image")

st.markdown("Not have picture in your storage. Don't Worry!!")
st.write('')
if st.button('Live OCR'):
    switch_page('Live_OCR')


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
