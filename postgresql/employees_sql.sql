SELECT * FROM public.employees;
SELECT * FROM public.salaries;

SELECT COUNT(DISTINCT birth_date) FROM public.employees; --4750

SELECT * FROM public.salaries
ORDER BY salary DESC, from_date ASC;

SELECT * FROM employees
WHERE first_name LIKE '%G%';

SELECT *, EXTRACT(YEAR FROM age(birth_date)) AS ages FROM employees
WHERE EXTRACT(YEAR FROM age(birth_date)) > 60;

SELECT * FROM public.employees AS e
INNER JOIN public.salaries AS s 
ON e.emp_no = s.emp_no;

-- Lesson 2 - Order By
SELECT * FROM public.employees
ORDER BY first_name ASC, last_name DESC;

SELECT * FROM public.employees
ORDER BY birth_date ASC;

SELECT * FROM public.employees
WHERE first_name LIKE 'K%'
ORDER BY hire_date ASC;

SELECT COUNT(*) FROM public.employees
WHERE first_name LIKE 'A%_r';

--comparisons
SELECT * FROM public.salaries;

--dates 
SELECT * FROM public.employees
WHERE EXTRACT(YEAR FROM AGE(birth_date)) > 60;


SELECT COUNT(*) FROM public.employees
WHERE EXTRACT(MONTH FROM hire_date) = 2;


SELECT COUNT(*) FROM public.employees
WHERE EXTRACT(MONTH FROM birth_date) = 11;

--joins
SELECT e.first_name, dp.dept_name FROM employees AS e
INNER JOIN dept_emp AS de ON de.emp_no = e.emp_no
INNER JOIN departments AS dp ON dp.dept_no = de.dept_no

SELECT * FROM employees AS e
INNER JOIN dept_emp AS de ON de.emp_no = e.emp_no
INNER JOIN departments AS dp ON dp.dept_no = de.dept_no
WHERE dp.dept_name = 'Development'

SELECT e.emp_no, e.first_name, e.last_name, s.salary FROM public.employees AS e 
INNER JOIN public.salaries AS s 
ON e.emp_no = s.emp_no;

SELECT first_name, last_name, salary FROM public.employees AS e 
INNER JOIN public.salaries AS s 
USING(emp_no);

SELECT hire_date, COUNT(*) FROM public.employees
GROUP BY hire_date
ORDER BY hire_date; 


SELECT hire_date, COUNT(*) FROM public.employees
GROUP BY hire_date
HAVING count(*) >= 10;

--SELECT *, avg(emp_no) over() from public.employees;
SELECT *, avg(salary) OVER(PARTITION BY emp_no, ORDER BY from_date) FROM public.salaries;

SELECT * FROM public.employees 
ORDER BY hire_date
LIMIT 10;


SELECT *, row_number() OVER(ORDER BY hire_date ASC) FROM public.employees;

SELECT * FROM (SELECT *, row_number() OVER(PARTITION BY dept_name, ORDER BY hire_date) FROM public.employees AS e
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no)
WHERE ordered >= 3;

--Lesson 4
--Group By
SELECT hire_date, COUNT(*) FROM public.employees
GROUP BY hire_date;

SELECT e.emp_no, COUNT(t.title) FROM public.employees AS e 
INNER JOIN public.titles AS t ON e.emp_no = t.emp_no
WHERE EXTRACT(YEAR FROM e.hire_date) > 1991
GROUP BY e.emp_no;

-- new task
SELECT EXTRACT(YEAR FROM hire_date) AS each_year, COUNT(*) FROM employees AS e 
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY each_year 

SELECT e.emp_no, e.first_name, d.dept_name FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales'
GROUP BY e.emp_no, d.dept_name;

-- new task
SELECT EXTRACT(MONTH FROM hire_date) AS each_month, COUNT(*) FROM employees AS e 
GROUP BY EXTRACT(MONTH FROM hire_date)
ORDER BY each_month 

