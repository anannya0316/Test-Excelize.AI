import streamlit as st
import pandas as pd
from PIL import Image

# Function to display images and bounding boxes
def display_image_with_boxes(image, boxes):
    html_code = ""
    for box in boxes:
        if "x" in box and "y" in box:
            html_code += f'<div style="position:absolute; left:{box["x"]}px; top:{box["y"]}px; width:100px; height:100px; border:2px solid red;"></div>'
        else:
            print("Invalid box:", box)
    st.markdown(html_code, unsafe_allow_html=True)


def main():
    st.title("Image Annotation Tool")

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Render bounding boxes
        boxes = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 200},
    # Add more boxes as needed
]
  # Example bounding box coordinates
        display_image_with_boxes(image, boxes)

        # Button to save annotations
        if st.button("Save Annotations"):
            save_annotations(boxes)

def save_annotations(boxes):
    # Convert bounding boxes to DataFrame
    df = pd.DataFrame(boxes)

    # Save DataFrame as CSV
    df.to_csv("annotations.csv", index=False)
    st.success("Annotations saved successfully.")

if __name__ == "__main__":
    main()
