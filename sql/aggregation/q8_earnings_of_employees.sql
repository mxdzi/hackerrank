SELECT
    months * salary AS max_salary, COUNT(*)
FROM
    employee
GROUP BY max_salary
ORDER BY max_salary DESC
LIMIT 1;
