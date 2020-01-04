SELECT DISTINCT
    city
FROM
    station
WHERE
    RIGHT(city, 1) NOT IN ('a' , 'e', 'i', 'o', 'u');
