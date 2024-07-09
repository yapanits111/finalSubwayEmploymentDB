import streamlit as st
import pandas as pd
from db_functions import *

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.session_state['logged_in'] = True

def logout():
    st.session_state['logged_in'] = False
    st.session_state.pop('selected_id', None)
    st.session_state.pop('applicant_info', None)
    st.session_state.pop('employment_history', None)
    st.session_state.pop('references', None)

def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if username == 'admin' and password == 'pass':
            login()
            st.success("Logged In as Admin")
        else:
            st.error("Incorrect username or password")

def display_dataframes():
    st.subheader("Admin Panel")

    applicant_data = get_all_applicant_info()
    df1 = pd.DataFrame(applicant_data, columns=[
        "Employee Number", "Name", "Tax ID", "Address", "Phone", "Age Verification",
        "Emergency Name", "Emergency Phone", "Emergency Address", "Position Type", "Hours", 
        "Start Date", "School", "School Address", "School Phone", "Counselor", "Grade", 
        "GWA", "Graduated", "Enrolled"
    ])
    employment_data = get_all_employment_history()
    df2 = pd.DataFrame(employment_data, columns=[
        "History Code", "Employee Number", "Company Name", "Company Address", "Company Phone", 
        "Position", "Supervisor", "Start Date", "End Date", "Wage", "Management Reference Checked By", 
        "Reason For Leaving", "Permission to Contact"
    ])
    reference_data = get_all_references()
    df3 = pd.DataFrame(reference_data, columns=[
        "Reference Code", "Employee Number", "Name", "Contact Number", "Years Known", "Address"
    ])

    st.write("Employee Information")
    st.dataframe(df1)
    st.write("Employment Histories")
    st.dataframe(df2)
    st.write("References")
    st.dataframe(df3)

