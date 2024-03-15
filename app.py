import streamlit as st
import pandas as pd
from PIL import ImageDraw, Image

def display_image_with_boxes(image, boxes):
    st.image(image, use_column_width=True)
    drawn = ImageDraw.Draw(image)

    for box in boxes:
        xmin, ymin, xmax, ymax = box
        drawn.rectangle([xmin, ymin, xmax, ymax], outline="red")

    return image

def main():
    st.title("Image Annotation Tool")

    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        num_boxes = st.number_input("Number of Boxes", min_value=1, value=1)

        if st.button("Annotate"):
            boxes = []
            for _ in range(num_boxes):
                st.write(f"Box {_ + 1}")
                xmin = st.number_input("X min", min_value=0, max_value=image.width - 1, value=0)
                ymin = st.number_input("Y min", min_value=0, max_value=image.height - 1, value=0)
                xmax = st.number_input("X max", min_value=xmin + 1, max_value=image.width, value=image.width)
                ymax = st.number_input("Y max", min_value=ymin + 1, max_value=image.height, value=image.height)
                boxes.append((xmin, ymin, xmax, ymax))

            annotated_image = display_image_with_boxes(image.copy(), boxes)
            st.image(annotated_image, caption="Annotated Image", use_column_width=True)

            if st.button("Save Annotations"):
                df = pd.DataFrame(boxes, columns=["xmin", "ymin", "xmax", "ymax"])
                st.write("Annotations saved as CSV:")
                st.write(df)
                df.to_csv("annotations.csv", index=False)

if __name__ == "__main__":
    main()