--Having
SELECT e.emp_no FROM public.employees AS e 
INNER JOIN public.titles AS t ON e.emp_no = t.emp_no
WHERE EXTRACT(YEAR FROM e.hire_date) > 1991
GROUP BY e.emp_no
HAVING COUNT(DISTINCT t.title) >= 2;

SELECT e.emp_no, d.dept_name FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
INNER JOIN public.salaries AS s ON e.emp_no = s.emp_no
WHERE d.dept_name = 'Development'
GROUP BY e.emp_no, d.dept_name
HAVING COUNT(s.salary) > 15;

SELECT e.emp_no FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
GROUP BY e.emp_no
HAVING COUNT(DISTINCT d.dept_name) > 1;


--Grouping Sets
SELECT COUNT(e.emp_no) AS total_employees, d.dept_name FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
GROUP BY
    GROUPING SETS(
        (d.dept_name),
        ()
    );

SELECT AVG(s.salary) AS avg_salary, d.dept_name FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
INNER JOIN public.salaries AS s ON e.emp_no = s.emp_no
GROUP BY 
    GROUPING SETS(
        (d.dept_name),
        ()
    );

--Lesson 5 and 6
--Window functions
--Find the average income for each position
-- SELECT DISTINCT(t.title), AVG(s.salary) OVER(PARTITION BY t.title) AS avg_income FROM public.employees as e 
-- INNER JOIN public.salaries AS s on e.emp_no = s.emp_no 
-- INNER JOIN public.titles AS t ON s.emp_no = t.emp_no;

SELECT DISTINCT(titles.title), AVG(salaries.salary) OVER(PARTITION BY titles.title) AS avg_income FROM employees 
INNER JOIN titles USING(emp_no)
INNER JOIN salaries USING(emp_no)

--row_number()
--Find the first three hired employees for each department
SELECT emp_no, dept_name, row_number 
FROM (
    SELECT e.emp_no, d.dept_name, ROW_NUMBER() OVER(PARTITION BY d.dept_name ORDER BY e.hire_date) AS row_number FROM public.employees AS e 
    INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
    INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
) AS ranked_employees
WHERE row_number <= 3

SELECT *
FROM (
    SELECT *, dense_rank() OVER(PARTITION BY d.dept_name ORDER BY e.hire_date) AS ordered FROM public.employees AS e 
    INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
    INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
)
WHERE ordered <= 3;


--Find the 3 highest salaries for each position
-- SELECT salary, title, highest_salaries
-- FROM (
--     SELECT s.emp_no, s.salary, t.title, ROW_NUMBER() OVER(PARTITION BY t.title ORDER BY s.salary DESC) AS highest_salaries FROM public.salaries AS s 
--     INNER JOIN public.titles AS t ON s.emp_no = t.emp_no
-- ) AS ranked_employees
-- WHERE highest_salaries <= 3;

SELECT salary, title, highest_salaries
FROM (
    SELECT salaries.emp_no, salaries.salary, titles.title, ROW_NUMBER() OVER(PARTITION BY titles.title ORDER BY salaries.salary DESC) AS highest_salaries
    FROM salaries 
    INNER JOIN titles USING(emp_no)
) AS ranked_salaries
WHERE highest_salaries <= 3

SELECT *
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY t.title ORDER BY s.salary DESC) AS row_number FROM public.salaries    AS s 
    INNER JOIN public.titles AS t ON s.emp_no = t.emp_no
)
WHERE row_number <= 3;

SELECT *, LAG(salary, 2) OVER(PARTITION BY emp_no ORDER BY from_date) - salary FROM public.employees
INNER JOIN public.salaries USING(emp_no);

SELECT *, FIRST_VALUE(salary) OVER(PARTITION BY emp_no ORDER BY from_date) FROM public.employees
INNER JOIN public.salaries USING(emp_no);


SELECT *, LAST_VALUE(salary) OVER(PARTITION BY emp_no ORDER BY from_date RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED CURRENT ROW) FROM public.employees
INNER JOIN public.salaries USING(emp_no);

