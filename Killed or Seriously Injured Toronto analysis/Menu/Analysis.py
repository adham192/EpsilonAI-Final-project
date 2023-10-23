# import needed libraries
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

def app():
    df = pd.read_csv('KSI')



    NUM_ACC = df.groupby(['YEAR'])['ACCNUM'].nunique()
    fig1 = px.bar(data_frame = NUM_ACC , title = 'Accidents caused in different years' 
        , labels = {'value' : 'Number of Accidents (ACCNUM)'} , color_discrete_sequence = ['red'] , text_auto = True)



    fig2 = px.histogram(data_frame = df , x = df['YEAR'] , color = df['FATAL'] , barmode = 'group' , text_auto = True)




    fig3 = px.bar(data_frame = df['District'].value_counts() , labels = {'value' : 'Number of accidents'} 
        , title = 'Number of accidents in each District' , color_discrete_sequence = ['pink'] , text_auto = True)



    fatality = df[ df['INJURY'] == 'Fatal' ]
    fatality = fatality.groupby(df['YEAR']).count()
    fig4 = px.bar(data_frame = fatality['INJURY'] , labels = {'value' : 'Number of Injury = Fatal'} 
        , title = 'Fatal Injuries over years' , color_discrete_sequence = ['purple'] , text_auto = True)




    Cause_Fatal = df.pivot_table(index='YEAR', margins=False 
                                ,values=['ALCOHOL', 'AG_DRIV', 'SPEEDING','REDLIGHT','DISABILITY'] , aggfunc=np.sum)
    fig5 = px.line(Cause_Fatal , title = 'Fatal Causes for accidents' , labels = {'value' : 'Fatal Accidents'})




    KSI_df = df.pivot_table(index = 'YEAR' , values = ['FATAL','DISABILITY'] , aggfunc = np.sum , margins = True 
                            , margins_name = 'Total Under Category')
    KSI_df.drop(['Total Under Category'] , axis = 0 , inplace = True)
    fig6 = px.bar(data_frame = KSI_df , barmode = 'group' , text_auto = True , labels = {'value' : 'Number of accidents'} 
        , title = 'Fatal and Disability accidents in different years')



    KSI_cause = df.pivot_table(index = 'YEAR' , values = ['AG_DRIV' , 'ALCOHOL' , 'REDLIGHT' , 'SPEEDING'] 
                            , aggfunc = np.sum , margins = True , margins_name = 'Total Under Category')
    fig7 = px.pie(data_frame = KSI_cause , values = KSI_cause.iloc[11] , names = ['AG_DRIV' , 'ALCOHOL' , 'REDLIGHT' , 'SPEEDING'])
    KSI_cause.drop('Total Under Category' , axis = 0 , inplace = True)




    KSI_Types = df.pivot_table(index = 'YEAR' , values = ['AUTOMOBILE', 'MOTORCYCLE', 'TRUCK', 'TRSN_CITY_VEH', 'EMERG_VEH']
                            , aggfunc = np.sum , margins = True , margins_name = 'Total Under Category')

    fig8 = px.pie(data_frame = KSI_Types , values = KSI_Types.iloc[11] , names = ['AUTOMOBILE', 'MOTORCYCLE', 'TRUCK', 'TRSN_CITY_VEH', 'EMERG_VEH'])
    KSI_Types.drop('Total Under Category', axis=0, inplace=True)




    KSI_victims = df.pivot_table(index = 'YEAR' , values = ['CYCLIST','PEDESTRIAN','PASSENGER'] ,
                                aggfunc = np.sum , margins = True , margins_name = 'Total Under Category')

    fig9 = px.pie(data_frame = KSI_victims , values = KSI_victims.iloc[11] , names = ['CYCLIST','PEDESTRIAN','PASSENGER'])
    KSI_victims.drop(['Total Under Category'] , axis = 0 , inplace = True)



    # Dividing our analysis into tabs , each tab contain different information

    tab_overall_vision , tab_districts , tab_fatal_injuries, tab_condition_involved , tab_conclusion = st.tabs(['Overall Vision' , 'Districts accidents' , 'Fatal Injuries causes' , 'Driving condition and victims involved' , 'Conclusion'])

    # Overall Vision tab

    with tab_overall_vision:
        # Title of the tab
        st.title('Some statistics over Time period (2007 - 2017)')
        # insights in this tab
        st.write('The information in this tab can answer the following questions:')
        st.write('  1- Does accidents decrease over years?')
        st.write('  2- Did non-fatal accidents decrease over years?')
        # first section
        st.header('Does accidents decrease over years?')
        st.write('From the graph we can see that total number of accidents has decreased slightly over years')
        st.plotly_chart(fig1)
        # second section 
        st.header('Did non-fatal accidents decrease over years?')
        st.plotly_chart(fig2)
        st.write('  1- From 2007 to 2017, the numbers of non-fatal accident declined while those occurance of fatal accident kept unchanged.')

    # Districts accidents tab

    with tab_districts:
        # Title of the tab
        st.title('Total number of accidents in each District.')
        # Insights in this tab
        st.write('The information we can gain from this tab is:')
        st.write(' The district that has the highest number of accidents.')
        # first section
        st.header('Which district has the most accidents?')
        st.write('The District Toronto East York has the most number of accidents.')
        st.plotly_chart(fig3)
        
    # Fatal injuries causes tab

    with tab_fatal_injuries:
        #Title of the tab
        st.title('Fatal injuries and causes')
        # insights in this tab
        st.write('The information we can gain from this tab is:')
        st.write('  1- Which year had the most fatal accidents?')
        st.write('  2- Fatal causes for accidents.')
        st.write('  3- Fatal and Disability accidents in different years.')
        # first section
        st.header('Which year had the most fatal accidents?')
        st.write('Fatal accidents was the highest in 2016.')
        st.plotly_chart(fig4)
        # second section
        st.header('Fatal causes for accidents.')
        st.write('Driving condition vs Fatal accidents over years.')
        st.plotly_chart(fig5)
        # third section
        st.header('Fatal and Disability accidents in different years.')
        st.plotly_chart(fig6)

    # tab_condition_involved

    with tab_condition_involved:
        #Title of the tab
        st.title('Driving condition that caused the accident and Victims involved in the accident')
        #insights in this tab
        st.write('The information we can gain from this tab is:')
        st.write('  1- The highest Driving condition that caused the accident.')
        st.write('  2- The highest vehicle type that caused the accident.')
        st.write('  3- The most victim involved in accidents.')
        #first section
        st.header('The highest Driving condition that caused the accident.')
        st.write('Aggressive driving has the highest number of accidents.')
        st.plotly_chart(fig7)
        #second section
        st.header('The highest vehicle type that caused the accident.')
        st.write('AutoMobile has the highest number of accidents.')
        st.plotly_chart(fig8)
        #third section
        st.header('The most victim involved in accidents.')
        st.write('Pedestrians are the most victims involved in accidents.')
        st.plotly_chart(fig9)
        
    # tab_conclusion
    with tab_conclusion:
        # Title of the Tab
        st.title('What we see through this analysis?')
        # conclusion
        st.write('We can see the following results:')
        st.write('  1- Fatal accidents decreases over years.')
        st.write('  2- The District Toronto East York has the most accidents, we must take a decision that decreases the number of accidents.')
        st.write('  3- Most drivers drives aggressively that causes alot of fatal accidents,So we should make a strict rule on driving aggressively.')
        st.write('  4- Among all vehicle types AutoMobile have the most number of accidents.')
        st.write('  5- Pedestrians are the most victims involved in accidents.')
