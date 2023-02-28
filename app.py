import streamlit as st

st.title("Innomatics Internship 2023")
st.snow()

btn_click = st.button("Select Me!")

if btn_click == True:
    st.subheader("Yaay!! You selected me :happy:")
    st.balloons()