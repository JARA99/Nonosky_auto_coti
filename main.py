import streamlit as st
import pandas as pd

st.title('Nonosky - Generar cotización')

data = st.file_uploader('Suba un archivo de excel.')


if st.button("Leer"):
    df = pd.read_excel(data)

    # st.write(df)
    st.data_editor(df)
