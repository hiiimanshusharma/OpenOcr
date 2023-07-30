import streamlit as st
from PIL import Image
import io
import PIL.TiffImagePlugin
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Image Converter", layout="wide")

selected = option_menu(
    menu_title=None,
    options=["JPG to PNG", "JPG to TIF", "PNG to JPG", "PNG to TIF", "TIF to JPG", "TIF to PNG"],
    icons=["card-image", "file-image", "file-image-fill", "image-alt", "image-fill", "image"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

if selected == "JPG to PNG":
    st.header("JPG to PNG Converter")

    # Create file upload widget
    uploaded_file = st.file_uploader("Upload a JPG file", type="jpg")

    # Convert JPG to PNG if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to PNG
        image = Image.open(io.BytesIO(uploaded_file.read()))
        png_image = io.BytesIO()
        image.save(png_image, format='PNG')

        # Display converted PNG image
        st.image(png_image, caption='Converted PNG image')

        # Create download button for converted PNG file
        download_button = st.download_button(
            label='Download PNG file',
            data=png_image.getvalue(),
            file_name='converted_image.png',
            mime='image/png'
        )

if selected == "JPG to TIF":
    st.header("JPG to TIFF Converter")

    # Create file upload widget
    uploaded_file = st.file_uploader("Upload a JPG file", type="jpg")

    # Convert JPG to TIFF if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to TIFF
        image = Image.open(io.BytesIO(uploaded_file.read()))
        tiff_image = io.BytesIO()
        image.save(tiff_image, format='TIFF')

        # Display converted TIFF image
        st.image(tiff_image, caption='Converted TIFF image')

        # Create download button for converted TIFF file
        download_button = st.download_button(
            label='Download TIFF file',
            data=tiff_image.getvalue(),
            file_name='converted_image.tif',
            mime='image/tiff'
        )

if selected == "PNG to JPG":
    st.header("PNG to JPG Converter")

    # Create file upload widget
    uploaded_file = st.file_uploader("Upload a PNG file", type="png")

    # Convert PNG to JPG if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to JPG
        image = Image.open(io.BytesIO(uploaded_file.read()))
        jpg_image = io.BytesIO()
        image.convert('RGB').save(jpg_image, format='JPEG')

        # Display converted JPG image
        st.image(jpg_image, caption='Converted JPG image')

        # Create download button for converted JPG file
        download_button = st.download_button(
            label='Download JPG file',
            data=jpg_image.getvalue(),
            file_name='converted_image.jpg',
            mime='image/jpeg'
        )
#
if selected == "PNG to TIF":
    st.title("PNG to TIFF Converter")

# Create file upload widget
    uploaded_file = st.file_uploader("Upload a PNG file", type="png")

    # Convert PNG to TIFF if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to TIFF
        image = Image.open(io.BytesIO(uploaded_file.read()))
        tiff_image = io.BytesIO()
        image.save(tiff_image, format='TIFF')

        # Display converted TIFF image
        st.image(tiff_image, caption='Converted TIFF image')

        # Create download button for converted TIFF file
        download_button = st.download_button(
            label='Download TIFF file',
            data=tiff_image.getvalue(),
            file_name='converted_image.tif',
            mime='image/tiff'
        )

if selected == "TIF to JPG":
    st.title("TIFF to JPG Converter")

    # Create file upload widget
    uploaded_file = st.file_uploader("Upload a TIFF file", type="tif")

    # Convert TIFF to JPG if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to JPG
        image = Image.open(io.BytesIO(uploaded_file.read()))
        jpg_image = io.BytesIO()
        image.convert('RGB').save(jpg_image, format='JPEG')

        # Display converted JPG image
        st.image(jpg_image, caption='Converted JPG image')

        # Create download button for converted JPG file
        download_button = st.download_button(
            label='Download JPG file',
            data=jpg_image.getvalue(),
            file_name='converted_image.jpg',
            mime='image/jpeg'
        )

if selected == "TIF to PNG":
    st.title("TIFF to PNG Converter")

    # Create file upload widget
    uploaded_file = st.file_uploader("Upload a TIFF file", type="tif")

    # Convert TIFF to PNG if file is uploaded
    if uploaded_file is not None:
        # Load image and convert to PNG
        image = Image.open(io.BytesIO(uploaded_file.read()))
        png_image = io.BytesIO()
        image.save(png_image, format='PNG')

        # Display converted PNG image
        st.image(png_image, caption='Converted PNG image')

        # Create download button for converted PNG file
        download_button = st.download_button(
            label='Download PNG file',
            data=png_image.getvalue(),
            file_name='converted_image.png',
            mime='image/png'
        )


st.markdown("# Know About Image Formats")

st.markdown("## JPG")

st.markdown("(short for Joint Photographic Experts Group) is a commonly used method of lossy compression for digital images, particularly for those images produced by digital photography")



st.markdown("## PNG")

st.markdown("(short for Portable Network Graphics) is a file format used for lossless image compression. PNG has almost entirely replaced the Graphics Interchange Format (GIF) that was widely used in the past.")

st.markdown("## TIFF")

st.markdown("(short for Tag Image File Format) is a computer file used to store raster graphics and image information. A favourite among photographers, TIFFs are a handy way to store high-quality images before editing if you want to avoid lossy file formats.")


st.caption("Made by Himanshu Sharma")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
                        """
st.markdown(hide_st_style, unsafe_allow_html=True)
