# sql_queries.py
import streamlit as st
import pandas as pd
import sqlite3

def execute_query(query):
    with sqlite3.connect("subwaydb.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
    return columns, data


def query1():
    query = """SELECT applicant_name, position_type 
               FROM applicant_info 
               WHERE age_verification = 'Yes' 
               AND position_type = 'Full Time' 
               ORDER BY applicant_name;"""
    return execute_query(query)

def query2():
    query = """SELECT applicant_name, date_availability 
        FROM applicant_info 
        WHERE (position_type = 'Full Time' 
        AND GWA > 2.0) OR enrolled = 'Yes' 
        ORDER BY date_availability DESC;"""
    return execute_query(query)

def query3():
    query = """SELECT applicant_name, school_name, position_type 
        FROM applicant_info 
        WHERE school_name LIKE '%Ateneo%' AND (graduated = 'Yes' OR enrolled = 'Yes') AND age_verification = 'Yes';"""
    return execute_query(query)

def query4():
    query = """SELECT ref_name 
        FROM reference 
        WHERE (years_known >= 5 AND ref_name LIKE 'Prof.%') 
        GROUP BY ref_name ORDER BY ref_name;"""
    return execute_query(query)

def query5():
    query = """SELECT company_name, SUM(wage) 
        FROM employment_history 
        GROUP BY company_name 
        HAVING SUM(wage) >= 20000 ORDER BY SUM(wage);"""
    return execute_query(query)

def query6():
    query = """SELECT company_name, COUNT(reason_for_leaving) as 'Migration Resignation' 
        FROM employment_history 
        WHERE reason_for_leaving = 'Migration' 
        GROUP BY company_name 
        HAVING COUNT(reason_for_leaving) >= 1;"""
    return execute_query(query)

def query7():
    query = """SELECT school_name, COUNT(emp_num) as 'Number of Full Time or Part Time Applicants'
        FROM applicant_info
        WHERE position_type IN ('Full Time', 'Part Time')
        GROUP BY school_name
        HAVING COUNT(emp_num) = 1
        ORDER BY COUNT(emp_num) DESC;"""
    return execute_query(query)

def query8():
    query = """SELECT a.applicant_name, COUNT(r.ref_name) AS num_referees 
        FROM applicant_info a, reference r 
        WHERE a.emp_num = r.emp_num 
        GROUP BY a.applicant_name 
        HAVING COUNT(r.ref_name) > 1;"""
    return execute_query(query)

def query9():
    query = """SELECT e.company_name, COUNT(a.emp_num) AS 'Number of Applicants for Full Time Position' 
        FROM applicant_info a, employment_history e 
        WHERE a.emp_num = e.emp_num AND a.position_type = 'Full Time' GROUP BY e.company_name 
        HAVING COUNT(a.emp_num) >= 1 
        ORDER BY COUNT(a.emp_num);"""
    return execute_query(query)

def query10():
    query = """SELECT a.applicant_name, COUNT(e.company_name) AS 'Number of Companies' 
        FROM applicant_info a, employment_history e 
        WHERE a.emp_num = e.emp_num AND e.wage > 10000 
        GROUP BY a.applicant_name
        ORDER BY COUNT(e.company_name) DESC;"""
    return execute_query(query)

def sql_queries():
    st.title("SQL Queries", anchor = False)
    
    st.subheader("Simple", anchor = False)

    st.write(" Display the names and positions of applicants who are qualified for the age verification and are applying for full-time positions. Sort the results by the applicant's name")
    if st.button("Query 1"):
        columns, data = query1()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.write("Display the names and availability date of applicants who are available for full-time positions and have a Grade Weighted Average (GWA) greater than 2.0 or are currently enrolled. Sort the results by the earliest availability date.")
    if st.button("Query 2"):
        columns, data = query2()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)
        
    st.write("According to the existing list of applicants, look for applicants who are currently studying or graduated from the school Ateneo then from this data display the name of the applicant, school name, and the position type he/she is currently applying for, only if he/she passed or qualified for the age verification.")
    if st.button("Query 3"):
        columns, data = query3()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.subheader("Moderate", anchor = False)

    st.write("Provide the names of referees or character witnesses who have known the applicants for at least 5 years and are considered as professors. Arrange the results orderly by their names.")
    if st.button("Query 4"):
        columns, data = query4()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.write("Compute the total wage offer for each company and display the total wage as well as the names of the companies who have a total wage offer that is greater than or equal to 20,000 based on the current list of employees present. Arrange the result according to the total wage offer.")
    if st.button("Query 5"):
        columns, data = query5()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)
    
    st.write("Based on the employment history of all the applicants, look for the companies that received a resignation letter from their employees that says migration and display only those companies that received this kind of reason for leaving equal to 1.")
    if st.button("Query 6"):
        columns, data = query6()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)
    
    st.write("From the existing applicant records, count all the applicants for each of the schools present who are applying for a full-time or part-time position. Display the name of the school along with the count of applicants. Include only those schools who have a count equal to or greater than 1. Arranged the result according to the number of applicants in a manner that is dropping.")
    if st.button("Query 7"):
        columns, data = query7()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.subheader("Difficult", anchor = False)

    st.write("Provide the names of referees or character witnesses who have known the applicant for at least 5 years and are considered as professors. Arrange the results orderly by their names.")
    if st.button("Query 8"):
        columns, data = query8()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.write("Based on the existing records of applicants, count the number of applicants from each existing company based on their employment history who are applying for a full-time position for Subway. Display only the name of the company and the number of applicants if the number of applicants is equal to or greater than 1. Arrange the result based on the number of applicants increasingly.")
    if st.button("Query 9"):
        columns, data = query9()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)

    st.write("Display the applicant's name along with the count of the companies that gave them a wage greater than 10,000 PHP. Arrange the result from the highest to the lowest amount of companies they are in.")
    if st.button("Query 10"):
        columns, data = query10()
        st.dataframe(pd.DataFrame(data, columns = columns), hide_index = True)