
import streamlit as st
from yolov9_code import perform_object_detection

def main():
    st.title("Image Uploader")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Call the perform_object_detection function
        perform_object_detection(uploaded_file)

if __name__ == "__main__":
    main()

# import streamlit as st
# import os
# import shutil
# from PIL import Image

# # Call the function to perform object detection
# def perform_object_detection():
#         import subprocess
        
#         # Install dependencies
#         subprocess.run(["pip", "install", "pydantic", "opencv-python-headless"])
        
#         # Clone the YOLOv9 repository
#         subprocess.run(["git", "clone", "https://github.com/WongKinYiu/yolov9.git"])
        
#         # Change directory to YOLOv9
#         os.chdir("yolov9")
        
#         # Install requirements
#         subprocess.run(["pip", "install", "-r", "requirements.txt"])
        
#         # Run detection
#         subprocess.run(["python", "detect.py", "--weights", "yolov9-c.pt", "--source", image_path])
        
#         # # Move output image to Downloads folder
#         # output_image = "runs/detect/exp_29/image.jpg"
#         # downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
#         # shutil.move(output_image, downloads_path)
        
#         # Display the output image
#         display_image(downloads_path, "image.jpg")

#     # Function to display the image
# def display_image(directory, filename):
#     image = Image.open(os.path.join(directory, filename))
#     st.image(image, caption='Output Image', use_column_width=True)
    
# # Function to upload image and return its path
# def upload_image():
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
#     if uploaded_file is not None:
#         image_path = os.path.join("/tmp", uploaded_file.name)
#         with open(image_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#         return image_path
#     return None

# # Get the path of the uploaded image
# image_path = upload_image()

# # Now you can use the image_path variable in your YOLOv9 detection code
# if image_path:
#     perform_object_detection()
    