def update_applicant_details():
    applicant_info = st.session_state['applicant_info']
    employment_history = st.session_state['employment_history']
    references = st.session_state['references']

    st.write("Update Applicant Information")

    st.subheader("*I. Personal Information*")
    updated_name = st.text_input("Full Name", value=applicant_info["applicant_name"], key="applicant_name")
    updated_tax_id = st.text_input("Tax ID Number", value=applicant_info["tax_ID_num"], key="tax_ID_num")
    updated_address = st.text_input("Address", value=applicant_info["applicant_address"], key="applicant_address")
    updated_tel_num = st.text_input("Phone Number", value=applicant_info["applicant_tel_num"], key="applicant_tel_num")
    updated_age_verification = st.radio("16 Years or above?", ["Yes", "No"], index=0 if applicant_info["age_verification"] == "Yes" else 1, key="age_verification")

    st.subheader("*II. Emergency Contact*")
    updated_emergency_name = st.text_input("Emergency Contact Name", value=applicant_info["emergency_name"], key="emergency_name")
    updated_emergency_tel_num = st.text_input("Emergency Contact Number", value=applicant_info["emergency_tel_num"], key="emergency_tel_num")
    updated_emergency_address = st.text_input("Contact Address", value=applicant_info["emergency_address"], key="emergency_address")

    st.subheader("*III. Availability*")
    updated_position_type = st.radio("Position Type", ["Part Time", "Full Time", "Seasonal", "Temporary"], index=["Part Time", "Full Time", "Seasonal", "Temporary"].index(applicant_info["position_type"]), key="position_type")
    updated_total_hours = st.number_input("Total Hours Available Per Week", value=int(applicant_info["total_hours"]), key="total_hours")
    updated_date_availability = st.date_input("Date Available to Start Work", value=pd.to_datetime(applicant_info["date_availability"]), key="date_availability")

    st.subheader("*IV. School Most Recent Attended*")
    updated_school_name = st.text_input("School Name", value=applicant_info["school_name"], key="school_name")
    updated_school_address = st.text_input("School Address", value=applicant_info["school_address"], key="school_address")
    updated_school_tel_num = st.text_input("School Telephone Number", value=applicant_info["school_tel_num"], key="school_tel_num")
    updated_counselor_name = st.text_input("Counselor Name", value=applicant_info["counselor_name"], key="counselor_name")
    updated_grade_completed = st.radio("Last Grade Completed", ['Elementary', 'Junior High School', 'Senior High School', 'College'], index=['Elementary', 'Junior High School', 'Senior High School', 'College'].index(applicant_info["grade_completed"]), horizontal=True, key="grade_completed")
    updated_GWA = st.number_input("Most Recent GWA", value=float(applicant_info["GWA"]), key="GWA")
    updated_graduated = st.radio("Graduated?", ["Yes", "No"], index=0 if applicant_info["graduated"] == "Yes" else 1, key="graduated")
    updated_enrolled = st.radio("Currently Enrolled?", ["Yes", "No"], index=0 if applicant_info["enrolled"] == "Yes" else 1, key="enrolled")

    st.write("Update Employment History")
    updated_employment_history = []
    for i, emp in enumerate(employment_history):
        st.subheader(f"*Employment Record {i+1}*")
        emp['company_name'] = st.text_input(f"Company Name", value=emp['company_name'], key=f"company_name_{i+1}")
        emp['company_address'] = st.text_input(f"Company Address", value=emp['company_address'], key=f"company_address_{i+1}")
        emp['company_tel_num'] = st.text_input(f"Company Telephone Number", value=emp['company_tel_num'], key=f"company_tel_num_{i+1}")
        emp['position'] = st.text_input(f"Position", value=emp['position'], key=f"position_{i+1}")
        emp['supervisor'] = st.text_input(f"Supervisor", value=emp['supervisor'], key=f"supervisor_{i+1}")
        emp['date_worked_from'] = st.date_input(f"Date Worked From", value=pd.to_datetime(emp['date_worked_from']), key=f"date_worked_from_{i+1}")
        emp['date_worked_to'] = st.date_input(f"Date Worked To", value=pd.to_datetime(emp['date_worked_to']), key=f"date_worked_to_{i+1}")
        emp['wage'] = st.number_input(f"Wage Per Month", value=int(emp['wage']), key=f"wage_{i+1}")
        emp['mgnt_ref_ck'] = st.text_input(f"Management Reference Checked By", value=emp['mgnt_ref_ck'], key=f"mgnt_ref_ck_{i+1}")
        emp['reason_for_leaving'] = st.text_input(f"Reason for Leaving", value=emp['reason_for_leaving'], key=f"reason_for_leaving_{i+1}")
        emp['permission'] = st.radio(f"Permission to Contact", ["Yes", "No"], index=0 if emp['permission'] == "Yes" else 1, key=f"permission_{i+1}")
        updated_employment_history.append(emp)

    st.write("Update References")
    updated_reference = []
    for i, ref in enumerate(references):
        st.subheader(f"*Reference {i+1}*")
        ref['ref_name'] = st.text_input(f"Reference Name", value=ref['ref_name'], key=f"ref_name_{i+1}")
        ref['ref_tel_num'] = st.text_input(f"Reference Telephone Number", value=ref['ref_tel_num'], key=f"ref_tel_num_{i+1}")
        ref['years_known'] = st.number_input(f"Years Known", value=int(ref['years_known']), key=f"years_known_{i+1}")
        ref['ref_address'] = st.text_input(f"Reference Address", value=ref['ref_address'], key=f"ref_address_{i+1}")
        updated_reference.append(ref)

    if st.button("Update"):
        try:
            update_applicant_info(
                st.session_state['selected_id'], updated_name, updated_tax_id, updated_address, updated_tel_num, 
                updated_age_verification, updated_emergency_name, updated_emergency_tel_num, 
                updated_emergency_address, updated_position_type, updated_total_hours, updated_date_availability, 
                updated_school_name, updated_school_address, updated_school_tel_num, updated_counselor_name, 
                updated_grade_completed, updated_GWA, updated_graduated, updated_enrolled
            )
            for emp in updated_employment_history:
                update_employment_history(
                    emp['history_code'], emp['emp_num'], emp['company_name'], emp['company_address'], 
                    emp['company_tel_num'], emp['position'], emp['supervisor'], emp['date_worked_from'], 
                    emp['date_worked_to'], emp['wage'], emp['mgnt_ref_ck'], emp['reason_for_leaving'], emp['permission']
                )
            for ref in updated_reference:
                update_reference(
                    ref['ref_code'], ref['emp_num'], ref['ref_name'], ref['ref_tel_num'], 
                    ref['years_known'], ref['ref_address']
                )
            st.success("Record updated successfully")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    if st.button("Delete"):
        delete_data(st.session_state['selected_id'])
        st.success("Record deleted successfully")
        display_dataframes()

def admin_panel():
    if not st.session_state['logged_in']:
        admin_login()
        return
    else:
        st.write("Welcome, admin! You are logged in.")
        display_dataframes()

    selected_id = st.text_input("Enter Employee Number to update/delete:")

    if st.button("Search"):
        try:
            if selected_id:
                selected_id = int(selected_id)
                st.session_state['selected_id'] = selected_id
                st.session_state['applicant_info'] = get_applicant_info_by_emp_num(selected_id)
                st.session_state['employment_history'] = get_employment_history_by_emp_num(selected_id)
                st.session_state['references'] = get_references_by_emp_num(selected_id)
                
                if st.session_state['applicant_info']:
                    update_applicant_details()
                else:
                    st.warning("No record found for the given Employee Number")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    if 'selected_id' in st.session_state:
        update_applicant_details()

    if st.button("Logout"):
        logout()
        st.success("Logged out successfully")

def main():
    if st.session_state['logged_in']:
        admin_panel()
    else:
        admin_login()

if __name__ == "__main__":
    main()
