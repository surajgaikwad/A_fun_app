import streamlit as st

st.title(":red[Innomatics] Internship 2023")
st.header("First Streamlit App")
st.snow()

btn_click = st.button("Select Me!")

if btn_click == True:
    st.subheader("Yaay!! You selected me :man_dancing:")
    st.balloons()