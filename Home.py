import streamlit as st
import pandas

df = pandas.read_csv("data.csv", sep=";")

#layout
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

#with col1:
    #st.image("images/photo.png")

with col2:
    st.title("Batu Hofer")
    content = """
    Welcome to my profile. This is my bio.
    """
    st.info(content)

content2 = "Some apps I built below:"
st.text(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        #st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        #st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")