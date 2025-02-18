CREATE DATABASE CompanyDB;

DROP DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    manager_id INT NULL
);

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    order_date DATETIME,
    total_amount DECIMAL(10, 2)
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date, manager_id)
VALUES 
('John', 'Doe', 'IT', 55000, '2020-01-15', NULL),
('John', 'Doe', 'IT', 55000, '2020-01-15', NULL),
('Jane', 'Smith', 'Finance', 60000, '2019-03-10', 1),
('Alice', 'Johnson', 'HR', 45000, '2021-07-01', 2),
('Bob', 'Brown', 'IT', 50000, '2018-11-20', 1);

INSERT INTO departments (department_name)
VALUES 
('IT'),
('Finance'),
('HR'),
('Marketing');

INSERT INTO projects (project_name, start_date, end_date, budget)
VALUES 
('Website Redesign', '2023-01-01', '2023-06-30', 100000),
('ERP Implementation', '2022-04-01', '2023-03-31', 250000),
('Recruitment Drive', '2023-08-01', NULL, 50000);

INSERT INTO orders (customer_name, order_date, total_amount)
VALUES 
('Michael Johnson', '2023-10-15 14:30:00', 150.50),
('Emily Davis', '2023-10-20 16:00:00', 75.00),
('Christopher Lee', '2023-10-22 10:15:00', 220.75);

/* agregate */

SELECT SUM(salary) AS total_salary FROM employees;

SELECT department, AVG(salary) AS average_salary 
FROM employees 
GROUP BY department;

SELECT department, COUNT(employee_id) AS total_employees 
FROM employees 
GROUP BY department;

SELECT MIN(salary) AS lowest_salary, MAX(salary) AS highest_salary 
FROM employees;

/* group by */

SELECT department FROM employees;

SELECT department
FROM employees
GROUP BY department;

SELECT first_name, last_name
FROM employees
GROUP BY first_name, last_name;

/* GROUP BY & AGGREGATE */

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT department, COUNT(employee_id) AS total_employees, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT department, SUM(salary) AS average_salary 
FROM employees 
WHERE department = 'IT';

/* INNER JOIN */ 

SELECT department_name, first_name
FROM departments
INNER JOIN employees
ON 

















