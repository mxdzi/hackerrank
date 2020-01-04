SELECT
    city, CHARACTER_LENGTH(city) AS len
FROM
    station
ORDER BY len, city
LIMIT 1;

SELECT
    city, CHARACTER_LENGTH(city) AS len
FROM
    station
ORDER BY len desc, city
LIMIT 1;