SELECT *, nth_value(salary, 1) OVER(PARTITION BY emp_no ORDER BY from_date RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED CURRENT ROW) FROM public.employees
INNER JOIN public.salaries USING(emp_no);


SELECT *, entail(5) OVER(ORDER BY hire_date) FROM employees;

--conditionals
SELECT *,
CASE 
    WHEN salary > 70000 THEN 'Rich'
    WHEN salary BETWEEN 60000 AND 70000 THEN 'Medium'
    ELSE 'Poor'
    END 
FROM employees
INNER JOIN salaries USING(emp_no);

-- 
-- SELECT *,
-- SUM(CASE 
--     WHEN salary > 70000 THEN 1
--     ELSE 0
--     END) 
-- FROM employees
-- INNER JOIN salaries USING(emp_no);


--new tasks
--How many employees were hired in each year?
SELECT COUNT(*) AS employees_count, EXTRACT(YEAR FROM hire_date) AS years FROM public.employees
GROUP BY EXTRACT(YEAR FROM hire_date);

--Count the number of employees who were hired each month
SELECT COUNT(*) AS employees_count, EXTRACT(MONTH FROM hire_date) AS months FROM public.employees
GROUP BY EXTRACT(MONTH FROM hire_date);

--Show me employees (emp_no) that have had more than 15 salary changes that work in the department development
SELECT emp_no, dept_name 
FROM (
    SELECT e.emp_no, d.dept_name, s.salary, LAG(s.salary) OVER(PARTITION BY e.emp_no ORDER BY s.from_date) AS prev_salary,
    CASE
        WHEN LAG(s.salary) OVER(PARTITION BY e.emp_no ORDER BY s.from_date) IS DISTINCT FROM s.salary THEN 1
        ELSE 0 
        END
    FROM public.employees AS e 
    INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
    INNER JOIN public.departments AS d ON de.dept_no = d.dept_no
    INNER JOIN public.salaries AS s ON s.emp_no = e.emp_no
    WHERE d.dept_name = 'Development'
) AS salary_changes
GROUP BY emp_no, dept_name 
HAVING COUNT(salary_changes) > 15;

--For each employee's title record, show the current title and the next title. If there is no next title, show NULL.
SELECT e.emp_no, t.title AS current_title, LEAD(t.title) OVER(PARTITION BY e.emp_no ORDER BY t.from_date) AS next_title FROM public.employees AS e 
INNER JOIN public.titles AS t ON e.emp_no = t.emp_no;

