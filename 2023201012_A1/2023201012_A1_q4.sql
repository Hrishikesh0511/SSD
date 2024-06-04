--create database q4;
--use q4;
SELECT e.emp_no,e.emp_joining_date,emp_salary,courses_completed,certificates_completed FROM Employee e
LEFT JOIN (
    SELECT emp_no, COUNT(*) AS courses_completed
    FROM CourseCompletions
    GROUP BY emp_no
) cc ON e.emp_no = cc.emp_no
LEFT JOIN (
    SELECT emp_no, COUNT(*) AS certificates_completed
    FROM CertificateCompletions
    GROUP BY emp_no
) cert ON e.emp_no = cert.emp_no;
