-- SQL Cheat Sheet
-- Creating the DB
CREATE DATABASE your_database_name;
USE your_database_name;  -- Use your database
SOURCE /path/to/your/sql/file.sql;  -- Import SQL file
SHOW TABLES;

-- BASIC SELECT FUNCTIONS
SELECT * FROM tablename;
SELECT (column1, column2) FROM tablename;

SELECT 
   column1,
   column2
FROM
    tablename;

-- SELECT FUNCTIONS WITHOUT TABLE - MATH, STRING & DATE FUNCTIONS
SELECT 1+1;
SELECT NOW()
SELECT CONCAT('John',' ','Doe');
SELECT CONCAT('Jane',' ','Doe') AS 'Full name';
SELECT 
  quantityOrdered * priceEach AS subtotal 
FROM 
  orderdetails 

-- ORDERING RESULTS
SELECT 
   select_list
FROM 
   table_name
ORDER BY 
   column1 [ASC|DESC], 
   column2 [ASC|DESC],
   ...;

ORDER BY column1 ASC;  ==  ORDER BY column1;

-- FIELD() FUNCTION - SOrt by manual sort
SELECT 
  orderNumber, 
  status
FROM 
  orders
ORDER BY 
  FIELD(
    status, 
    'In Process', 
    'On Hold', 
    'Cancelled', 
    'Resolved', 
    'Disputed', 
    'Shipped'
  );

-- WHERE filter logic - BETWEEN, IN, LIKE, IS NOT NULL
SELECT 
    lastname, 
    firstname, 
    jobtitle,
    officeCode
FROM
    employees
WHERE
    jobtitle = 'Sales Rep' AND 
    officeCode = 1;
WHERE
    lastName LIKE '%son'
WHERE
    officeCode BETWEEN 1 AND 3
WHERE
    officeCode IN (1 , 2, 3)
WHERE
    sstate IS NOT NULL

-- SELECT DISTINCT -- unique lists, filter double data

SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY 
    state, 
    city;

SELECT
customerName AS name,
customerNumber AS number
FROM
customers;


