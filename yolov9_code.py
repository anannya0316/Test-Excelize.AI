
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


