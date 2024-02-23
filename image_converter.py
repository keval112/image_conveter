import streamlit as st
from PIL import Image
import os
import tempfile

def convert_image(image_path, new_format):
    with Image.open(image_path) as img:
        new_name = image_path.name.split('.')[0] + '.' + new_format
        temp_dir = tempfile.mkdtemp()  # Create a temporary directory
        final_path = os.path.join(temp_dir, new_name)
        img.save(final_path)
        st.success('Image saved at ' + final_path)
        return final_path  # Return the final path of the converted image


# Function to generate a download link for the image
def get_image_download_link(file_path):
    filename = os.path.basename(file_path)
    href = f'<a href="data:file/{new_format};base64,{file_path}" download="{filename}">Click here to download your image</a>'
    return href

st.title('Image converter')
image_path = st.file_uploader('Enter your image', type=['png', 'jpeg', 'jpg'])
new_format = st.selectbox('Select output format', ['png', 'jpeg', 'jpg'])

if st.button('Convert'):
    if image_path is not None:
        converted_path = convert_image(image_path, new_format)
        st.markdown(get_image_download_link(converted_path), unsafe_allow_html=True)
    else:
        st.error("Please upload the image")

