import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Taxidermy Studio", layout="wide")

# Title
st.title("🦌 Taxidermy Studio")
st.subheader("Preserving Nature with Art")

# Hero Image
st.image("hero.jpg", use_column_width=True)

st.write("""
Welcome to our professional Taxidermy Studio.  
We specialize in preserving wildlife with artistic detail.
""")

# Sidebar
menu = st.sidebar.selectbox(
    "Menu",
    ["Home","Gallery","Videos","Upload Photo","About","Contact"]
)

# Home
if menu == "Home":
    st.header("Welcome")
    st.write("Professional Taxidermy Services")

# Gallery
elif menu == "Gallery":
    st.header("Animal Gallery")

    cols = st.columns(3)

    cols[0].image("images/animal1.jpg")
    cols[1].image("images/animal2.jpg")
    cols[2].image("images/animal3.jpg")

# Videos
elif menu == "Videos":
    st.header("Taxidermy Process Videos")

    st.video("videos/process1.mp4")
    st.video("videos/process2.mp4")

# Upload
elif menu == "Upload Photo":
    st.header("Upload Your Animal Photo")

    uploaded_file = st.file_uploader("Choose image", type=["jpg","png"])

    if uploaded_file:
        st.image(uploaded_file)

# About
elif menu == "About":
    st.header("About Taxidermy")

    st.write("""
Taxidermy is the art of preserving animals for study or display.
Our studio provides high-quality preservation services.
""")

# Contact
elif menu == "Contact":
    st.header("Contact Us")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        st.success("Message Sent!")
