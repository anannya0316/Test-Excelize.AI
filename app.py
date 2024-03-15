import streamlit as st

def display_image_with_boxes(image, boxes):
    st.image(image, use_column_width=True)
    image_width = st.image(image).width
    image_height = st.image(image).height

    for box in boxes:
        box_left = box["x"] * image_width
        box_top = box["y"] * image_height
        box_width = box["width"] * image_width
        box_height = box["height"] * image_height

        st.markdown(
            f'<div style="position:relative; left:{box_left}px; top:{box_top}px; width:{box_width}px; height:{box_height}px; border:2px solid red;"></div>',
            unsafe_allow_html=True
        )

def main():
    image = "path_to_your_image.jpg"  # Change this to the path of your image
    boxes = [{"x": 0.1, "y": 0.1, "width": 0.2, "height": 0.2}]  # Example box, change as needed

    display_image_with_boxes(image, boxes)

if __name__ == "__main__":
    main()

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
