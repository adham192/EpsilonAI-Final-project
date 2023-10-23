import streamlit as st
import pandas as pd
def app():
    st.title('Killed or Seriously injured Toronto Dataset')
    st.markdown('<a href="https://www.kaggle.com/datasets/jrmistry/killed-or-seriously-injured-ksi-toronto-clean/data"> <center> Link to Dataset  </center> </a> ', unsafe_allow_html=True)
    df = pd.read_csv('KSI')
    df.drop('Unnamed: 0' , axis = 1 , inplace = True)
    st.dataframe(df)