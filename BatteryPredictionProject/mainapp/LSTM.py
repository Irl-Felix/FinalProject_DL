from keras.models import load_model
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "LSTM_Model.h5")


newmodel = load_model(file_path)


#loading the model for prediction
def prediction(values):
    SOH_Values = newmodel.predict(sc.fit_transform(values)).flatten().tolist()
    rounded_SOH = np.round(SOH_Values, 2).tolist()
    return rounded_SOH[0]

