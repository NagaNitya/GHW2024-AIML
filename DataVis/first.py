import streamlit as st
import pandas as pd
import warnings
from visualisations import (plot_market_cap_dist)

warnings.filterwarnings('ignore')

st.set_page_config(layout="wide")

def load_csv(file_path):
    #load csv file and process Market Cap (USD) column
    df = pd.read_csv(file_path, index_col=0)
    return df

def main():
    st.title('Company Data Visualisation')

    chart_type = st.sidebar.radio('Select Chart Type', ['Data Table', 'Market Cap Distribution', 'Line Chart', 'Scatter Plot'])
    df = load_csv('companies_data.csv')

    if chart_type == 'Data Table':
        st.dataframe(df)
    elif chart_type == 'Market Cap Distribution':
        fig= plot_market_cap_dist(df)
        st.pyplot(fig)
    

if __name__ == '__main__':
    main() 