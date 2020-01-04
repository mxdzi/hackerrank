SELECT DISTINCT
    city
FROM
    station
WHERE
    RIGHT(id, 1) % 2 = 0;
