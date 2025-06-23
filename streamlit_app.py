import streamlit as st
from pyairtable import Table
import pandas as pd
import os

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# Read API key, base ID, and table name from Streamlit secrets or environment variables
api_key = st.secrets["airtable"]["api_key"] if "airtable" in st.secrets else os.getenv("AIRTABLE_API_KEY")
base_id = st.secrets["airtable"]["base_id"] if "airtable" in st.secrets else os.getenv("AIRTABLE_BASE_ID")
table_name = st.secrets["airtable"]["table_name"] if "airtable" in st.secrets else os.getenv("AIRTABLE_TABLE_NAME")

# Connect to Airtable
table = Table(api_key, base_id, table_name)

# Fetch records
records = table.all()
data = [record['fields'] for record in records]
df = pd.DataFrame(data)

st.title("Airtable Data")
st.write(df)
