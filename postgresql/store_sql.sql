SELECT * FROM public.customers;
SELECT COUNT(customerid) FROM public.customers
WHERE gender = 'F' OR state = 'Oregon'; --10010


SELECT * FROM public.customers
WHERE age > 44 AND income >= 100000;


SELECT * FROM public.customers
WHERE age BETWEEN 30 AND 50 AND income < 50000;


SELECT AVG(income) FROM public.customers
WHERE age BETWEEN 21 AND 49; --59409.926240780098


SELECT * FROM public.orders;
SELECT COUNT(*) FROM public.orders
WHERE customerid IN(7888, 1082, 12808, 9623); --6


SELECT * FROM public.customers
WHERE (age BETWEEN 30 AND 50) AND income < 50000;


SELECT AVG(income) FROM public.customers
WHERE age BETWEEN 20 AND 50; --59361.925908612832

--Lesson 2
SELECT COUNT(*) FROM public.customers
WHERE CAST(zip AS TEXT) LIKE '2_1%';

SELECT COUNT(*) FROM public.customers
WHERE CAST(zip AS TEXT) LIKE '%2%';

--comparisons
SELECT * FROM public.customers
WHERE (age < 30 OR age > 50) AND (income > 50000) AND country IN('Japan', 'Australia', 'US');

--dates
SELECT COUNT(*) FROM public.orders
WHERE EXTRACT(YEAR FROM orderdate) = 2024 AND (EXTRACT(MONTH FROM orderdate) = 1);

--joins
SELECT * FROM public.orders AS o 
LEFT JOIN public.customers AS c 
ON o.customerid = c.customerid
WHERE c.state IN('OH', 'NY', 'OR'); 


SELECT * FROM public.products AS p 
RIGHT JOIN public.inventory AS i 
ON p.prod_id = i.prod_id; 

--row_number()
--Find the average price for each category and then subtract the item’s price from its category’s price 
SELECT *, AVG(price), price - OVER(PARTITION BY category) AS avg_price AS price_difference
FROM public.products;

--Find the most expensive product for each category
SELECT category, price, most_expensive_product 
FROM (
    SELECT c.category, p.price, ROW_NUMBER() OVER(PARTITION BY c.category ORDER BY p.price DESC) AS most_expensive_product 
    FROM public.categories AS c
    INNER JOIN public.products AS p ON c.category = p.category
)
WHERE most_expensive_product = 1;

--Find the most expensive product for each category
SELECT * 
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY c.category ORDER BY p.price DESC) AS most_expensive_product 
    FROM public.categories AS c
    INNER JOIN public.products AS p ON c.category = p.category
)
WHERE most_expensive_product <= 1;

--conditionals
SELECT prod_id, 
(CASE
    WHEN price > 20 THEN 'expensive'
    WHEN price BETWEEN 10 AND 20 THEN 'average'
    ELSE 'cheap'
    END) AS price_class
FROM public.products;

--Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state
SELECT * FROM public.orders AS o 
INNER JOIN public.customers AS c ON o.customerid = c.customerid
WHERE c.state IN('OH', 'NY', 'OR');
