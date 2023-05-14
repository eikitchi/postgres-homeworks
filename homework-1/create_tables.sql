-- SQL-команды для создания таблиц
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
 	first_name VARCHAR(100),
 	last_name VARCHAR(100),
	title VARCHAR(100),
 	birth_date DATE,
	notes text
);

CREATE TABLE customers (
 	customer_id VARCHAR(100) PRIMARY KEY,
 	company_name VARCHAR(100),
	contact_name VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
	customer_id VARCHAR(100),
	employee_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    order_date DATE,
    ship_city VARCHAR(100)
);
