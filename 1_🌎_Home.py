import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os
import uvicorn

textColor = "#090C25"
backgroundColor = '#DCDDF4'
primaryColor = '#282B7B'
secondaryBackgroundColor = '#3E43C1'
font="sans serif"

# Set page tab display
st.set_page_config(
   page_title="Simple Image Uploader",
   page_icon= ':marco_con_foto:',
   layout="wide",
   initial_sidebar_state="expanded"
)




#url = 'https://skin-cancer-detection-5fdu6rckpq-uc.a.run.app'
load_dotenv()
url = os.getenv('API_URL')
# App title and description


def cs_body():

    st.title('Image Recognition for diverse skin lesions and diseases 📸')

    colu1, colu2 = st.columns(2)

    with colu2:
        st.image('./Skin_front.png')
    with colu1:

        st.write('Welcome to our image predictor')
        st.markdown('''
            > This is a IA made from Convolutional Neural Networks for the identification of diverse skin lessions and diseases such as:
            > * Melanoma
            > * Melanocytic nevi
            > * Basal cell carcinoma
            > * Actinic keratoses and intraepithelial carcinoma / Bowen's disease
            > * Benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses
            > * Dermatofibroma
            > * Vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage)
            ''')
    st.markdown("---")
### Create a native Streamlit file upload input
    st.markdown("### Please drag the skin image here (Required to be taken from a Dermatoscope) 👇")
    img_file_buffer = st.file_uploader('Upload an image', type=['png','jpg'])

    if img_file_buffer is not None:
         col1, col2 = st.columns(2)

         with col1:
         ### Display the image user uploaded
            st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded 👆")
         with col2:
            with st.spinner("Wait for it..."):
         ### Get bytes from the file buffer
               img_bytes = img_file_buffer.getvalue()
         ### Make request to  API (stream=True to stream response as bytes)
            res = requests.post(url + "/upload_image", files={'img': img_bytes})
            if res.status_code == 200:
            ### Display the image returned by the API
               st.header(res.json())
            else:
               st.markdown("**Oops**, something went wrong 😓 Please try again.")
               print (res.status_code, res.content)

         return res.content

def main():
   cs_body()


if __name__ == '__main__':
    main()
