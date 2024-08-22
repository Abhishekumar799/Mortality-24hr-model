
import numpy as np
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
from PIL import Image

model = load_model('Model/lightgbm_Gosis_model')

cat_map = {
    "No": 0,
    "Yes": 1,
    "Not Available": np.nan,
    
    
}


def predict(model, input_df):
    #model.memory = "Data/"
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['prediction_label'][0]
    confidence = predictions_df['prediction_score'][0]
    return predictions, confidence


def get_data():
    # data = pd.read_csv("Data/peerj-08-10337-s001.csv")
    data = pd.read_csv("Data/gosis-1-24hr.csv")
    data.columns = list(map(str.strip, list(data.columns)))
    data = data[['age', 'height', 'hospital_los_days', 'icu_death', 'icu_los_days', 'weight', 'bun_apache', 'creatinine_apache', 'gcs_eyes_apache', 'glucose_apache', 'heart_rate_apache', 'hematocrit_apache', 'map_apache', 'resprate_apache', 'sodium_apache', 'temp_apache', 'urineoutput_apache', 'ventilated_apache', 'wbc_apache', 'd1_heartrate_max', 'd1_heartrate_min', 'd1_spo2_max', 'd1_spo2_min', 'd1_sysbp_max', 'd1_sysbp_min', 'h1_heartrate_max', 'h1_heartrate_min', 'h1_spo2_max', 'h1_spo2_min', 'h1_sysbp_max', 'h1_sysbp_min', 'd1_potassium_max', 'd1_potassium_min']]

    return data


