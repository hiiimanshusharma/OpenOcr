import streamlit as st


def main():
    # Set page config
    st.set_page_config(
        page_title="OpenOCR",
        layout="wide",
    )


    st.title("OpenOCR")

    #subtitle
    st.markdown("## Optical Character Recognition - Extract `Text` from  `Images`")

    st.markdown("")
    # Add some sections or features
    st.header("Features:")
    st.markdown("- OCR")
    st.markdown("- Realtime OCR")
    st.markdown("- Image Convertor")


    st.markdown("---")
    st.caption("Made by Himanshu Sharma")

if __name__ == "__main__":
    main()




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
