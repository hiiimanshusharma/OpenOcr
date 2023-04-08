import streamlit as st
import cv2
import easyocr
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.set_page_config(page_title="Live OCR", layout="wide")
# Initialize the OCR reader
reader = easyocr.Reader(['en','hi'])

# Create a function to perform OCR on the image
def ocr(image):
    result = reader.readtext(image)
    text = ''
    for detection in result:
        text += detection[1] + ' '
    return text

# Create the Streamlit app
def main():
    st.title("Real-time OCR with EasyOCR")
    if st.button("Use Webcam"):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR")
            text = ocr(frame)
            st.write(text)
        cap.release()

    st.markdown("## Use Real Time OCR feature")
    if st.button("OCR on livestream"):
        # Open the video capture device (0 is usually the default webcam)
        cap = cv2.VideoCapture(0)

        # Create a window for the video stream
        cv2.namedWindow("Live Stream", cv2.WINDOW_NORMAL)

        # Loop through each frame of the video stream
        while True:
            ret, frame = cap.read()

            # If there was an error reading the frame, break the loop
            if not ret:
                break

            # Perform OCR on the frame
            text = ocr(frame)

            # Display the text on the frame
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Display the frame in the window
            cv2.imshow("Live Stream", frame)

            # Exit the loop if the user presses the 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture device and close the window
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



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
