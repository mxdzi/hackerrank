SELECT
    ROUND(AVG(salary)) - ROUND(AVG(REPLACE(salary, 0, '')))
FROM
    employees;
