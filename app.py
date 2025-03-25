import streamlit as st
# import pages.ContactMe
from pages import home

# Set page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


from streamlit_option_menu import option_menu
st.header("Data Science Portfolio")

selected_menu=option_menu("",
            ["Home","About","Project","Contact Me"]
            , orientation="horizontal",
            icons=[ ],
            default_index=0)
if selected_menu=="Home":
    home.app()


# if selected_menu=="About":
#     pages.About

# if selected_menu=="Project":
#    pages.Project

# if selected_menu=="Contact Me":
#     pages.ContactMe






