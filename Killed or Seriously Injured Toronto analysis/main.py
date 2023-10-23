import streamlit as st
from streamlit_option_menu import option_menu
import Analysis , Data , About , Home , prediction

st.set_page_config(
        page_title="Killed or Seriously injured Toronto project",
)




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title = 'Menu',
                options=['Home','About','Analysis','Data' , 'prediction'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"}}
                
                )

        
        if app == "Home":
            Home.app()
        if app == "About":
            About.app()    
        if app == "Analysis":
            Analysis.app()        
        if app == 'Data':
            Data.app()
        if app == 'prediction':
            prediction.main() 
             
    run()