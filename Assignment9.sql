CREATE TABLE Product (
    id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

INSERT INTO Product (id, product_name, category, price) VALUES
(1, 'Laptop', 'Electronics', 899.99),
(2, 'Smartphone', 'Electronics', 699.99),
(3, 'Coffee Maker', 'Kitchen', 79.99),
(4, 'Running Shoes', 'Footwear', 129.99),
(5, 'Headphones', 'Electronics', 149.99);

CREATE TABLE Sales (
    id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);

INSERT INTO Sales (id, product_id, quantity_sold, sale_date, total_price) VALUES
(1, 1, 2, '2023-10-15', 1799.98),
(2, 3, 1, '2023-10-16', 79.99),
(3, 2, 3, '2023-10-17', 2099.97),
(4, 5, 2, '2023-10-18', 299.98),
(5, 4, 1, '2023-10-19', 129.99);

SELECT * FROM Product;

SELECT product_name, price FROM Product;

SELECT * FROM Sales LIMIT 2;

SELECT * FROM Sales WHERE total_price > 100;

SELECT category, COUNT(*) as count 
FROM Product 
GROUP BY category 
HAVING COUNT(*) > 1;

SELECT COUNT(*) as total_products FROM Product;

SELECT SUM(total_price) as total_sales FROM Sales;

SELECT AVG(price) as average_price FROM Product; 