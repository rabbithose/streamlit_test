import streamlit as st
import random
omikuzi = ["大吉","中吉","小吉","凶"]

if st.button("おみくじ"):
    st.write(random.choice(omikuzi))