-- SQLite
--#1 SIMPLE 
SELECT applicant_name, position_type
FROM applicant_info
WHERE age_verification = 'Yes' AND position_type = 'Full time'
ORDER BY applicant_name;

--#2 SIMPLE
SELECT applicant_name, graduated
FROM applicant_info
WHERE graduated = 'Yes'
ORDER BY applicant_name;

--#3 SIMPLE
SELECT applicant_name, date_availability
FROM applicant_info
WHERE (position_type = 'Full time' AND GWA > 2.0) OR enrolled = 'Yes'
ORDER BY date_availability DESC;

--#4 SIMPLE
SELECT applicant_name, school_name, position_type
FROM applicant_info
WHERE school_name LIKE '%Ateneo%' AND (graduated = 'Yes' OR enrolled = 'Yes') AND age_verification = 'Yes';

--#1 MODERATE
SELECT ref_name
FROM reference
WHERE (years_known >= 5 AND ref_name LIKE 'Prof.%')
GROUP BY ref_name
ORDER BY ref_name;

--#2 MODERATE
SELECT company_name, SUM(wage)
FROM employment_history
GROUP BY company_name
HAVING SUM(wage) >= 20000 
ORDER BY SUM(wage);

--#3 MODERATE
SELECT company_name, COUNT(reason_for_leaving) as 'Migration Resignation'
FROM employment_history
WHERE reason_for_leaving = 'Migration'
GROUP BY company_name
HAVING COUNT(reason_for_leaving) = 1;

--#4 MODERATE
SELECT school_name, COUNT(emp_num) as 'Number of Full Time or Part Time Applicants'
FROM applicant_info
WHERE position_type IN ('Full Time', 'Part Time')
GROUP BY school_name
HAVING COUNT(emp_num) = 1
ORDER BY COUNT(emp_num) DESC;


--#1 DIFFICULT
SELECT a.applicant_name, COUNT(r.ref_name) AS num_referees
FROM applicant_info a, reference r
WHERE a.emp_num = r.emp_num
GROUP BY a.applicant_name
HAVING COUNT(r.ref_name) > 1;

--#2 DIFFICULT
SELECT e.company_name, COUNT(a.emp_num) AS 'Number of Applicants for Full Time Position'
FROM applicant_info a, employment_history e
WHERE a.emp_num = e.emp_num AND a.position_type = 'Full Time'
GROUP BY e.company_name
HAVING COUNT(a.emp_num) >= 1
ORDER BY COUNT(a.emp_num);

--#3 DIFFICULT
SELECT a.applicant_name, COUNT(e.company_name) AS 'Number of Companies'
FROM applicant_info a, employment_history e
WHERE a.emp_num = e.emp_num AND wage > 10000
GROUP BY a.applicant_name;

-- -- Insert dummy data into applicant_info
-- INSERT INTO applicant_info (applicant_name, tax_ID_num, applicant_address, applicant_tel_num, age_verification, emergency_name, emergency_tel_num, emergency_address, position_type, total_hours, date_availability, school_name, school_address, school_tel_num, counselor_name, grade_completed, GWA, graduated, enrolled)
-- VALUES
-- ('Juan Dela Cruz', '123456789', '1234 Mabini St, Manila', '09171234567', 'Yes', 'Maria Dela Cruz', '09181234567', '1234 Mabini St, Manila', 'Full Time', '40', '2024-07-01', 'University of the Philippines', 'Diliman, Quezon City', '9818500', 'Prof. Santos', 'College', 1.75, 'Yes', 'No'),
-- ('Maria Clara Reyes', '987654321', '5678 Luna St, Quezon City', '09187654321', 'Yes', 'Pedro Reyes', '09191234567', '5678 Luna St, Quezon City', 'Part Time', '20', '2024-07-05', 'Ateneo de Manila University', 'Katipunan Ave, Quezon City', '8426001', 'Prof. Reyes', 'College', 2.0, 'Yes', 'No'),
-- ('Jose Protacio Rizal', '456789123', '7890 Bonifacio St, Makati', '09194567890', 'Yes', 'Teodora Rizal', '09201234567', '7890 Bonifacio St, Makati', 'Seasonal', '30', '2024-07-10', 'De La Salle University', 'Taft Ave, Manila', '5244611', 'Prof. Dela Torre', 'College', 1.5, 'Yes', 'No'),
-- ('Andres Bonifacio', '321654987', '2345 Aguinaldo St, Pasig', '09193216549', 'Yes', 'Gregoria Bonifacio', '09211234567', '2345 Aguinaldo St, Pasig', 'Temporary', '25', '2024-07-15', 'Mapua University', 'Intramuros, Manila', '2475000', 'Prof. Cruz', 'College', 2.25, 'Yes', 'No'),
-- ('Emilio Aguinaldo', '654321987', '3456 Mabini St, Cavite', '09196543219', 'Yes', 'Hilaria Aguinaldo', '09221234567', '3456 Mabini St, Cavite', 'Full Time', '40', '2024-07-20', 'Polytechnic University of the Philippines', 'Sta. Mesa, Manila', '5330010', 'Prof. Garcia', 'College', 2.5, 'Yes', 'No');

