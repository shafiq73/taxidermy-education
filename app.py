import streamlit as st

st.set_page_config(page_title="Taxidermy Education", layout="wide")

st.title("Learn Taxidermy")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Home","Education","Tutorials","Reading List","FAQ"]
)

if menu == "Home":
    st.header("Welcome")
    st.write("Learn the art and science of taxidermy.")

elif menu == "Education":
    st.header("Intro to Taxidermy")
    st.write("Taxidermy is preserving animals for study and display.")
    st.header("Laws")
    st.write("- Lacey Act\n- CITES\n- Endangered Species Act\n- Migratory Bird Treaty Act")
    st.header("Supplies")
    st.write("- Mounting forms\n- Chemicals\n- Tools")
