import streamlit as st
import pandas as pd
import numpy as np
from streamlit_dynamic_filters import DynamicFilters

st.title('Top Movies Of Each Year')

# Load data from CSV
df = pd.read_csv('TopMovie&Genre_Data.csv')

# Dynamic Filtering
movie_filters = DynamicFilters(df, filters=['Genre', 'Year'])
with st.sidebar:
    st.write("Select Filters")
movie_filters.display_filters(location='sidebar')

# Write raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    movie_filters.display_df()

# Graph of top grossing movie of each genre
# st.write(filtered_df)





## JUNKYARD ##
# st.subheader('1995 Movies')
# df1995 = df[(df["Year"] == 1995)]
# st.write(df1995)

# Allow filter for genre
# year_to_filter = st.slider('Year', 1995, 2018, 2010)
# filtered_df = df[df["Year"] == year_to_filter]
# st.subheader('Top Movies by Genre from %s' % year_to_filter)



