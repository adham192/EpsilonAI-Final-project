
import streamlit as st
import pandas as pd
import joblib


Inputs = joblib.load(filename = "Inputs.pkl")
Model = joblib.load(filename = "Model.pkl")
    

def prediction(District , VISIBILITY , LIGHT , INJURY , PEDESTRIAN , CYCLIST , AUTOMOBILE , TRUCK , MOTORCYCLE , TRSN_CITY_VEH , EMERG_VEH , PASSENGER , SPEEDING , AG_DRIV , REDLIGHT , ALCOHOL , DISABILITY):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0 , 'District'] = District
    test_df.at[0 , 'VISIBILITY'] = VISIBILITY
    test_df.at[0 , 'LIGHT'] = LIGHT
    test_df.at[0 , 'INJURY'] = INJURY
    test_df.at[0 , 'PEDESTRIAN'] = PEDESTRIAN
    test_df.at[0 , 'CYCLIST'] = CYCLIST
    test_df.at[0 , 'AUTOMOBILE'] = AUTOMOBILE
    test_df.at[0 , 'TRUCK'] = TRUCK
    test_df.at[0 , 'MOTORCYCLE'] = MOTORCYCLE
    test_df.at[0 , 'TRSN_CITY_VEH'] = TRSN_CITY_VEH
    test_df.at[0 , 'EMERG_VEH'] = EMERG_VEH
    test_df.at[0 , 'PASSENGER']  = PASSENGER
    test_df.at[0 , 'SPEEDING'] = SPEEDING
    test_df.at[0 , 'AG_DRIV'] = AG_DRIV
    test_df.at[0 , 'REDLIGHT'] = REDLIGHT
    test_df.at[0 , 'ALCOHOL'] = ALCOHOL
    test_df.at[0 , 'DISABILITY'] = DISABILITY
    result = Model.predict(test_df)[0]
    return result

def main():
    st.title('Fatal Accident prediction')
    District = st.selectbox("District" , ['Toronto East York', 'Scarborough', 'Etobicoke York', 'North York'])
    VISIBILITY = st.selectbox("Visibility" , ['Clear', 'Rain', 'Freezing Rain', 'Snow','Fog, Mist, Smoke, Dust' , 'Drifting Snow', 'Strong wind'])
    LIGHT = st.selectbox("Light" , ['Dark', 'Dark, artificial', 'Dusk, artificial', 'Daylight',
       'Daylight, artificial', 'Dusk', 'Dawn, artificial' , 'Dawn'])
    INJURY = st.selectbox("Injury" ,  ['Minimal', 'Fatal', 'Major', 'Minor'])
    PEDESTRIAN = st.slider('Is there any pedestrians involved?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    CYCLIST = st.slider('Is there any cyclists involved?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    AUTOMOBILE = st.slider('AutoMobile' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    TRUCK =  st.slider('Truck' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    MOTORCYCLE =  st.slider('Motorcycle' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    TRSN_CITY_VEH = st.slider('Is the there any Transition city vehicles?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    EMERG_VEH =  st.slider('Emergency vehicle' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    PASSENGER = st.slider('Were there any passengers with the driver?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    SPEEDING =  st.slider('Speeding?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    AG_DRIV =  st.slider('Agressive Driving?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    REDLIGHT =  st.slider('Ran a redlight?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    ALCOHOL =  st.slider('Drunk?' , min_value = 0 , max_value = 1 , value = 0 , step = 1)
    DISABILITY = st.slider('Disability' , min_value = 0 , max_value = 1 , value = 0 , step = 1)

    if st.button("predict"):
        result = prediction(District , VISIBILITY , LIGHT , INJURY , PEDESTRIAN , CYCLIST , AUTOMOBILE , TRUCK , MOTORCYCLE , TRSN_CITY_VEH , EMERG_VEH , PASSENGER , SPEEDING , AG_DRIV , REDLIGHT , ALCOHOL , DISABILITY)
        st.text(f'The Accident is (0) = non-fatal , (1) = Fatal : {result}')
