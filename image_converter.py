import streamlit as st
from PIL import Image
import io
import base64

def convert_image(image_path, new_format):
    with Image.open(image_path) as img:
        new_name = image_path.name.split('.')[0] + '.' + new_format
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=new_format)
        img_bytes.seek(0)
        return img_bytes

def get_image_download_link(image_bytes, image_format):
    encoded_image = base64.b64encode(image_bytes.getvalue()).decode()
    href = f'<a href="data:image/{image_format};base64,{encoded_image}" download="converted_image.{image_format}">Click here to download your image</a>'
    return href


st.title('Image converter')
image_path = st.file_uploader('Enter your image', type=['png', 'jpeg', 'jpg'])
new_format = st.selectbox('Select output format', ['png', 'jpeg', 'jpg'])

if st.button('Convert'):
    if image_path is not None:
        converted_image_bytes = convert_image(image_path, new_format)
        st.markdown(get_image_download_link(converted_image_bytes, new_format), unsafe_allow_html=True)
    else:
        st.error("Please upload the image")

# Function to generate a download link for the image
