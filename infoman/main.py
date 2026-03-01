# main.py
import os
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import date

st.set_page_config(page_title="Subway Application Management", page_icon=":sandwich:", layout="wide")

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'applicant_info' not in st.session_state:
    st.session_state.applicant_info = {
        'applicant_name': "",
        'tax_ID_num': 0,
        'applicant_address': "",
        'applicant_tel_num': 0,
        'age_verification': "Yes",
        'emergency_name': "",
        'emergency_tel_num': 0,
        'emergency_address': "",
        'position_type': "Part Time",
        'total_hours': 0,
        'date_availability': date.today(),
        'school_name': "",
        'school_address': "",
        'school_tel_num': 0,
        'counselor_name': "",
        'grade_completed': 'Elementary',
        'GWA': 0.0,
        'graduated': "Yes",
        'enrolled': "Yes"
    }

if 'employment_history' not in st.session_state:
    st.session_state.employment_history = [{
        'company_name': "",
        'company_address': "",
        'company_tel_num': 0,
        'position': "",
        'supervisor': "",
        'date_worked_from': date.today(),
        'date_worked_to': date.today(),
        'wage': 0,
        'mgnt_ref_ck': "",
        'reason_for_leaving': "",
        'permission': "Yes"
    }]

if 'references' not in st.session_state:
    st.session_state.references = [{
        'ref_name': "",
        'ref_tel_num': 0,
        'years_known': 0,
        'ref_address': ""
    }]

# Import after session state initialization
from create_application import new_application
from admin_login import admin_panel 
from sql_queries import sql_queries

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
        
        /* Fixed width main content */
        .main .block-container {
            max-width: 1200px;
            padding-left: 2rem;
            padding-right: 2rem;
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
