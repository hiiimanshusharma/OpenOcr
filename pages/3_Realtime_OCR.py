import os
import cv2
from google.cloud import vision_v1
import numpy as np
import streamlit as st

st.write('')
if st.button('Return to Home'):
    switch_page('Home')

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
    st.title("Real-Time Text Detection in Live Video Stream")
    st.write("Upload an image and let the magic happen!")

    # Set up OpenCV video capture
    cap = cv2.VideoCapture(0)

    # Create a placeholder for displaying the video stream
    video_placeholder = st.empty()

    # Create a list to store the extracted text
    extracted_texts = []

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to capture video.")
            break

        # Convert the frame from BGR to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform text extraction
        image = vision_v1.Image(content=cv2.imencode(".jpg", frame_rgb)[1].tobytes())
        extracted_text = extract_text_from_image(image)

        # Overlay the extracted text on the video frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottom_left_corner = (10, frame.shape[0] - 10)
        font_scale = 0.6
        font_color = (255, 255, 255)  # White color
        line_type = 1
        cv2.putText(frame, extracted_text, bottom_left_corner, font, font_scale, font_color, line_type)

        # Add the extracted text to the list
        extracted_texts.append(extracted_text)

        # Display the frame with the overlaid text
        video_placeholder.image(frame, channels="BGR", use_column_width=True)

        # Join the extracted text list with newline characters and display in Streamlit
        all_extracted_text = "\n".join(extracted_texts)
        st.text("All Extracted Text:")
        st.text(all_extracted_text)

    # Release the video capture and close the Streamlit app
    cap.release()

if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"openocr-394310-95d8b763df38.json"
    main()
