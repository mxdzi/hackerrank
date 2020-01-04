SELECT DISTINCT
    city
FROM
    station
WHERE
    INSTR(city, 'a') = 1
        OR INSTR(city, 'e') = 1
        OR INSTR(city, 'i') = 1
        OR INSTR(city, 'o') = 1
        OR INSTR(city, 'u') = 1;
