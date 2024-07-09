# db_functions
import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect("subwaydb.db")

def create_tables():
    creating_db = [
        "PRAGMA foreign_keys = off;",
        "BEGIN TRANSACTION;",
        """
            CREATE TABLE IF NOT EXISTS applicant_info (
                emp_num INTEGER PRIMARY KEY AUTOINCREMENT,
                applicant_name TEXT NOT NULL,
                tax_ID_num INTEGER NOT NULL,
                applicant_address TEXT NOT NULL,
                applicant_tel_num INTEGER NOT NULL,
                age_verification TEXT CHECK(age_verification IN ('Yes', 'No')) NOT NULL,
                emergency_name TEXT,
                emergency_tel_num INTEGER,
                emergency_address TEXT,
                position_type TEXT CHECK(position_type IN ('Part Time', 'Full Time', 'Seasonal', 'Temporary')),
                total_hours INTEGER,
                date_availability DATE NOT NULL,
                school_name TEXT,
                school_address TEXT,
                school_tel_num INTEGER,
                counselor_name TEXT,
                grade_completed TEXT CHECK(grade_completed IN ('Elementary', 'Junior High School', 'Senior High School', 'College')),
                GWA REAL,
                graduated TEXT CHECK(graduated IN ('Yes', 'No')) NOT NULL,
                enrolled TEXT CHECK(enrolled IN ('Yes', 'No')) NOT NULL
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS employment_history (
                history_code INTEGER PRIMARY KEY AUTOINCREMENT,
                emp_num INTEGER NOT NULL,
                company_name TEXT,
                company_address TEXT,
                company_tel_num INTEGER,
                position TEXT,
                supervisor TEXT,
                date_worked_from DATE,
                date_worked_to DATE,
                wage INTEGER,
                mgnt_ref_ck TEXT,
                reason_for_leaving TEXT,
                permission TEXT CHECK(permission IN ('Yes', 'No')),
                FOREIGN KEY(emp_num) REFERENCES applicant_info(emp_num)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS reference (
                ref_code INTEGER PRIMARY KEY AUTOINCREMENT,
                emp_num INTEGER NOT NULL,
                ref_name TEXT,
                ref_tel_num INTEGER,
                years_known INTEGER,
                ref_address TEXT,
                FOREIGN KEY(emp_num) REFERENCES applicant_info(emp_num)
            );
        """,
        "COMMIT TRANSACTION;",
        "PRAGMA foreign_keys = on;"
    ]

    # Connect to the database
    with connect_db() as conn:
        cursor = conn.cursor()
        for statement in creating_db:
            cursor.execute(statement)

