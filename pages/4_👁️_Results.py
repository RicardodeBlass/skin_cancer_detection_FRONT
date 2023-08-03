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

st.write('''According to Nature science journal, the journal of the European Society for Medical Oncology and
         the Japanese Society of Medical Oncology, the accuracy of a diagnosis performed by inexperienced
         dermatologists and experts with dermatoscopic imaging alone ranges between **71.3%** and **75.7%**, respectively.
        While taking into account additional information from dermatology studies increases accuracy by 10%. This means that this type of tools could
        be useful to offer guidance to the doctors on what type of laboratory studies need to be performed and give an idea of
        the type of disease or lession that the patient may have, especially in doctors with little experience in the area,
        resulting in reduction of diagnosis times and costs in laboratory studies. ''')


st.subheader('Best Model Combination 🟢')
st.info('This model achieved an **accuracy of 78.43%, precision of 76.34%, and recall of 76.56%.**')

col1, col2 = st.columns(2)
with col1:
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

col2.image(Image.open('/mount/src/skin_cancer_detection_front/pages/model.jpeg'))


st.subheader('Next steps 🔜')

st.info('''
We would like to share this algorithm with hospitals and dermatological medical units to test its operation in real situations, while feeding the model with new dermatoscopic images to improve its prediction.
''')
