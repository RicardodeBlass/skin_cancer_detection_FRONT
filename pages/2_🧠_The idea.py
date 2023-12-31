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

st.title('The idea 🧠')

col1, col2 =st.columns(2)

st.write('')


with col1:
    st.markdown('''

The purpose of this project is to classify skin images obtained through dermatoscopy into seven different lesions or diseases,
thereby **_reducing diagnosis time and medical costs_**.

The seven classifications are the following:

>1. Actinic keratoses and intraepithelial carcinoma / Bowen's disease (AKIEC)
>2. Basal cell carcinoma (BCC)
>3. Benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, BKL)
>4. Dermatofibroma (DF)
>5. Melanoma (MEL)
>6. Melanocytic nevi (NV)
>7. Vascular lesions (angiomas, angiokeratomas, pyogenic granulomas, and hemorrhage, VASC)

''')
    st.markdown("---")

col2.image(Image.open('/mount/src/skin_cancer_detection_front/pages/dataset-cover.png'))

c1, c2 = st.columns(2)

st.title('How it works? 👩‍⚕️')

st.markdown('''
Normal dermatological analysis can take approximately **one month**, this period can play a critical role for early detection of the disease in order to increase the chances of a successful treatment.
In average the cost of the entire process is around **$1,000** when a correct diagnosis is made.''')

with c1:

    st.markdown('''The process to make a correct diagnosis is as follows:

>1. Initial clinical evaluation: The first consultation with a general physician who evaluates the suspicious
lesion and possible causes.
>
>2. Specialist evaluation: Consultation with a dermatologist, where the patient's medical history is reviewed,
a physical examination of the skin is performed, and the appearance of the lesion is assessed.
>
>3. Dermatoscopy: A device called  Dermatoscope is used to thoroughly examine the lesion.
>
>4. Biopsy: If the lesion appears suspicious, a skin sample is taken for laboratory analysis.
>
>5. Pathological analysis: A pathologist examines the cells to detect any suspicious characteristics, mainly
related to cancer.
>
>6. Oncology consultation: If the diagnosis is unclear or further studies are needed, the patient is referred
to a specialist in dermatological oncology, who conducts additional laboratory studies to gather more information.
>
>7. Evaluation of results: The dermatologist reviews all the information and studies to get a correct
diagnosis and initiate treatment.'''
)

c2.image(Image.open('/mount/src/skin_cancer_detection_front/pages/Dermatoscopio.jpeg'))

st.info('''
This project was created with the purpose of supporting the medical community, saving time on the diagnosis process and reducing the associated costs
for the patients.
We aimed to support decision-making in steps 4, 5, and 6 to reduce the number of laboratory analysis or specialist consultations.''')
