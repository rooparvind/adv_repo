
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')
df["model_year"] = pd.to_numeric(df["model_year"], errors="coerce") 
df["price"] = pd.to_numeric(df["price"], errors="coerce") 
df["cylinders"] = pd.to_numeric(df["cylinders"], errors="coerce") 
df['price'] = df['price'].astype('float32') 

# NaN values
df['price'] = df['price'].fillna(0)

# Handle missing values and convert data types
df['days_listed'] = df['days_listed'].fillna(0).astype('float32')
df['model_year'] = df['model_year'].fillna(0).astype("Int64")
df['cylinders'] = df['cylinders'].fillna(0).astype("Int64")
df['odometer'] = df['odometer'].fillna(0).astype('float32')
df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)  
df['paint_color'] = df['paint_color'].fillna("unknown")

print(df.dtypes)
print(df.isnull().sum())

df['manufacturer'] = df['model'].fillna("Unknown").apply(lambda x: x.split()[0])

st.header("Data Viewer")
if df.empty:
    st.write("No data available.")
else:
    st.dataframe(df)

show_manuf_1k_ads = st.checkbox('Include manufacturers with less than 1000 ads')
if not show_manuf_1k_ads:
    df = df.groupby('manufacturer').filter(lambda x: len(x) > 1000)

st.dataframe(df)
st.header('Vehicle types by manufacturer')
st.write(px.histogram(df, x='manufacturer', color='type'))
st.header('Histogram of `condition` vs `model_year`')

# histograms in plotly_express:
st.write(px.histogram(df, x='model_year', color='condition'))
# a lot more concise!
# -------------------------------------------------------

st.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox('Select manufacturer 1',
                              manufac_list, index=manufac_list.index('dodge'))

manufacturer_2 = st.selectbox('Select manufacturer 2',
                              manufac_list, index=manufac_list.index('ford'))
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay'))