def create_applicant_info(applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, 
                          emergency_name, emergency_tel_num, emergency_address, position_type, total_hours, 
                          date_availability, school_name, school_address, school_tel_num, counselor_name, 
                          grade_completed, GWA, graduated, enrolled):
    query = """
        INSERT INTO applicant_info (applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, 
                                    emergency_name, emergency_tel_num, emergency_address, position_type, total_hours, 
                                    date_availability, school_name, school_address, school_tel_num, counselor_name, 
                                    grade_completed, GWA, graduated, enrolled)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    values = (applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, emergency_name, 
              emergency_tel_num, emergency_address, position_type, total_hours, date_availability, school_name, 
              school_address, school_tel_num, counselor_name, grade_completed, GWA, graduated, enrolled)
    
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid  # Return the emp_num of the newly inserted applicant

def create_employment_history(emp_num, company_name, company_address, company_tel_num, position, supervisor, 
                              date_worked_from, date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission):
    query = """
        INSERT INTO employment_history (emp_num, company_name, company_address, company_tel_num, position, supervisor, 
                                        date_worked_from, date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    values = (emp_num, company_name, company_address, company_tel_num, position, supervisor, date_worked_from, 
              date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission)
    
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

def create_reference(emp_num, ref_name, ref_tel_num, years_known, ref_address):
    query = """
        INSERT INTO reference (emp_num, ref_name, ref_tel_num, years_known, ref_address)
        VALUES (?, ?, ?, ?, ?);
    """
    values = (emp_num, ref_name, ref_tel_num, years_known, ref_address)
    
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

def get_last_inserted_id():
    with connect_db() as conn:
        cursor = conn.execute("SELECT last_insert_rowid()")
        last_id = cursor.fetchone()
        return last_id[0] if last_id else None

def get_all_applicant_info():
    with connect_db() as conn:
        cursor = conn.execute("SELECT * FROM applicant_info")
        data = cursor.fetchall()
        return data
    
def get_all_employment_history():
    with connect_db() as conn:
        cursor = conn.execute("SELECT * FROM employment_history")
        data = cursor.fetchall()
        return data
        
def get_all_references():
    with connect_db() as conn:
        cursor = conn.execute("SELECT * FROM reference")
        data = cursor.fetchall()
        return data

def insert_applicant_info(*args):
    query = """
    INSERT INTO applicant_info (
        applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, emergency_name, emergency_tel_num, emergency_address, position_type, total_hours, date_availability, school_name, school_address, school_tel_num, counselor_name, grade_completed, GWA, graduated, enrolled)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def insert_employment_history(*args):
    query = """
    INSERT INTO employment_history (
        emp_num, company_name, company_address, company_tel_num, position, supervisor, date_worked_from, date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def insert_reference(*args):
    query = """
    INSERT INTO reference (
        emp_num, ref_name, ref_tel_num, years_known, ref_address)
    VALUES (?, ?, ?, ?, ?)
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def get_applicant_info_by_emp_num(emp_num):
    query = "SELECT * FROM applicant_info WHERE emp_num = ?"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (emp_num,))
    result = cursor.fetchone()
    conn.close()
    if result:
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, result))
    return None

def get_employment_history_by_emp_num(emp_num):
    query = "SELECT * FROM employment_history WHERE emp_num = ?"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (emp_num,))
    result = cursor.fetchall()
    conn.close()
    if result:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in result]
    return []

def get_references_by_emp_num(emp_num):
    query = "SELECT * FROM reference WHERE emp_num = ?"
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (emp_num,))
    result = cursor.fetchall()
    conn.close()
    if result:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in result]
    return []

def update_applicant_info(emp_num, applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification,
                          emergency_name, emergency_tel_num, emergency_address, position_type, total_hours,
                          date_availability, school_name, school_address, school_tel_num, counselor_name,
                          grade_completed, GWA, graduated, enrolled):
    query = """
    UPDATE applicant_info SET
        applicant_name = ?, tax_ID_num = ?, applicant_address = ?, applicant_tel_num = ?, age_verification = ?,
        emergency_name = ?, emergency_tel_num = ?, emergency_address = ?, position_type = ?, total_hours = ?,
        date_availability = ?, school_name = ?, school_address = ?, school_tel_num = ?, counselor_name = ?,
        grade_completed = ?, GWA = ?, graduated = ?, enrolled = ?
    WHERE emp_num = ?
    """
    values = (applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, emergency_name,
              emergency_tel_num, emergency_address, position_type, total_hours, date_availability, school_name,
              school_address, school_tel_num, counselor_name, grade_completed, GWA, graduated, enrolled, emp_num)
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

def update_employment_history(history_code, emp_num, company_name, company_address, company_tel_num, position, supervisor,
                              date_worked_from, date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission):
    query = """
    UPDATE employment_history SET
        company_name = ?, company_address = ?, company_tel_num = ?, position = ?, supervisor = ?,
        date_worked_from = ?, date_worked_to = ?, wage = ?, mgnt_ref_ck = ?, reason_for_leaving = ?, permission = ?
    WHERE history_code = ? AND emp_num = ?
    """
    values = (company_name, company_address, company_tel_num, position, supervisor, date_worked_from,
              date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission, history_code, emp_num)
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

def update_reference(ref_code, emp_num, ref_name, ref_tel_num, years_known, ref_address):
    query = """
    UPDATE reference SET
        ref_name = ?, ref_tel_num = ?, years_known = ?, ref_address = ?
    WHERE ref_code = ? AND emp_num = ?
    """
    values = (ref_name, ref_tel_num, years_known, ref_address, ref_code, emp_num)
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

def delete_data(emp_num):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reference WHERE emp_num = ?", (emp_num,))
        cursor.execute("DELETE FROM employment_history WHERE emp_num = ?", (emp_num,))
        cursor.execute("DELETE FROM applicant_info WHERE emp_num = ?", (emp_num,))
        conn.commit()

if __name__ == "__main__":
    create_tables()