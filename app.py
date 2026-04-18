import streamlit as st
from PIL import Image
from api_calling import perform_ai_operations

# Title and description
st.title("Code Debugger")

st.header("AI Coder debugger App")
st.divider()
st.subheader("Upload your error screenshot and let the AI find and fix bugs for you!")

# take images from user
upload_images = st.file_uploader(
    "Upload your error screenshots", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True)

# select options for operations
options = st.selectbox(
    "Select the operations you want to perform", 
    ["Find Bugs", "Fix Bugs", "Explain Errors"])

# display uploaded images and selected options
if not upload_images:
    st.warning("Please upload at least one error screenshot to proceed.")
if not options:
    st.warning("Please select an operation to perform.")

if upload_images and options:
    st.markdown("You have uploaded images are: ")
    cols = st.columns(len(upload_images))
    for idx, image in enumerate(upload_images):
        with cols[idx]:
            st.image(image, caption=f"Uploaded Image {idx + 1}")

    st.markdown(f"You have selected the operation: **{options}**")

# submit button to initiate AI processing
button_clicked = st.button("Click the button to Initiate AI", key="submit_button", type="primary")

# perform AI operations when the button is clicked
if button_clicked:
    if not upload_images:
        st.error("Please upload at least one error screenshot to proceed.")
    if not options:
        st.error("Please select an operation to perform.")

    # If both images and options are provided, simulate AI processing
    if upload_images and options:
        # Convert uploaded images to PIL format for AI processing
        pil_images = [Image.open(image) for image in upload_images]
        
        # Create a container to display AI processing results
        with st.container(border=True):
            # Simulate AI processing with a spinner
            with st.spinner("Processing your request with AI..."):
                result = perform_ai_operations(pil_images, options)
                st.success("AI has completed the operation successfully!")
                st.markdown(result)