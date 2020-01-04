SELECT DISTINCT
    city
FROM
    station
WHERE
    SUBSTRING(city, CHAR_LENGTH(city), 1) IN ('a', 'e', 'i', 'o', 'u');
