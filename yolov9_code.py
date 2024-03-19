
def perform_object_detection(uploaded_file):
  from google.colab import drive
  drive.mount('/content/drive')
  #%cd /content/drive/MyDrive/yolov9-main
  !python detect.py --weights /content/drive/MyDrive/yolov9-main/yolov9-c.pt --source {} --device cpu".format(uploaded_file)
  import os
  from IPython.display import Image, display

  output_dir = "/content/drive/MyDrive/yolov9-main/runs/train/exp9"

  # Get a list of all files in the directory
  file_list = os.listdir(output_dir)

  # Filter out only the image files
  image_files = [f for f in file_list if f.endswith('.jpg')]

  # Display each image
  for image_file in image_files:
      display(Image(filename=os.path.join(output_dir, image_file), width=1000))

# import streamlit as st
# import os

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
#     def perform_object_detection():
#         from google.colab import drive
#         drive.mount('/content/drive')
#         !wget -P /mydrive/yolov9 https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt
        
#         !wget -P /mydrive/yolov9 https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt !git clone https://github.com/WongKinYiu/yolov9.git
#         %cd /content/drive/MyDrive/yolov9-main
#         !pip install -r requirements.txt
#         !python detect.py --weights /content/drive/MyDrive/yolov9-main/yolov9-c.pt --source image_path  --device cpu
#         import os
#         from IPython.display import Image, display
        
#         output_dir = "/content/drive/MyDrive/yolov9-main/runs/detect/exp_29"
        
#         # Get a list of all files in the directory
#         file_list = os.listdir(output_dir)
        
#         # Filter out only the image files
#         image_files = [f for f in file_list if f.endswith('.jpg')]
        
#         # Display each image
#         for image_file in image_files:
#             display(Image(filename=os.path.join(output_dir, image_file), width=1000))


