# frontend appss

#installing dependencies
import PIL
import streamlit as st
import frontend_funcs






#set the page icon and title
icon_load = PIL.Image.open("resources/page_icon.ico")
st.set_page_config(page_title="Notenrechner light home",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")

#title the page
st.title("Notenrechner light") 




