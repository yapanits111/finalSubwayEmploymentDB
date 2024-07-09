import streamlit as st
from db_functions import create_applicant_info, create_employment_history, create_reference
from datetime import date

# Initialize session state
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

# Functions to add employment history and reference
def add_employment_history():
    st.session_state.employment_history.append({
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
    })

def add_reference():
    st.session_state.references.append({
        'ref_name': "",
        'ref_tel_num': 0,
        'years_known': 0,
        'ref_address': ""
    })

# Application form function
def new_application():
    st.header("Employment Application Form")

    with st.form(key='new_application', clear_on_submit = True):
        st.subheader("*I. Personal Information*")
        applicant_name = st.text_input("Full Name", value=st.session_state.applicant_info['applicant_name'], key='applicant_name')
        tax_ID_num = st.number_input("Tax ID Number", value=st.session_state.applicant_info['tax_ID_num'], format="%d", key='tax_ID_num')
        applicant_address = st.text_input("Address", value=st.session_state.applicant_info['applicant_address'], key='applicant_address')
        applicant_tel_num = st.number_input("Cell/Telephone Number", value=st.session_state.applicant_info['applicant_tel_num'], format="%d", key='applicant_tel_num')
        age_verification = st.radio("Are You 16 years of age or over?", ["Yes", "No"], index=0 if st.session_state.applicant_info['age_verification'] == "Yes" else 1, key='age_verification')
        st.divider()

        st.subheader("*II. In Case of Emergency, Notify*")
        emergency_name = st.text_input("Emergency Contact Name", value=st.session_state.applicant_info['emergency_name'], key='emergency_name')
        emergency_tel_num = st.number_input("Contact Number", value=st.session_state.applicant_info['emergency_tel_num'], format="%d", key='emergency_tel_num')
        emergency_address = st.text_input("Contact Address", value=st.session_state.applicant_info['emergency_address'], key='emergency_address')
        st.divider()

        st.subheader("*III. Availability*")
        position_type = st.radio("Position Type", ["Part Time", "Full Time", "Seasonal", "Temporary"], index=["Part Time", "Full Time", "Seasonal", "Temporary"].index(st.session_state.applicant_info['position_type']), key='position_type')
        total_hours = st.number_input("Total Hours Available Per Week", value=st.session_state.applicant_info['total_hours'], format="%d", key='total_hours')
        date_availability = st.date_input("Date Available to Start Work", value=st.session_state.applicant_info['date_availability'], key='date_availability')
        st.divider()

        st.subheader("*IV. School Most Recent Attended*")
        school_name = st.text_input("School Name", value=st.session_state.applicant_info['school_name'], key='school_name')
        school_address = st.text_input("School Address", value=st.session_state.applicant_info['school_address'], key='school_address')
        school_tel_num = st.number_input("School Telephone Number", value=st.session_state.applicant_info['school_tel_num'], format="%d", key='school_tel_num')
        counselor_name = st.text_input("Counselor Name", value=st.session_state.applicant_info['counselor_name'], key='counselor_name')
        grade_completed = st.radio("Last Grade Completed", ['Elementary', 'Junior High School', 'Senior High School', 'College'], index=['Elementary', 'Junior High School', 'Senior High School', 'College'].index(st.session_state.applicant_info['grade_completed']), horizontal=True, key='grade_completed')
        GWA = st.number_input("Most Recent GWA", value=st.session_state.applicant_info['GWA'], key='GWA')
        graduated = st.radio("Graduated?", ["Yes", "No"], index=0 if st.session_state.applicant_info['graduated'] == "Yes" else 1, key='graduated')
        enrolled = st.radio("Now Enrolled?", ["Yes", "No"], index=0 if st.session_state.applicant_info['enrolled'] == "Yes" else 1, key='enrolled')
        st.divider()

        st.subheader("*V. Most Recent Employment*")
        for i, emp in enumerate(st.session_state.employment_history):
            st.write(f"Employment History {i+1}")
            emp['company_name'] = st.text_input(f"Company Name", value=emp['company_name'], key=f'company_name_{i+1}')
            emp['company_address'] = st.text_input(f"Company Address", value=emp['company_address'], key=f'company_address_{i+1}')
            emp['company_tel_num'] = st.number_input(f"Company Telephone Number", value=emp['company_tel_num'], key=f'company_tel_num_{i+1}', format="%d")
            emp['position'] = st.text_input(f"Position", value=emp['position'], key=f'position_{i+1}')
            emp['supervisor'] = st.text_input(f"Supervisor", value=emp['supervisor'], key=f'supervisor_{i+1}')
            emp['date_worked_from'] = st.date_input(f"Date Worked From", value=emp['date_worked_from'], key=f'date_worked_from_{i+1}')
            emp['date_worked_to'] = st.date_input(f"Date Worked To", value=emp['date_worked_to'], key=f'date_worked_to_{i+1}')
            emp['wage'] = st.number_input(f"Wage Per Month ", value=emp['wage'], key=f'wage_{i+1}', format="%d")
            emp['mgnt_ref_ck'] = st.text_input(f"Management Reference Checked By", value=emp['mgnt_ref_ck'], key=f'mgnt_ref_ck_{i+1}')
            emp['reason_for_leaving'] = st.text_input(f"Reason for Leaving", value=emp['reason_for_leaving'], key=f'reason_for_leaving_{i+1}')
            emp['permission'] = st.radio(f"Do we have your permission to contact your previous employer?", ['Yes', 'No'], index=0 if emp['permission'] == "Yes" else 1, key=f'permission_{i+1}')

        new_empHist = st.form_submit_button("Add Employment History")
        if new_empHist:
            add_employment_history()

        st.subheader("*VI. References*")
        for j, ref in enumerate(st.session_state.references):
            st.write(f"Reference Person {j+1}")
            ref['ref_name'] = st.text_input(f"Full Name", value=ref['ref_name'], key=f'ref_name_{j+1}')
            ref['ref_tel_num'] = st.number_input(f"Tel. Number", value=ref['ref_tel_num'], key=f'ref_tel_num_{j+1}', format="%d")
            ref['years_known'] = st.number_input(f"Years Known", value=ref['years_known'], key=f'years_known_{j+1}')
            ref['ref_address'] = st.text_input(f"Address", value=ref['ref_address'], key=f'ref_address_{j+1}')

        new_ref = st.form_submit_button("Add Reference Person")
        if new_ref:
            add_reference()

        submitted = st.form_submit_button('Submit')
        if submitted:
            emp_num = create_applicant_info(applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, 
                                            emergency_name, emergency_tel_num, emergency_address, position_type, total_hours, 
                                            date_availability, school_name, school_address, school_tel_num, counselor_name, 
                                            grade_completed, GWA, graduated, enrolled)
    
            for emp in st.session_state.employment_history:
                if emp['company_name']: 
                    create_employment_history(emp_num, emp['company_name'], emp['company_address'], emp['company_tel_num'], 
                                              emp['position'], emp['supervisor'], emp['date_worked_from'], emp['date_worked_to'], 
                                              emp['wage'], emp['mgnt_ref_ck'], emp['reason_for_leaving'], emp['permission'])
    
            for ref in st.session_state.references:
                if ref['ref_name']: 
                    create_reference(emp_num, ref['ref_name'], ref['ref_tel_num'], ref['years_known'], ref['ref_address'])
    
            st.success("Application submitted successfully!")

if __name__ == "__main__":
    new_application()
