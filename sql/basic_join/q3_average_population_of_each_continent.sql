SELECT
    country.continent,
    TRUNCATE(AVG(city.population), 0) AS avg_population
FROM
    city
        JOIN
    country ON city.countrycode = country.code
GROUP BY country.continent
ORDER BY avg_population;
