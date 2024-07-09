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
    st.header("Employment Application Form", anchor = False)

    with st.form(key='new_application', clear_on_submit= True):
        st.subheader("*I. Personal Information*")
        applicant_name = st.text_input("**Full Name**", value=st.session_state.applicant_info['applicant_name'], key='applicant_name', placeholder="First Name, Middle Initial, Lastname")
        applicant_address = st.text_input("**Address**", value=st.session_state.applicant_info['applicant_address'], key='applicant_address', placeholder="Block No., Street Name, City")
        newcol1, newcol2, newcol3 = st.columns (3)
        with newcol1:
            tax_ID_num = st.number_input("**Tax ID Number**", value=st.session_state.applicant_info['tax_ID_num'], format="%d", key='tax_ID_num', placeholder="000-000-000-000")
        with newcol2:
            applicant_tel_num = st.number_input("**Cell/Telephone Number**", value=st.session_state.applicant_info['applicant_tel_num'], format="%d", key='applicant_tel_num', placeholder="00000000000")
        with newcol3:
            age_verification = st.radio("**Are You 16 years of age or over?**", ["Yes", "No"], index=0, horizontal =True if st.session_state.applicant_info['age_verification'] == "Yes" else 1, key='age_verification')
        st.divider()

        st.subheader("*II. In Case of Emergency, Notify*", anchor = False)
        emergency1, emergency2 = st.columns(2)
        with emergency1:
            emergency_name = st.text_input("**Emergency Contact Name**", value=st.session_state.applicant_info['emergency_name'], key='emergency_name', placeholder="Full Name")
        with emergency2:  
            emergency_tel_num = st.number_input("**Contact Number**", value=st.session_state.applicant_info['emergency_tel_num'], format="%d", key='emergency_tel_num', placeholder="00000000000")
        emergency_address = st.text_input("**Contact Address**", value=st.session_state.applicant_info['emergency_address'], key='emergency_address', placeholder="Block No., Street Name, City")
        st.divider()

        st.subheader("*III. Availability*", anchor = False)
        position_type = st.radio("**Position Type**", ["Part Time", "Full Time", "Seasonal", "Temporary"], index=["Part Time", "Full Time", "Seasonal", "Temporary"].index(st.session_state.applicant_info['position_type']), key='position_type', horizontal =True)
        av1, av2 = st.columns(2)
        with av1:
            total_hours = st.number_input("**Total Hours Available Per Week**", value=st.session_state.applicant_info['total_hours'], format="%d", key='total_hours')
        with av2:
            date_availability = st.date_input("**Date Available to Start Work**", value=st.session_state.applicant_info['date_availability'], key='date_availability')
        st.divider()

        st.subheader("*IV. School Most Recent Attended*", anchor = False)
        sch1, sch2 = st.columns(2)
        with sch1:
            school_name = st.text_input("**School**", value=st.session_state.applicant_info['school_name'], key='school_name', placeholder="School Name")
            school_tel_num = st.number_input("**School Telephone Number**", value=st.session_state.applicant_info['school_tel_num'], format="%d", key='school_tel_num', placeholder="00000000000")
        with sch2:
            school_address = st.text_input("**School Address**", value=st.session_state.applicant_info['school_address'], key='school_address', placeholder="Block No., Street Name, City")
            counselor_name = st.text_input("**Counselor Name**", value=st.session_state.applicant_info['counselor_name'], key='counselor_name', placeholder="Full Name")
        sch3, sch4, sch5, sch6 = st.columns(4)
        with sch3:
            grade_completed = st.radio("**Last Grade Completed**", ['Elementary', 'Junior High School', 'Senior High School', 'College'], index=['Elementary', 'Junior High School', 'Senior High School', 'College'].index(st.session_state.applicant_info['grade_completed']), horizontal=True, key='grade_completed')
        with sch4:
            GWA = st.number_input("**Most Recent GWA**", value=st.session_state.applicant_info['GWA'], key='GWA', placeholder="0.00")
        with sch5:
            graduated = st.radio("**Graduated?**", ["Yes", "No"], index=0 if st.session_state.applicant_info['graduated'] == "Yes" else 1, key='graduated', horizontal =True)
        with sch6:
            enrolled = st.radio("**Now Enrolled?**", ["Yes", "No"], index=0 if st.session_state.applicant_info['enrolled'] == "Yes" else 1, key='enrolled', horizontal =True)
        st.divider()

        st.subheader("*V. Most Recent Employment*", anchor = False)
        for i, emp in enumerate(st.session_state.employment_history):
            st.write(f"**Employment History** {i+1}")
            comp1, comp2 = st.columns(2)
            with comp1:
                emp['company_name'] = st.text_input(f"**Company**", value=emp['company_name'], key=f'company_name_{i+1}', placeholder="Company Name")
            with comp2:
                emp['company_address'] = st.text_input(f"**Company Address**", value=emp['company_address'], key=f'company_address_{i+1}', placeholder="Block No., Street Name, City")
            comp3, comp4, comp5 = st.columns(3)
            with comp3:
                emp['company_tel_num'] = st.number_input(f"**Company Telephone Number**", value=emp['company_tel_num'], key=f'company_tel_num_{i+1}', format="%d", placeholder="000000000")
            with comp4:
                emp['position'] = st.text_input(f"**Position**", value=emp['position'], key=f'position_{i+1}', placeholder="Type of Position")
            with comp5:
                emp['supervisor'] = st.text_input(f"**Supervisor**", value=emp['supervisor'], key=f'supervisor_{i+1}', placeholder="Full Name")
            comp6, comp7, comp8, comp9 = st.columns(4)
            with comp6:
                emp['date_worked_from'] = st.date_input(f"**Date Worked From**", value=emp['date_worked_from'], key=f'date_worked_from_{i+1}')
            with comp7:
                emp['date_worked_to'] = st.date_input(f"**Date Worked To**", value=emp['date_worked_to'], key=f'date_worked_to_{i+1}')
            with comp8:
                emp['wage'] = st.number_input(f"**Wage Per Month**", value=emp['wage'], key=f'wage_{i+1}', format="%d", placeholder="0.00")
            with comp9:
                emp['mgnt_ref_ck'] = st.text_input(f"**Management Reference Checked By**", value=emp['mgnt_ref_ck'], key=f'mgnt_ref_ck_{i+1}', placeholder="Full Name")
            emp['reason_for_leaving'] = st.text_input(f"**Reason for Leaving**", value=emp['reason_for_leaving'], key=f'reason_for_leaving_{i+1}')
            emp['permission'] = st.radio(f"**Do we have your permission to contact your previous employer?**", ['Yes', 'No'], index=0, horizontal =True if emp['permission'] == "Yes" else 1, key=f'permission_{i+1}')

        if st.form_submit_button("Add Employment History"):
            add_employment_history()

        st.subheader("*VI. References*", anchor = False)
        for j, ref in enumerate(st.session_state.references):
            st.write(f"**Reference Person {j+1}**")
            refe1, refe2 = st.columns(2)
            with refe1:
                ref['ref_name'] = st.text_input(f"**Reference Name**", value=ref['ref_name'], key=f'ref_name_{j+1}', placeholder="Full Name")
                ref['ref_tel_num'] = st.number_input(f"**Telephone Number**", value=ref['ref_tel_num'], key=f'ref_tel_num_{j+1}', format="%d", placeholder="0000 000 0000")
            with refe2:
                ref['ref_address'] = st.text_input(f"**Address**", value=ref['ref_address'], key=f'ref_address_{j+1}', placeholder="Block No., Street Name, City")
                ref['years_known'] = st.number_input(f"**Years Known**", value=ref['years_known'], key=f'years_known_{j+1}', placeholder="0")

        if st.form_submit_button("Add Reference Person"):
            add_reference()

        if st.form_submit_button('Submit'):
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
