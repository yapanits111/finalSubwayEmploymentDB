# main.py
import os
import streamlit as st
from create_application import new_application
from streamlit_option_menu import option_menu
from admin_login import admin_panel 
from sql_queries import sql_queries
import pandas as pd

st.set_page_config(page_title="Subway Application Management", page_icon=":sandwich:", layout="wide")

st.markdown(
    '''
    <style>
       [data-testid="stApp"] {
            background-color: #EBEBEB;
            background-size: cover;
        }
        
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stSidebarContent"]{
            background-color: #0D4E16;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
#pabago nalang ung pic nsa gdrive na
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    image_path = os.path.abspath("newlogo.png")
    st.image(image_path)

with st.sidebar:
    selected = option_menu (
        menu_title="Navigation",
        options = ["Create New Application", "Admin Panel", "SQL Queries"],
        icons = ["pencil-square", "shield-shaded", "filetype-sql"],
        menu_icon ="person-walking",
        default_index=0,
        styles= {
            "container-xxl": {"background-color": "#EBEBEB"},
            "menu-title": {"font-size": "18px"},
            "icon": { "font-size": "15px"},
            "nav-link": {
                "font-size": "15px",
                "--hover-color": "#eee",
            }
        }
    )

if selected == "Create New Application":
    new_application()
if selected == "Admin Panel":
    admin_panel()
if selected == "SQL Queries":
    sql_queries()
