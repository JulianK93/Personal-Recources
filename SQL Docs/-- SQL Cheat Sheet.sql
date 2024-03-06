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
    lastName, 
    firstName, 
    jobTitle
FROM
    employees;

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

ORDER BY
   column1,
   column2;

-- FIELD() FUNCTION

