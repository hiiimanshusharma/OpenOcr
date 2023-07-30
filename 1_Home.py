import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    # Set page config
    st.set_page_config(
        page_title="OpenOCR",
        layout="wide",
    )

    # Add a beautiful image
    # st.image(r"C:\Users\91830\Desktop\OpenOCR\pages\OCR_logo.png", use_column_width=True)

    st.title("OpenOCR")

    #subtitle
    st.markdown("## Optical Character Recognition - Extract `Text` from  `Images`")

    st.markdown("")
    # Add some sections or features
    st.header("Features:")
    if st.button('Extract Text'):
        switch_page('2_OCR')
    if st.button('- Image Convertor'):
        switch_page('Image_Convertor')
    if st.button('- Realtime Text Extraction'):
        switch_page('Realtime_ocr')

    # Add a nice footer
    st.markdown("---")
    # st.write('')
    if st.button('Contact Me'):
        switch_page('Contact_Me')



    st.write('')
    if st.button('Return to Home'):
        switch_page('Home')

if __name__ == "__main__":
    main()


st.caption("Made by Himanshu Sharma")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
