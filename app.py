
import streamlit as st
import pandas as pd
import pickle

# Load models and data
model = pickle.load(open('kmeans_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title('🧠 Financial Behavior Cluster Predictor')

st.header('Enter Your Finance Info:')
total_spent = st.number_input('Total Spent Last Month ($)', min_value=0)
avg_transaction = st.number_input('Average Transaction Amount ($)', min_value=0)
transaction_count = st.number_input('Number of Transactions', min_value=0)
rent_pct = st.slider('Rent Spend %', 0.0, 1.0)
grocery_pct = st.slider('Grocery Spend %', 0.0, 1.0)
entertainment_pct = st.slider('Entertainment Spend %', 0.0, 1.0)

# Prediction
if st.button('Predict My Cluster'):
    X = scaler.transform([[total_spent, avg_transaction, transaction_count, rent_pct, grocery_pct, entertainment_pct]])
    cluster = model.predict(X)
    st.success(f'You belong to Cluster {cluster[0]}!')
