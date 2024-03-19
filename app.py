
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
