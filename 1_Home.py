import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.markdown("""
<style>
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("OpenOCR")

st.markdown("# OCR and Image Conversion: Your One-Stop Shop")

#st.write('')
if st.button('Extract Now'):
    switch_page('Extract Now')

st.markdown("Not have picture in your browser. Don't Worry!!")
#st.write('')
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
