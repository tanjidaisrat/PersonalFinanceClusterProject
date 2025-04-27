
# Decision Patterns: Analyzing Personal Finance Decisions Through Behavioral Clustering

This project analyzes personal finance transactions to uncover hidden behavioral patterns among users. By clustering users based on their spending behavior, we can identify distinct financial habits that can help improve personal finance management.

### Key Technologies:
- **Data Cleaning & Feature Engineering**: Using `Pandas` and `Numpy` to preprocess and engineer features from raw transaction data.
- **Unsupervised Learning**: Implemented **KMeans clustering** to categorize users based on their spending habits.
- **Data Visualization**: Leveraged **Matplotlib** and **Seaborn** to create compelling visualizations for better understanding of clusters.
- **Streamlit App**: Built an optional interactive web app for users to predict their cluster based on input financial data.

---

## Folder Structure

```plaintext
finance_behavior_clustering/
│
├── data/
│   └── transactions.csv   # (dataset)
│
├── notebooks/
│   └── finance_clustering.ipynb  # (main analysis notebook)
│
├── app/
│   └── app.py  # (optional Streamlit app)
│
├── README.md
│
├── requirements.txt
│
└── visuals/
    └── cluster_plot.png
    └── spending_patterns.png

/data: Contains the transaction dataset used for clustering analysis.


/notebooks: Contains the Jupyter notebook with the main analysis and clustering steps.


/app: Optional folder for the Streamlit web app to predict clusters based on user input.


/visuals: Folder for storing visual outputs such as clustering plots and spending patterns.



Requirements
Install the required libraries by using the requirements.txt file:
pip install -r requirements.txt

The requirements.txt includes the following libraries:
pandas


numpy


scikit-learn


matplotlib


seaborn


plotly


streamlit



Dataset
The dataset used in this project contains transaction details of users. You can use a dataset like the Personal Finance Dataset on Kaggle or simulate sample data. The dataset has the following columns:
user_id: Unique identifier for each user


transaction_date: Date when the transaction occurred


transaction_amount: Amount spent on the transaction


transaction_category: Category of the transaction (e.g., Rent, Grocery, Entertainment)


Sample transactions.csv:
user_id,transaction_date,transaction_amount,transaction_category
1,2023-01-02,1200,Rent
1,2023-01-03,150,Grocery
1,2023-01-10,40,Entertainment
2,2023-01-04,1000,Rent
2,2023-01-07,200,Investment
2,2023-01-09,300,Grocery
...


Data Cleaning & Feature Engineering
The finance_clustering.ipynb notebook covers data preprocessing and feature engineering steps, including:
Converting transaction dates to proper datetime format


Aggregating transaction data by user (total spent, average transaction, transaction count)


Calculating the percentage of spending by category (Rent, Grocery, Entertainment)


Normalizing the data using StandardScaler for clustering



Clustering
KMeans clustering is applied to group users based on their spending patterns. The number of clusters is set to 4, but this can be adjusted as needed.
KMeans Implementation:
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X_scaled)


Data Visualization
To better understand the clusters, we use PCA (Principal Component Analysis) to reduce the data to two dimensions and visualize it in a 2D scatter plot.
Visualization Code:
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

sns.scatterplot(data=final_df, x='pca_1', y='pca_2', hue='cluster', palette='Set2')


Insights
After clustering, you can analyze and describe the characteristics of each cluster. For example:
Cluster 0: Big spenders, heavy entertainment expenditure


Cluster 1: Careful savers, high rent percentage


Additional clusters with varying financial behaviors can be explored.


To generate the insights:
for c in final_df['cluster'].unique():
    display(final_df[final_df['cluster'] == c].describe())


Streamlit App (Optional)
A Streamlit app is included to allow users to input their financial data and predict their cluster.
App Code (app/app.py):
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


Conclusion
This project is a complete end-to-end analysis that combines machine learning, data preprocessing, and visualization to provide valuable insights into personal finance decision-making. The project will help demonstrate your ability to work with real-world datasets, apply clustering algorithms, and present actionable insights
Thank you for exploring this project! Feel free to contribute and provide feedback.