def main():
    data = get_data()
    # image2 = Image.open('Images/icu.png')
    # st.sidebar.info('This app is created to predict a particular patient need ICU treatment or no. [DeepAarogya]] - Version 2')
    # st.sidebar.image(image2)
    st.title("ICU Mortality 24 hr")

    st.sidebar.title("Check Analysis:")

   

    if st.checkbox("Do you have patient age?", False):
        age = st.number_input('Age:', 
                          min_value=data.describe()["age"].loc["min"], 
                          max_value=data.describe()["age"].loc["max"], 
                          value=data.describe()["age"].loc["50%"])
    else:
        age = np.nan

    if st.checkbox("Do you have patient height?", False):
        height = st.number_input('Height:', 
                                min_value=data.describe()["height"].loc["min"], 
                                max_value=data.describe()["height"].loc["max"], 
                                value=data.describe()["height"].loc["50%"])
    else:
        height = np.nan

    if st.checkbox("Do you have patient hospital length of stay in hours?", False):
        hospital_los_hours = st.number_input('Hospital LOS Hours:', 
                                            min_value=24*(data.describe()["hospital_los_days"].loc["min"]), 
                                            max_value=24*(data.describe()["hospital_los_days"].loc["max"]), 
                                            value=24*(data.describe()["hospital_los_days"].loc["50%"]))
    else:
        hospital_los_hours = np.nan


    if st.checkbox("Do you have patient icu length of stay in hours?", False):
        icu_los_hours = st.number_input('ICU LOS Hours:', 
                                    min_value= 24*(data.describe()["icu_los_days"].loc["min"]), 
                                    max_value=24*(data.describe()["icu_los_days"].loc["max"]), 
                                    value=24*(data.describe()["icu_los_days"].loc["50%"]))
    else:
        icu_los_hours = np.nan


    if st.checkbox("Do you have patient weight?", False):
        weight = st.number_input('Weight:', 
                                min_value=data.describe()["weight"].loc["min"], 
                                max_value=data.describe()["weight"].loc["max"], 
                                value=data.describe()["weight"].loc["50%"])
    else:
        weight = np.nan

    if st.checkbox("Do you have patient bun_apache?", False):
        bun_apache = st.number_input('BUN APACHE:', 
                                    min_value=data.describe()["bun_apache"].loc["min"], 
                                    max_value=data.describe()["bun_apache"].loc["max"], 
                                    value=data.describe()["bun_apache"].loc["50%"])
    else:
        bun_apache = np.nan

    if st.checkbox("Do you have patient creatinine_apache?", False):
        creatinine_apache = st.number_input('Creatinine APACHE:', 
                                            min_value=data.describe()["creatinine_apache"].loc["min"], 
                                            max_value=data.describe()["creatinine_apache"].loc["max"], 
                                            value=data.describe()["creatinine_apache"].loc["50%"])
    else:
        creatinine_apache = np.nan

    if st.checkbox("Do you have patient gcs_eyes_apache?", False):
        gcs_eyes_apache = st.number_input('GCS Eyes APACHE:', 
                                        min_value=data.describe()["gcs_eyes_apache"].loc["min"], 
                                        max_value=data.describe()["gcs_eyes_apache"].loc["max"], 
                                        value=data.describe()["gcs_eyes_apache"].loc["50%"])
    else:
        gcs_eyes_apache = np.nan

    if st.checkbox("Do you have patient glucose_apache?", False):
        glucose_apache = st.number_input('Glucose APACHE:', 
                                        min_value=data.describe()["glucose_apache"].loc["min"], 
                                        max_value=data.describe()["glucose_apache"].loc["max"], 
                                        value=data.describe()["glucose_apache"].loc["50%"])
    else:
        glucose_apache = np.nan

    if st.checkbox("Do you have patient heart_rate_apache?", False):
        heart_rate_apache = st.number_input('Heart Rate APACHE:', 
                                            min_value=data.describe()["heart_rate_apache"].loc["min"], 
                                            max_value=data.describe()["heart_rate_apache"].loc["max"], 
                                            value=data.describe()["heart_rate_apache"].loc["50%"])
    else:
        heart_rate_apache = np.nan

    if st.checkbox("Do you have patient hematocrit_apache?", False):
        hematocrit_apache = st.number_input('Hematocrit APACHE:', 
                                            min_value=data.describe()["hematocrit_apache"].loc["min"], 
                                            max_value=data.describe()["hematocrit_apache"].loc["max"], 
                                            value=data.describe()["hematocrit_apache"].loc["50%"])
    else:
        hematocrit_apache = np.nan

    if st.checkbox("Do you have patient map_apache?", False):
        map_apache = st.number_input('MAP APACHE:', 
                                    min_value=data.describe()["map_apache"].loc["min"], 
                                    max_value=data.describe()["map_apache"].loc["max"], 
                                    value=data.describe()["map_apache"].loc["50%"])
    else:
        map_apache = np.nan

    if st.checkbox("Do you have patient resprate_apache?", False):
        resprate_apache = st.number_input('Respiratory Rate APACHE:', 
                                        min_value=data.describe()["resprate_apache"].loc["min"], 
                                        max_value=data.describe()["resprate_apache"].loc["max"], 
                                        value=data.describe()["resprate_apache"].loc["50%"])
    else:
        resprate_apache = np.nan

    if st.checkbox("Do you have patient sodium_apache?", False):
        sodium_apache = st.number_input('Sodium APACHE:', 
                                        min_value=data.describe()["sodium_apache"].loc["min"], 
                                        max_value=data.describe()["sodium_apache"].loc["max"], 
                                        value=data.describe()["sodium_apache"].loc["50%"])
    else:
        sodium_apache = np.nan

    if st.checkbox("Do you have patient temp_apache?", False):
        temp_apache = st.number_input('Temp APACHE:', 
                                    min_value=data.describe()["temp_apache"].loc["min"], 
                                    max_value=data.describe()["temp_apache"].loc["max"], 
                                    value=data.describe()["temp_apache"].loc["50%"])
    else:
        temp_apache = np.nan

    if st.checkbox("Do you have patient urineoutput_apache?", False):
        urineoutput_apache = st.number_input('Urine Output APACHE:', 
                                            min_value=data.describe()["urineoutput_apache"].loc["min"], 
                                            max_value=data.describe()["urineoutput_apache"].loc["max"], 
                                            value=data.describe()["urineoutput_apache"].loc["50%"])
    else:
        urineoutput_apache = np.nan

    if st.checkbox("Do you have patient ventilated_apache?", False):
        ventilated_apache = st.number_input('Ventilated APACHE:', 
                                            min_value=data.describe()["ventilated_apache"].loc["min"], 
                                            max_value=data.describe()["ventilated_apache"].loc["max"], 
                                            value=data.describe()["ventilated_apache"].loc["50%"])
    else:
        ventilated_apache = np.nan

    if st.checkbox("Do you have patient wbc_apache?", False):
        wbc_apache = st.number_input('WBC APACHE:', 
                                    min_value=data.describe()["wbc_apache"].loc["min"], 
                                    max_value=data.describe()["wbc_apache"].loc["max"], 
                                    value=data.describe()["wbc_apache"].loc["50%"])
    else:
        wbc_apache = np.nan

    if st.checkbox("Do you have patient d1_heartrate_max?", False):
        d1_heartrate_max = st.number_input('D1 Heartrate Max:', 
                                        min_value=data.describe()["d1_heartrate_max"].loc["min"], 
                                        max_value=data.describe()["d1_heartrate_max"].loc["max"], 
                                        value=data.describe()["d1_heartrate_max"].loc["50%"])
    else:
        d1_heartrate_max = np.nan

    if st.checkbox("Do you have patient d1_heartrate_min?", False):
        d1_heartrate_min = st.number_input('D1 Heartrate Min:', 
                                        min_value=data.describe()["d1_heartrate_min"].loc["min"], 
                                        max_value=data.describe()["d1_heartrate_min"].loc["max"], 
                                        value=data.describe()["d1_heartrate_min"].loc["50%"])
    else:
        d1_heartrate_min = np.nan

    if st.checkbox("Do you have patient d1_spo2_max?", False):
        d1_spo2_max = st.number_input('D1 SpO2 Max:', 
                                    min_value=data.describe()["d1_spo2_max"].loc["min"], 
                                    max_value=data.describe()["d1_spo2_max"].loc["max"], 
                                    value=data.describe()["d1_spo2_max"].loc["50%"])
    else:
        d1_spo2_max = np.nan

    if st.checkbox("Do you have patient d1_spo2_min?", False):
        d1_spo2_min = st.number_input('D1 SpO2 Min:', 
                                    min_value=data.describe()["d1_spo2_min"].loc["min"], 
                                    max_value=data.describe()["d1_spo2_min"].loc["max"], 
                                    value=data.describe()["d1_spo2_min"].loc["50%"])
    else:
        d1_spo2_min = np.nan

    if st.checkbox("Do you have patient d1_sysbp_max?", False):
        d1_sysbp_max = st.number_input('D1 SysBP Max:', 
                                    min_value=data.describe()["d1_sysbp_max"].loc["min"], 
                                    max_value=data.describe()["d1_sysbp_max"].loc["max"], 
                                    value=data.describe()["d1_sysbp_max"].loc["50%"])
    else:
        d1_sysbp_max = np.nan

    if st.checkbox("Do you have patient d1_sysbp_min?", False):
        d1_sysbp_min = st.number_input('D1 SysBP Min:', 
                                    min_value=data.describe()["d1_sysbp_min"].loc["min"], 
                                    max_value=data.describe()["d1_sysbp_min"].loc["max"], 
                                    value=data.describe()["d1_sysbp_min"].loc["50%"])
    else:
        d1_sysbp_min = np.nan

    if st.checkbox("Do you have patient h1_heartrate_max?", False):
        h1_heartrate_max = st.number_input('H1 Heartrate Max:', 
                                        min_value=data.describe()["h1_heartrate_max"].loc["min"], 
                                        max_value=data.describe()["h1_heartrate_max"].loc["max"], 
                                        value=data.describe()["h1_heartrate_max"].loc["50%"])
    else:
        h1_heartrate_max = np.nan

    if st.checkbox("Do you have patient h1_heartrate_min?", False):
        h1_heartrate_min = st.number_input('H1 Heartrate Min:', 
                                        min_value=data.describe()["h1_heartrate_min"].loc["min"], 
                                        max_value=data.describe()["h1_heartrate_min"].loc["max"], 
                                        value=data.describe()["h1_heartrate_min"].loc["50%"])
    else:
        h1_heartrate_min = np.nan

    if st.checkbox("Do you have patient h1_spo2_max?", False):
        h1_spo2_max = st.number_input('H1 SpO2 Max:', 
                                    min_value=data.describe()["h1_spo2_max"].loc["min"], 
                                    max_value=data.describe()["h1_spo2_max"].loc["max"], 
                                    value=data.describe()["h1_spo2_max"].loc["50%"])
    else:
        h1_spo2_max = np.nan

    if st.checkbox("Do you have patient h1_spo2_min?", False):
        h1_spo2_min = st.number_input('H1 SpO2 Min:', 
                                    min_value=data.describe()["h1_spo2_min"].loc["min"], 
                                    max_value=data.describe()["h1_spo2_min"].loc["max"], 
                                    value=data.describe()["h1_spo2_min"].loc["50%"])
    else:
        h1_spo2_min = np.nan

    if st.checkbox("Do you have patient h1_sysbp_max?", False):
        h1_sysbp_max = st.number_input('H1 SysBP Max:', 
                                    min_value=data.describe()["h1_sysbp_max"].loc["min"], 
                                    max_value=data.describe()["h1_sysbp_max"].loc["max"], 
                                    value=data.describe()["h1_sysbp_max"].loc["50%"])
    else:
        h1_sysbp_max = np.nan

    if st.checkbox("Do you have patient h1_sysbp_min?", False):
        h1_sysbp_min = st.number_input('H1 SysBP Min:', 
                                    min_value=data.describe()["h1_sysbp_min"].loc["min"], 
                                    max_value=data.describe()["h1_sysbp_min"].loc["max"], 
                                    value=data.describe()["h1_sysbp_min"].loc["50%"])
    else:
        h1_sysbp_min = np.nan

    if st.checkbox("Do you have patient d1_potassium_max?", False):
        d1_potassium_max = st.number_input('D1 Potassium Max:', 
                                        min_value=data.describe()["d1_potassium_max"].loc["min"], 
                                        max_value=data.describe()["d1_potassium_max"].loc["max"], 
                                        value=data.describe()["d1_potassium_max"].loc["50%"])
    else:
        d1_potassium_max = np.nan

    if st.checkbox("Do you have patient d1_potassium_min?", False):
        d1_potassium_min = st.number_input('D1 Potassium Min:', 
                                        min_value=data.describe()["d1_potassium_min"].loc["min"], 
                                        max_value=data.describe()["d1_potassium_min"].loc["max"], 
                                        value=data.describe()["d1_potassium_min"].loc["50%"])
    else:
        d1_potassium_min = np.nan

    


    output = ""

   
    input_dict = {
    'age': age,
    'height': height,
    'hospital_los_days': (hospital_los_hours)/24,
    'icu_los_days': (icu_los_hours)/24,
    'weight': weight,
    'bun_apache': bun_apache,
    'creatinine_apache': creatinine_apache,
    'gcs_eyes_apache': gcs_eyes_apache,
    'glucose_apache': glucose_apache,
    'heart_rate_apache': heart_rate_apache,
    'hematocrit_apache': hematocrit_apache,
    'map_apache': map_apache,
    'resprate_apache': resprate_apache,
    'sodium_apache': sodium_apache,
    'temp_apache': temp_apache,
    'urineoutput_apache': urineoutput_apache,
    'ventilated_apache': ventilated_apache,
    'wbc_apache': wbc_apache,
    'd1_heartrate_max': d1_heartrate_max,
    'd1_heartrate_min': d1_heartrate_min,
    'd1_spo2_max': d1_spo2_max,
    'd1_spo2_min': d1_spo2_min,
    'd1_sysbp_max': d1_sysbp_max,
    'd1_sysbp_min': d1_sysbp_min,
    'h1_heartrate_max': h1_heartrate_max,
    'h1_heartrate_min': h1_heartrate_min,
    'h1_spo2_max': h1_spo2_max,
    'h1_spo2_min': h1_spo2_min,
    'h1_sysbp_max': h1_sysbp_max,
    'h1_sysbp_min': h1_sysbp_min,
    'd1_potassium_max': d1_potassium_max,
    'd1_potassium_min': d1_potassium_min
    }

  # Printing the dictionary to verify



    
    input_df = pd.DataFrame([input_dict])
    if st.button("Predict"):
        output, confidence = predict(model=model, input_df=input_df)
        print(output)
        if output == 1:
            st.warning(f"Patient have high chance of mortality with {confidence*100}%" )
        else:
            st.success( f"Patient is fine!!!{confidence*100}% and icu hour {icu_los_hours} and icu_los_day {input_dict["icu_los_days"]}")


if __name__ == '__main__':
    main()


