import streamlit as st
def app():
    # Page content
    st.markdown(' <center> <h1> Killed or Seriously injured (KSI) Toronto analysis </h1> </font> </center> </h1> ', 
            unsafe_allow_html = True)
    st.markdown(''' <center> <h6>This app is created to analyze the data of Toronto accidents </center> </h6> ''' , unsafe_allow_html = True)

    # the path of a photo provided from the path of this file
    st.image('./MAC14_TORONTO_TRAFFIC_POST.jpg')