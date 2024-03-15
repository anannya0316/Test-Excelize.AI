import streamlit as st
import pandas as pd
from PIL import Image

# Function to display images and bounding boxes
def display_image_with_boxes(image, boxes):
    st.image(image, use_column_width=True)
    for box in boxes:
        st.markdown(
            f'<div style="position:absolute; left:{box["x"]}px; top:{box["y"]}px; width:{box["width"]}px; height:{box["height"]}px; border:2px solid red;"></div>',
            unsafe_allow_html=True
        )

def main():
    st.title("Image Annotation Tool")

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Render bounding boxes
        boxes = [{"x": 100, "y": 100, "width": 50, "height": 50}, ...]  # Example bounding box coordinates
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
