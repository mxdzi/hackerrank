SELECT
    (SELECT
            COUNT(city)
        FROM
            station) - (SELECT
            COUNT(city)
        FROM
            (SELECT DISTINCT
                city
            FROM
                station) as d);
