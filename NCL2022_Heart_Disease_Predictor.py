# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 03:14:48 2022

@author: Raj Kiran
"""
import streamlit as sl
import joblib

def add_bg_from_url():
    sl.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://th.bing.com/th/id/R.c7323d22054856f490a89e7ff5976846?rik=F0CQa7rowRTOWA&riu=http%3a%2f%2fanalyticsinsight.b-cdn.net%2fwp-content%2fuploads%2f2020%2f10%2fMachine-Learning-2-1024x512.jpg&ehk=l7OO6%2bq8WtSJKROM7vLYQyXi%2bYLahhwymCDPq7VR2oI%3d&risl=&pid=ImgRaw&r=0");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def main():
    html_template = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;font-family: monospace";text-align:center> Newcastle University(2022)- Heart Disease Predictor</h2>
    </div>
    """


    sl.markdown("""
    <style>
    div.stSlider{
        font-family:Lucida Console;
    
        font-weight: bold;
        
        }
    div.stSelectbox{
        font-family:Lucida Console;
        
        font-weight: bold;
        
        }
    div.stNumberInput{
        font-family:Lucida Console;
        
        font-weight: bold;
        
        }
    
        div.stButton > button:first-child {
        background-color: black;
        
        
        }
        div.stButton  {
        font-size:30px;
        font-family:sans-serif;
        }
        .st-f6 {
    color: rgb(248 249 251);
}
        .st-fh {
    color: rgb(248 249 251);
}
        div.stButton > button:hover {
    background-color: black;
    color:#ff0000;
    
    }
        .css-znku1x {
    font-family: monospace;
    
}
        .st-dq {
    color: #fff173;
}
        p, ol, ul, dl {
    font-size: 3rem;
    font-weight: initial;
}
        .css-15tx938 {
    font-size: 30px;
    color: rgb(233 232 132);
    
    }
   .st-ag {
    font-weight: bold;
}
   .st-af {
    font-size: 1.3rem;
} 
   .css-1inwz65 {
    
    font-size: 20px;
    
}
   .css-10y5sf6 {
    font-size: 16px;
    font-weight: bold;
}
   .css-fg4pbf {
    
    color: rgb(248 249 251);
    
}
   .css-1r8izn3 {
    margin: -3px;
    height: 117%;
    }
    </style>""", unsafe_allow_html=True)
    sl.markdown(html_template, unsafe_allow_html=True)
    
    model = joblib.load('NCL2022_Heart_Disease_Predictor')
    
        
    v1 = sl.slider('Enter your age',18,100)
    s1=sl.selectbox("Sex Enter your age",("Male","Female"))
    if s1=="Male":
        v2=1
    else:
        v2=0

    s2=sl.selectbox("Chest Pain",("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic"))
    if s2=="Typical angina":
        v3=0
    elif s2=="Atypical angina":
        v3=1 
    elif s2=="Non-anginal pain":
        v3=2
    else :
        v3=3
    v4 = sl.slider('Resting Blood Pressure (in mm Hg on admission to the hospital)',100,200)
    v5 =sl.number_input("Enter Your Serum Cholestoral in mg/dl",min_value=100)
    s3 =sl.number_input("Fasting blood sugar in mg/dl",min_value=20)
    if s3>120:
        v6=1
    else:
        v6=0
    s4 = sl.selectbox('Resting Electrocardiographic Results',('Normal','Having ST-T wave abnormality','left ventricular hyperthrophy'))
    if s4=="Normal":
        v7=0
    elif s4=="Having ST-T wave abnormality":
        v7=1
    else :
        v7=2
    v8 =sl.number_input("Maximum Heart Rate Achieved",min_value=100,max_value=200)
    s5=sl.selectbox("Exercise Induced Angina ",("Yes","No"))
    if s5=="Yes":
        v9=1
    else:
        v9=0
    v10 =sl.number_input("ST depression induced by exercise relative to rest",max_value=10.0)
    s6 = sl.selectbox('Slope of the peak exercise ST segment',('Upsloping','Flat','Downsloping'))
    if s6=="Upsloping":
        v11=0
    elif s6=="Flat":
        v11=1
    else :
        v11=2
    v12 = sl.slider('Number of major vessels coloured by fluoroscopy',0,4)
    s7 = sl.selectbox('Thalassemia',('Normal', 'Fixed defect', 'Reversable defect'))
    if s7=="Normal":
        v13=1
    elif s7=="Fixed defect":
        v13=2
    else :
        v13=3
    
    if sl.button('Predict'):
        prediction = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]])
        sl.balloons()
        if prediction[0]==0:
            sl.success('No Heart Disease ') 
        else:
            sl.success('Possible Heart Disease ')     
    
    

if __name__ == '__main__':
    main()