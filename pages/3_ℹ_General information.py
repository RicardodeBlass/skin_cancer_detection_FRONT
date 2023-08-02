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
   page_title="General information ℹ️",
   page_icon= ':marco_con_foto:',
   layout="wide",
   initial_sidebar_state="expanded")

st.title('General information ℹ️')


st.subheader('Summary')
st.markdown('''
Using a dataset of 10,000 dermatoscopic images from Kaggle as the primary source of information, this model was
design employing the TensorFlow and Keras libraries in Python and trained in Google Colab, also a transfer learning
approach was used with Inception-ResNet-V2 convolutional neural network.
''')
st.markdown("---")

co1,co2,co3,co4,co5,co6,co7,co8,co9 =st.columns(9)

co1.image(Image.open('/mount/src/skin_cancer_detection_front/pages/Kaggle.png'))
co2.image(Image.open('/mount/src/skin_cancer_detection_front/pages/phyton.png'))
co3.image(Image.open('/mount/src/skin_cancer_detection_front/pages/co.png'))
co4.image(Image.open('/mount/src/skin_cancer_detection_front/pages/TF.png'))
co5.image(Image.open('/mount/src/skin_cancer_detection_front/pages/keras.png'))
co6.image(Image.open('/mount/src/skin_cancer_detection_front/pages/docker.png'))
co7.image(Image.open('/mount/src/skin_cancer_detection_front/pages/Google-Cloud-Run.png'))
co8.image(Image.open('/mount/src/skin_cancer_detection_front/pages/github.png'))
co9.image(Image.open('/mount/src/skin_cancer_detection_front/pages/Streamlit.png'))



c1,c2 = st.columns(2)
with c1:
    st.subheader('Methodology 🧪')
    st.markdown('''More than 100 experiments were conducted for the final dense layers, considering various combinations of:

> - Convolutional models: ResNet50, Xception, and Inception-ResNet-V2.
> - Number of dense layers: 1-3
> - Number of neurons and distribution in each layer: 250 to 5000, with pyramid, inverse pyramid, and linear orders.
> - Optimizers: Adam, RMSPROP, Adagrad, and SGD.
> - Learning rate: 0.1 - 0.0001
> - Batch size: 32 - 264
> - Pooling: Average - Max
> - Epochs: 100 - 200
> - EarlyStopping: 80 - 150
> - Regularizers: L1, L2 & L1/L2 (0.5 - 0.00005)
> - A dropout layer of 20% was applied to each Dense Layer.
''')

st.write("The model's performance was also compared with Data Augmentation and SMOTE using Confusion Matrix.")

with c2:
    st.subheader("**Confussion Matrix SMOTE 📶**")
    st.image('/mount/src/skin_cancer_detection_front/pages/Matrix_Conf.png')

st.write('''Subsequently, Docker and Google Cloud Run were used to deploy the model in the cloud, and the API was designed and uploaded to Streamlit.
         All these components are now stored in GitHub repositories.''')

st.info('''To use the API, you only need to upload a skin image taken from a dermatoscope, and it will automatically provide the corresponding result.
''')
