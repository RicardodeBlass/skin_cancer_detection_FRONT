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
   page_title="The idea 🧠",
   page_icon= ':marco_con_foto:',
   layout="wide",
   initial_sidebar_state="expanded")

st.title('Results 👁️')

st.write('''According to Nature and the journal of the European Society for Medical Oncology and
         the Japanese Society of Medical Oncology, the accuracy of a correct diagnosis by inexperienced
         dermatologists and experts with dermatoscopic imaging alone was on average **71.3%** and **75.7%**, respectively.
        While with additional information from studies increased accuracy by 10%. This means that this type of tools can
        be useful to help guide the doctor on what type of laboratory studies needs to be performed and give an idea of
        the type of disease or lession that the patient may have, especially in doctors with little experience in the area,
        thus reducing the time of diagnosis and costs in laboratory studies. ''')


st.subheader('Best Model Combination 🟢')
st.info('This model achieved an **accuracy of 78.43%, precision of 76.34%, and recall of 76.56%.**')
st.markdown('''The selected model at the end of the experiments was as follows:
> - CNN Model: Inception-Resnet-V2
> - Optimizer: RMSPROP
> - Learning rate: 0.0001
> - Number of dense layers: 3
> - Number of neurons in dense layer 1: 5000
> - Number of neurons in dense layer 2: 5000
> - Number of neurons in dense layer 3: 2000
> - Image Size: 128x128
> - Batch Size: 256
> - Pooling: Max
> - Epochs: 100
> - Early Stopping: 80
> - Regularizers (l2) - Ridge: 0.05
            ''')



st.subheader('Next steps 🔜')

st.info('''
We would like to share this algorithm with hospitals and dermatological medical units to test its operation in real situations, while feeding the model with new dermatoscopic images to improve its prediction.
''')
