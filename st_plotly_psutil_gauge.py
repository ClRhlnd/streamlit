import streamlit as st
import plotly.graph_objects as go
import psutil

battery = psutil.sensors_battery()

fig = go.Figure(
    go.Indicator(
        value=battery.percent,
        mode="gauge+number",
        domain={"x": [0,1], "y": [0,1]},
        title={"text": "Battery Level"},
        
        gauge={
            "axis": {"range":[0,100]},
            "bar": {'color':"darkblue", "thickness": 0.3},
            "steps": [
                {"range":[0,10],"color":"red"},
                {"range":[10,70], "color":"yellow"}
            ],
        }
    )
)

st.subheader("Battery level in Streamlit with plotly Gauge")
st.plotly_chart(fig)
