SET @row = 0;

SELECT
    ROUND(AVG(lat_n), 4)
FROM
    (SELECT
        (@row:=@row + 1) AS `row`, lat_n
    FROM
        station
    ORDER BY lat_n) tmp
WHERE
    `row` = (SELECT
            CEIL(COUNT(*) / 2)
        FROM
            station)
        OR `row` = (SELECT
            FLOOR((COUNT(*) / 2) + 1)
        FROM
            station);
