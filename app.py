import streamlit as st
import pandas as pd
import joblib

# Title
st.header("Модель для предсказания силы тока I (mA)")

# Input bar 1
additive = st.number_input("Введите легирующую добавку, %")

# Input bar 2
mass = st.number_input("Введите массу")

# If button is pressed
if st.button("Предсказать"):
    
    # Unpickle regressor
    reg = joblib.load("model_cb.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[additive, mass]], 
                       columns = ["Легирующая добавка, %", "М "])
    
    # Get prediction
    prediction = reg.predict(X)
    
    # Output prediction
    st.text(f"Требуемая сила тока (I, mA) = {prediction} mA")
    