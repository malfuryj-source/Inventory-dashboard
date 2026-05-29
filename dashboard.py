import streamlit as st
import pandas as pd

df = pd.read_excel("inventory.xlsx")

df["Stock Value"] = df["Current Stock"] * df["Unit Cost"]

def get_status(row):
    if row["Current Stock"] < row["Min Stock"]:
        return "Low Stock"
    elif row["Current Stock"] > row["Max Stock"]:
        return "Over Stock"
    else:
        return "Normal"

total_stock_value = df["Stock Value"].sum()
low_stock_count = len(df[df["Current Stock"] < df["Min Stock"]])
over_stock_count = len(df[df["Current Stock"] > df["Max Stock"]])

st.title("Inventory Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Stock Value", round(total_stock_value, 2))

with col2:
    st.metric("Low Stock", low_stock_count)

with col3:
    st.metric("Over Stock", over_stock_count)

    st.subheader("Inventory Data")
    st.subheader("Stock Status Distribution")

status_counts = df["Status"].value_counts()

st.bar_chart(status_counts)
st.dataframe(df)
st.subheader("Current Stock by Item")

st.bar_chart(
df.set_index("Item Name")["Current Stock"]
)

