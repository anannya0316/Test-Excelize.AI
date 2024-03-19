
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
import requests
from PIL import Image

# Function to download file content from Google Drive
def download_file_from_google_drive(file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    return response.content

# Replace 'YOUR_FILE_ID' with the file ID from your Google Drive link
file_id = '19KbrZ_swK_jbS0Qv2sHZibh8XGEh5wBs'

# Download the file content from Google Drive
file_content = download_file_from_google_drive(file_id)

# Save the file content to a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix='.pt') as temp_file:
    temp_file.write(file_content)
    save_path = temp_file.name

def perform_object_detection(uploaded_file):
    # Define the path to the YOLOv9 detection script
    detect_script = 'detect.py'
    
    # Create a temporary directory to store the output images
    output_dir = tempfile.mkdtemp()
    
    # Save the uploaded image to a temporary file
    with open(os.path.join(output_dir, 'uploaded_image.jpg'), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Run YOLOv9 detection script using subprocess
    subprocess.run(['python', detect_script, '--weights', save_path, '--source', os.path.join(output_dir, 'uploaded_image.jpg'), '--device', 'cpu', '--output', output_dir])
    
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Display the output images with detected labels
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            image_path = os.path.join(output_dir, filename)
            st.image(Image.open(image_path), caption='Detected Objects', use_column_width=True)



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
