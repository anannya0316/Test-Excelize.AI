
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
import subprocess
import os
import tempfile
from PIL import Image
import streamlit as st

def perform_object_detection(uploaded_file):
    # Define the path to the YOLOv9 detection script
    detect_script = '/content/drive/MyDrive/yolov9-main/detect.py'
    
    # Create a temporary directory to store the output images
    output_dir = tempfile.mkdtemp()
    
    # Run YOLOv9 detection script using subprocess
    subprocess.run(['python', detect_script, '--weights', '/content/drive/MyDrive/yolov9-main/yolov9-c.pt', '--source', str(uploaded_file), '--device', 'cpu', '--output', output_dir])
    
    # Display the output images with detected labels
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            image_path = os.path.join(output_dir, filename)
            st.image(image_path, caption='Detected Objects', use_column_width=True)

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
