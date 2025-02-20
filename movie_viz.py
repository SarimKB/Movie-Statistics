import streamlit as st
import pandas as pd
import numpy as np
from streamlit_dynamic_filters import DynamicFilters

st.title('Movie Genre Statistics')

# Global Vars
YEAR_COL = "Year"
GEN_COL = "Genre"
GEN_GROSS_COL = "Gross"
GEN_IGROSS_COL = "Inflation-Adjusted Gross"
MOV_COL = "Top Movie"
MOV_GROSS_COL = "Top Movie Gross (That Year)"
MOV_IGROSS_COL = "Top Movie Inflation-Adjusted Gross (That Year)"

# Load data from CSV file
df = pd.read_csv('TopMovie&Genre_Data.csv')

# Dynamic Filtering
movie_filters = DynamicFilters(df, filters=['Genre'])
with st.sidebar:
    st.write("Select Filters")
movie_filters.display_filters(location='sidebar')

# Applying chosen filter to dataframe
filt_df = movie_filters.filter_df()

# Write raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    movie_filters.display_df()


# Graph of top grossing movie of each genre
Genre_filt = "(Genre Here)"
st.write("%s Movies Grossed" % Genre_filt)
#st.bar_chart(data=df[(df[GEN_COL] == 'Action')], x=YEAR_COL, y=GEN_GROSS_COL, x_label="Year", y_label="Total Grossed")
st.bar_chart(data=filt_df, x=YEAR_COL, y=GEN_GROSS_COL, x_label="Year", y_label="Total Grossed ($USD)")


### JUNKYARD ###
# st.subheader('1995 Movies')
# df1995 = df[(df["Year"] == 1995)]
# st.write(df1995)

# Allow filter for genre
# year_to_filter = st.slider('Year', 1995, 2018, 2010)
# filtered_df = df[df["Year"] == year_to_filter]
# st.subheader('Top Movies by Genre from %s' % year_to_filter)



