import streamlit as st
from PIL import Image

def convert_image(image_path,new_format):
    with Image.open(image_path) as img:
        new_name = image_path.name.split('.')[0]+'.'+ new_format
        final_path =  'storage' + new_name
        img.save(final_path)
        st.success('image saved at ' + final_path)



st.title('Image converter')
image_path = st.file_uploader('enter your image',type=['png','jpeg','jpg'])
new_format = st.selectbox('select output format',['png','jpeg','jpg'])

if st.button('convert'):
    if image_path is not None:
        convert_image(image_path,new_format)
    else:
        st.error("plese,upload the image")

