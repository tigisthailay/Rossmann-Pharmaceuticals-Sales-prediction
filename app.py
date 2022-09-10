# Importing necessary packages
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import pickle
import math
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Dashboard | Rossmann Pharmaceuticals Sales prediction ", layout="wide")
st.markdown("<h1 style='color:#0b4eab;font-size:36px;border-radius:10px;'>Pharmaceutical Sales Prediction Model </h1>", unsafe_allow_html=True)

# loading the trained model
pickle_in = open('C:/Users/user/Desktop/10Academy/Rossmann-Pharmaceuticals-Sales-prediction/models/linearregression-2022-09-09-10-21-22.pkl', 'rb') 
calculator = pickle.load(pickle_in)
 
@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Store, dayofweek, Open, Promo,  SchoolHoliday, Day, weekofyear,Month, Year, StoreType,
              Assortment,CompetitionDistance, Promo2):   
 
    # Pre-processing user input    
    if Promo == 1:
        Promo = 1
    else:
        Promo = 0

    if StoreType == "a":
        StoreType = 1
    elif StoreType == "b":
        StoreType = 2
    elif StoreType == "c":
        StoreType = 3
    else:
        StoreType = 4

    if Assortment == "a":
        Assortment = 0
    elif Assortment == "b":
        Assortment = 1
    else:
        Assortment = 2
 
    if Promo2 == 1:
        Promo2 = 1
    else:
        Promo2 = 0 
    

    # Making predictions 
    prediction = calculator.predict( 
        [[Store, dayofweek, Open, Promo,  SchoolHoliday, Day, weekofyear,Month, Year, StoreType,
              Assortment,CompetitionDistance, Promo2]])
     
    return prediction*5773.8
  
def main():       
   
    html_temp = """ 
    
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    form = st.form(key="my-form")
    c1, c2 = st.columns(2)
    with c1:
        Store = st.number_input('Enter Store number/Id')
        StoreType = st.selectbox('Select StoreType',("a","b","c","d")) 
        DayOfWeek = st.number_input('Enter DayOfWeek')
        Promo = st.selectbox('Are you in Promo',(1,0))
        #StateHoliday = st.selectbox('Is it StateHoliday',("a","b","c"))  
        SchoolHoliday = st.selectbox('Is it SchoolHoliday',(1,0)) 
        Year = st.number_input('Enter Year')
    with c2:
        Month = st.number_input('Enter Month')
        Day = st.number_input('Enter Day')
        WeekOfYear = st.number_input('Enter WeekOfYear')
        Assortment = st.selectbox('Choose Assortment',("a","b","c")) 
        CompetitionDistance = st.number_input('Enter Competition distanc')

        Promo2 = st.selectbox('Are you in Promo2',(1,0))
    
    result =""
    Open = 1
    
  
    if st.button("Predict"): 
        result = prediction(Store, DayOfWeek, Open, Promo, SchoolHoliday, Day, WeekOfYear, Month, Year, StoreType,
              Assortment,CompetitionDistance, Promo2) 
        st.success('Your Sales is {}'.format(result))

     
if __name__=='__main__': 
    main()