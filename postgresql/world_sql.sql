SELECT * FROM public.countrylanguage;

SELECT COUNT(DISTINCT LANGUAGE) FROM public.countrylanguage
WHERE isofficial = TRUE; --102


SELECT DISTINCT lifeexpectancy FROM public.country;

SELECT AVG(lifeexpectancy) FROM public.country; -- 66.486036


SELECT * FROM public.city;

SELECT AVG(population) FROM public.city
WHERE countrycode = 'NLD'; --185001.75


SELECT COUNT(NAME) FROM public.city
WHERE district IN('Zuid-Holland', ' Noord-Brabant', 'Utrecht'); --8


SELECT DISTINCT NAME FROM public.country
WHERE lifeexpectancy BETWEEN 20 AND 50; 


--joins
SELECT NAME, LANGUAGE FROM public.country AS c 
INNER JOIN public.countrylanguage AS cl
ON c.code = cl.countrycode;

--Find the percentage of the world's population that lives on each continent
SELECT DISTINCT continent, ROUND((SUM(population) OVER(PARTITION BY continent)::FLOAT / SUM(population) OVER()) * 100) || '%' AS percentage 
FROM public.country
GROUP BY continent, population;

--conditionals
SELECT 
SUM(CASE
    WHEN population > 50000000 THEN surfacearea
    ELSE surfacearea
    END)
FROM public.country;

