import streamlit as st
import seaborn as sns


header= st.container()
data= st.container()
features= st.container()
ml_model=st.container()

with header:
    st.title("kashti ki app")
    st.text("we talk about the kashti data set")

with data:
    st.title("kashti ki data")
    st.text("we talk about the kashti data set ki details")
    #load the data
    df= sns.load_dataset("titanic")
    st.write(df.head(10))
    st.subheader("kitny admi ty")
    st.bar_chart(df['sex'].value_counts())
    #others plots
    st.subheader("class ki hisab sy farq")
    st.bar_chart(df['class'].value_counts())

    st.bar_chart(df['age'].sample(10))

with features:
    st.title("kashti k data k features")
    st.text("we talk about the kashti data features")
    st.markdown('1. **Feature 1:**  tell the app features')
    st.markdown('2. **Feature 2:**  tell the app features')

with ml_model:
    st.title("kashti ka kia bna")
    st.text("we talk about the kashti data  ka kia bhti data  ka kia bna  ")  
    #making columns
    input,disply=st.columns(2)
    max_depth= input.slider("How many people do you know?",min_value=20,max_value=100,value=20,step=5)
    #n estimator
    n_estimator=input.selectbox("How many shoulb be there in RF?",options=[20,30,40,50,100,'no_limit'])
    #input features
    input_featurs= input.text_input("which featurs we should use")