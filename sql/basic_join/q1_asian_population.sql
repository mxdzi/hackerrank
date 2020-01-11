SELECT
    SUM(city.population)
FROM
    city
        JOIN
    country ON city.countrycode = country.code
WHERE
    country.continent = 'Asia';
