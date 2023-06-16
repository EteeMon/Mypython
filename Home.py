import streamlit as st
st.header('kairung')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./pic/setosa.jpg")

with col2:
   st.header("Verginiga")
   st.image("./pic/versicolor.jpg")

with col3:
   st.header("Setosa")
   st.image("./pic/virginica.jpg")