-- For each employee's department record, show the current department, the previous department, the next department, and the last recorded department for that employee
SELECT e.emp_no,
       d.dept_name AS current_dept,
       LAG(d.dept_name) OVER(PARTITION BY e.emp_no ORDER BY de.from_date) AS prev_dept,
       LEAD(d.dept_name) OVER(PARTITION BY e.emp_no ORDER BY de.from_date) AS next_dept,
       LAST_VALUE(d.dept_name) OVER(PARTITION BY e.emp_no ORDER BY de.from_date 
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_recorded_dept
FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no;

--For each employee, calculate the number of days between their hire date and the hire date of the previous employee based on the emp_no order. If there is no previous employee, show NULL
SELECT *, (hire_date - LAG(hire_date) OVER(ORDER BY emp_no)) AS day_counts FROM public.employees;

--Assign a dense rank to each employee's title based on the from_date within each employee. Additionally, mark the first title each employee received
SELECT e.emp_no, t.title, t.from_date,  
       DENSE_RANK() OVER(PARTITION BY e.emp_no ORDER BY t.from_date) AS employee_title_rank,
       FIRST_VALUE(t.title) OVER(PARTITION BY e.emp_no ORDER BY t.from_date) AS first_title
FROM public.employees AS e 
INNER JOIN public.titles AS t ON e.emp_no = t.emp_no;


--UNION
SELECT AVG(s.salary) AS avg_salary, d.dept_name FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no 
INNER JOIN public.salaries AS s ON s.emp_no = e.emp_no
GROUP BY d.dept_name

UNION ALL

SELECT AVG(s.salary) AS avg_salary, NULL FROM public.employees AS e 
INNER JOIN public.dept_emp AS de ON e.emp_no = de.emp_no
INNER JOIN public.departments AS d ON de.dept_no = d.dept_no 
INNER JOIN public.salaries AS s ON s.emp_no = e.emp_no;

--Views
CREATE TEMPORARY VIEW "90-95" AS
SELECT * 
FROM public.employees
WHERE EXTRACT(YEAR FROM hire_date) BETWEEN 1990 AND 1995;

SELECT * FROM "90-95"
ORDER BY HIRE_DATE ASC;


CREATE TEMPORARY VIEW "bigbucks" AS
SELECT e.emp_no, e.first_name, e.last_name, e.gender, s.salary
FROM public.employees AS e 
INNER JOIN public.salaries AS s ON e.emp_no = s.emp_no 
WHERE s.salary > 80000;

SELECT * FROM "bigbucks";

--Assign a sequential number to each employee based on their hire date within each gender. Additionally, mark whether the employee is in the --top half or bottom half of their gender group based on their hire date

--COUNT(*) / 2 calculates the midpoint based on gender
SELECT *,  ROW_NUMBER() OVER(PARTITION BY gender ORDER BY hire_date) AS employee_rank,
    CASE 
        WHEN ROW_NUMBER() OVER(PARTITION BY gender ORDER BY hire_date) <= (COUNT(*) OVER(PARTITION BY gender) / 2.0) THEN 'top half'
        ELSE 'bottom half'
    END AS half_type
FROM public.employees;

-- SELECT *, RANK() OVER(PARTITION BY gender ORDER BY hire_date) AS employee_rank, 
--         CASE 
--             WHEN RANK() OVER(PARTITION BY gender ORDER BY hire_date) < (SELECT COUNT(*) / 2 FROM public.employees) THEN 'top half'
--             ELSE 'bottom half'
--         END AS half_type
-- FROM public.employees;

--views
CREATE VIEW avg_emp AS 
(SELECT e.emp_no, AVG(s.salary) FROM public.employees AS e 
INNER JOIN public.salaries AS s ON e.emp_no = s.emp_no
GROUP BY e.emp_no);

SELECT * FROM public.avg_emp;
-- SELECT * FROM employees AS e 
-- WHERE e.emp_no IN(SELECT emp_no FROM salaries);


--common table expressions
WITH averages AS(
SELECT DISTINCT d.dept_name, t.title, AVG(s.salary) FROM employees AS e 
INNER JOIN salaries AS e ON s.emp_no = e.emp_no 
INNER JOIN titles AS t ON t.emp_no = s.emp_no 
INNER JOIN dept_emp AS de ON de.emp_no = e.emp_no 
INNER JOIN departments AS d ON d.dept_no = e.emp_no
GROUP BY
    GROUPING SETS (
        (d.dept_name),
        (t.title),
        ()
    )
)

SELECT * FROM averages;

SELECT concat(first_name, ' ', last_name) AS full_name, salary FROM 
(SELECT *, ROW_NUMBER() OVER(PARTITION BY e.emp_no ORDER BY s.from_date) AS gulnara FROM employees AS e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no) 
WHERE gulnara = 1;

-- Interview Questions
-- Find the first salary of each employees 
WITH subquery AS(
    SELECT 
        emp_no, 
        FIRST_VALUE(salary) OVER(PARTITION BY emp_no ORDER BY from_date ASC) AS first_salary,
        ROW_NUMBER() OVER(PARTITION BY emp_no ORDER BY from_date ASC) AS rn
    FROM public.salaries
)

SELECT sq.emp_no, sq.first_salary
FROM subquery AS sq
INNER JOIN public.employees AS e 
ON sq.emp_no = e.emp_no
WHERE sq.rn = 1;






























