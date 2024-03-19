
# import streamlit as st
# from yolov9_code import perform_object_detection

# def main():
#     st.title("Image Uploader")

#     # File uploader widget
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         # Display the uploaded image
#         st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

#         # Call the perform_object_detection function
#         perform_object_detection(uploaded_file)

# if __name__ == "__main__":
#     main()

import streamlit as st
from PIL import Image
import os
from google.colab import drive

# Function to perform object detection
def perform_object_detection(uploaded_file):
    # Mount Google Drive
    drive.mount('/content/drive')

    # Run YOLOv9 detection script
    !python detect.py --weights /content/drive/MyDrive/yolov9-main/yolov9-c.pt --source {uploaded_file} --device cpu
    
    # Define the output directory
    output_dir = "/content/drive/MyDrive/yolov9-main/runs/train/exp9"

    # Display the output images
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            st.image(Image.open(os.path.join(output_dir, filename)), caption='Detected Objects', use_column_width=True)

def main():
    st.title("YOLOv9 Object Detection")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Perform object detection
        perform_object_detection(uploaded_file)

if __name__ == "__main__":
    main()
