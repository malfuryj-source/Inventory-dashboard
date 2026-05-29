import streamlit as st
import pandas as pd
st.set_page_config(
page_title="Inventory Dashboard",
page_icon="📦",
layout="wide"
)
# Sidebar Navigation

st.sidebar.title("📦 Inventory Control")

st.sidebar.caption(
"Daily Stock Monitoring System"
)

page = st.sidebar.radio(
"Navigation",
[
"Dashboard",
"Critical Items",
"Inventory Table",
"AI Assistant"
]
)

st.markdown("""
<style>
.main {
padding-top: 1rem;
}

h1 {
color: #4CAF50;
}

[data-testid="metric-container"] {
background-color: #262730;
border: 1px solid #4CAF50;
padding: 15px;
border-radius: 10px;
}
</style>    
""", unsafe_allow_html=True)

df = pd.read_excel("inventory.xlsx")


df["Stock Value"] = df["Current Stock"] * df["Unit Cost"]
df = pd.read_excel("inventory.xlsx")

df["Stock Value"] = df["Current Stock"] * df["Unit Cost"]

def get_status(row):
    if row["Current Stock"] < row["Min Stock"]:
        return "Low Stock"
    elif row["Current Stock"] > row["Max Stock"]:
        return "Over Stock"
    else:
        return "Normal"

df["Status"] = df.apply(get_status, axis=1)

df["Suggested Order Qty"] = (
df["Max Stock"] - df["Current Stock"]
).clip(lower=0)

total_stock_value = df["Stock Value"].sum()
low_stock_count = len(df[df["Current Stock"] < df["Min Stock"]])
over_stock_count = len(df[df["Current Stock"] > df["Max Stock"]])

st.title("📦 Inventory Dashboard")
st.caption("Daily Stock Monitoring & Analysis")

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
if page == "Dashboard":

    st.subheader("Inventory Data")

    st.dataframe(
        df,
        use_container_width=True
)

    st.subheader("Stock Status Distribution")

    status_counts = (df["Status"].value_counts()
)

    st.bar_chart(status_counts)

    st.subheader(
        "Current Stock by Item"
)

    st.bar_chart(
    df.set_index("Item Name")[
        "Current Stock"
    ]
)

elif page == "Critical Items":

    st.subheader(
    "🚨 Critical Items")

    critical_items = df[
        df["Status"] == "Low Stock"
]

st.dataframe(
    critical_items,
    use_container_width=True
)

elif page == "Inventory Table":

    st.subheader("📋 Full Inventory")

    st.dataframe(
    df,
    use_container_width=True
)

elif page == "AI Assistant":

    st.subheader("🤖 AI Assistant")

    question = st.text_input(
    "Ask about inventory"
)

if question:
    st.info(
        "AI assistant will be connected next."
)
