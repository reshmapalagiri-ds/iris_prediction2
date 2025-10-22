import streamlit as st
st.title("My first streamlit App")
st.write("Hello, streamlit this is my first web app")
st.header('1.TEXT ELEMENT')
st.subheader("this is the subheader")
st.text("this is the simple text")
st.markdown("this is a markdown")

st.header("User Input Info")
name=st.text_input("enter your name")
age=st.slider("select your age:",1,100,25)
if st.button("submit"):
    st.write(f"Hello {name}! you are {age} years old")

st.sidebar.title("app settings")
options=st.sidebar.selectbox(""
        "choose your view",
        ("Data view","chat view","summary")
        )
st.write(f"you selected {options}")