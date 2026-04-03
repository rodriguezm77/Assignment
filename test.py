import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('brooklyn_bridge_pedestrians(1).csv')

st.header('Brooklyn Bridge Crossings')
st.subheader('Pedestrian Traffic Oct 2017 - Jun 2018')

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df.set_index("hour_beginning", inplace=True)

a = df.select_dtypes(include = "number")

Type = st.sidebar.radio('Type:', ['Hourly', 'Daily', 'Weekly'])

if Type == 'Hourly':
    result = a
elif Type == "Daily":
    result = a.resample('D').sum()
else:
    result = a.resample('W').sum()
st.write(result)

fig, ax = plt.subplots()
ax.plot(df['pedestrians'])
ax.set_xlabel("Date")
ax.set_ylabel('# of Pedestrians')
st.pyplot(fig)

if Type == 'Hourly':
    result = df["pedestrians"]

elif Type == 'Daily':
    result = df["pedestrians"].resample("D").sum()

else:
    result = df["pedestrians"].resample("W").sum()

total_pedestrians = result.sum()
average_pedestrians = result.mean()

col1, col2 = st.columns(2)

col1.metric("Total Pedestrians", f"{total_pedestrians:,.0f}")
col2.metric("Average Pedestrians", f"{average_pedestrians:,.2f}")

fig1, ax = plt.subplots()
ax.plot(df.index, df['to_manhattan'], label = 'To Manhattan', color = 'red')
ax.plot(df.index, df['to_brooklyn'], label = 'To Brooklyn', color = 'blue')
ax.legend()

st.pyplot(fig1)
