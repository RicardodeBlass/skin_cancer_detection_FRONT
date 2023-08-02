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


st.title('**The team 🌟**')

co1,co2,co3=st.columns(3)
with co1:
    st.write('Ricardo de Blass')
    st.info('**GitHub: [@RicardodeBlass](https://github.com/RicardodeBlass)**', icon="💻")

with co2:
    st.write('Desseyra Camaño',)
    st.info('**GitHub: [@Desseyra](https://github.com/Desseyra)**', icon="💻")

with co3:
    st.write('Leonardo Michel')
    st.info('**GitHub: [@LeonMichel96](https://github.com/LeonMichel96)**', icon="💻")


st.subheader('References')
st.info('**Data: [Kaggle](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)**', icon="🤖")

st.markdown('''
>-Tschandl, P., Rinner, C., Apalla, Z. et al. Human-computer collaboration for skin cancer recognition. Nat Med (2020). (https://doi.org/10.1038/s41591-020-0942-0)
>
>-Haenssle, H. A. et al. Man against machine: diagnostic performance of a deep learning convolutional neural network for dermoscopic melanoma recognition in comparison to 58 dermatologists. Ann. Oncol. 29, 1836–1842 (2018)
''')