-- -- Insert dummy data into employment_history
-- INSERT INTO employment_history (emp_num, company_name, company_address, company_tel_num, position, supervisor, date_worked_from, date_worked_to, wage, mgnt_ref_ck, reason_for_leaving, permission)
-- VALUES
-- (1, 'Company A', 'Ayala Ave, Makati', '028123456', 'Manager', 'Mr. Alberto Santos', '2020-01-01', '2022-12-31', 30000, 'Yes', 'Career Growth', 'Yes'),
-- (1, 'Company B', 'Ortigas Ave, Pasig', '028654321', 'Supervisor', 'Ms. Beatriz Reyes', '2018-01-01', '2019-12-31', 25000, 'Yes', 'Relocation', 'Yes'),
-- (2, 'Company C', 'BGC, Taguig', '027123456', 'Assistant', 'Mr. Carlos Mercado', '2019-01-01', '2021-12-31', 20000, 'Yes', 'Family Reasons', 'Yes'),
-- (2, 'Company D', 'Libis, Quezon City', '027654321', 'Clerk', 'Ms. Diana Hernandez', '2017-01-01', '2018-12-31', 15000, 'Yes', 'Personal Growth', 'Yes'),
-- (3, 'Company E', 'Eastwood, Quezon City', '025123456', 'Analyst', 'Mr. Edward Garcia', '2020-01-01', '2023-12-31', 35000, 'Yes', 'New Opportunities', 'Yes'),
-- (3, 'Company F', 'Makati Ave, Makati', '025654321', 'Specialist', 'Ms. Fiona Diaz', '2018-01-01', '2019-12-31', 30000, 'Yes', 'Higher Studies', 'Yes'),
-- (4, 'Company G', 'Alabang, Muntinlupa', '023123456', 'Engineer', 'Mr. George Cruz', '2021-01-01', '2023-12-31', 40000, 'Yes', 'Career Advancement', 'Yes'),
-- (4, 'Company H', 'Commonwealth, Quezon City', '023654321', 'Technician', 'Ms. Hannah Morales', '2019-01-01', '2020-12-31', 25000, 'Yes', 'Project End', 'Yes'),
-- (5, 'Company I', 'Mall of Asia, Pasay', '021123456', 'Consultant', 'Mr. Ian Gonzales', '2018-01-01', '2020-12-31', 50000, 'Yes', 'Career Change', 'Yes'),
-- (5, 'Company J', 'Greenhills, San Juan', '021654321', 'Advisor', 'Ms. Julia Romero', '2016-01-01', '2017-12-31', 45000, 'Yes', 'Family Relocation', 'Yes');

-- -- Insert dummy data into reference
-- INSERT INTO reference (emp_num, ref_name, ref_tel_num, years_known, ref_address)
-- VALUES
-- (1, 'Carlos Mercado', '09181234568', '5', 'Intramuros, Manila'),
-- (1, 'Luis Navarro', '09181234569', '3', 'Binondo, Manila'),
-- (2, 'Ana Ortega', '09191234568', '4', 'Marikina, Metro Manila'),
-- (2, 'Beth Perez', '09191234569', '6', 'Makati, Metro Manila'),
-- (3, 'Leo Quijano', '09194567891', '2', 'Taguig, Metro Manila'),
-- (3, 'Mike Rivera', '09194567892', '7', 'Mandaluyong, Metro Manila'),
-- (4, 'Nina Santos', '09193216550', '3', 'Pasig, Metro Manila'),
-- (4, 'Oscar Torres', '09193216551', '5', 'Antipolo, Rizal'),
-- (5, 'Patricia Ubaldo', '09196543220', '6', 'Las Pinas, Metro Manila'),
-- (5, 'Quinn Valencia', '09196543221', '8', 'Paranaque, Metro Manila');
