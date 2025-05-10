import streamlit as st

import pandas as pd
from google.cloud import firestore

db = firestore.Client.from_service_account_json("serviceAccountKey.json")

st.header(type(df))
# docs = db.collection("iris").stream()
# data = []
# for d in docs:
#     data.append(d.to_dict())
spieces = st.sidebar.selectbox("spieces", ["setosa","versicolor","virginica"])
# df = pd.DataFrame(data)
# df = df[df["species"] == spieces].reset_index(drop=True)
# st.write(df)
# st.line_chart(df, x="sepal_length", y="sepal_width")
