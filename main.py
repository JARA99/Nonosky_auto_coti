import streamlit as st
import pandas as pd

st.title('Nonosky - Generar cotización')

data = st.file_uploader('Suba un archivo de excel.')


# if st.button("Leer"):
if data:
    df = pd.read_excel(data)

    # st.write(df)
    st.data_editor(df)

    if st.button('Generar'):
        textable = df.to_latex(
            index=False, column_format='|p{0.43\\linewidth}|C{0.15\\linewidth}|C{0.15\\linewidth}|C{0.15\\linewidth}|')

        textable_s = textable.split('\n')
        textable_x = textable_s[0:0] + textable_s[4:-2] + [textable_s[-2]]
        # textable = '\n'.join(textable_s)
        st.text(textable_x)

        # st.write(textable)

# data['Precio por unidad'] = data['Precio por unidad'].apply(lambda x: f"Q{x:,.2f}")
