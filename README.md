# skin_cancer_detection_FRONT
**Summary**

Using a dataset of 10,000 dermatoscopic images from Kaggle as the primary source of information, 
this model was design employing the TensorFlow and Keras libraries in Python and trained in Google Colab, 
also a transfer learning approach was used from TensorFlow - Keras pretrained models.

**Methodology 🧪**
**More than 100 experiments** were conducted for the final dense layers, considering various combinations of:

> Convolutional models: ResNet50, Xception, and Inception-ResNet-V2.

> Number of dense layers: 1-3

> Number of neurons and distribution in each layer: 250 to 5000, with pyramid, inverse pyramid, and linear orders.

> Optimizers: Adam, RMSPROP, Adagrad, and SGD.

> Learning rate: 0.1 - 0.0001

> Batch size: 32 - 264

> Pooling: Average - Max

> Epochs: 100 - 200

> EarlyStopping: 80 - 150

> Regularizers: L1, L2 & L1/L2 (0.5 - 0.00005)

> A dropout layer of 20% was applied to each Dense Layer.

The model's performance was also compared with Data Augmentation and SMOTE using Confusion Matrix.

Subsequently, Docker and Google Cloud Run were used to deploy the model in the cloud, and the API was designed and uploaded to Streamlit. 
All these components are now stored in GitHub repositories.

To use the API, you only need to upload a skin image taken from a dermatoscope, and it will automatically provide the corresponding result.
https://skincancerdetectionfront-obdqg2vvjgfcvwpchhxdqm.streamlit.app/
