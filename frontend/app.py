# frontend appss

#installing dependencies
import PIL
import streamlit as st
import frontend_funcs







#initializing the page
icon_load = PIL.Image.open("resources/page_icon.ico")
st.set_page_config(page_title="Notenrechner light",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Test") # ! NOT WORKING YET; NEEDS FIX
#st.header("Notenrechner light")