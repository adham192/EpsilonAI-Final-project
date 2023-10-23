import streamlit as st
def app():
    st.title('About (KSI) Toronto project')
    st.write('Inside is information for all traffic accidents reported between 2007 and 2017. There is data on the time, location, and the type of incident with various attributes about the traffic conditions at the time of the incident. the police wants to know:')
    st.write('  1- Does accidents increase over years.')
    st.write('  2- Does fatal accidents happens occasionally.')
    st.write('  3- Number of accidnets in each District.')
    st.write('  4- The driving condition that had the most accidents in last 10 years.')
    st.write('The above insights can help the police to decrease the number of accidents in the future.')
    st.write('Lets start our analysis.....')