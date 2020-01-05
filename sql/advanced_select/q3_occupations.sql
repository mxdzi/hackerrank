set @row1=0, @row2=0, @row3=0, @row4=0;
SELECT
    MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM
    (SELECT
        CASE
                WHEN occupation = 'Doctor' THEN (@row1:=@row1 + 1)
                WHEN occupation = 'Professor' THEN (@row2:=@row2 + 1)
                WHEN occupation = 'Singer' THEN (@row3:=@row3 + 1)
                WHEN occupation = 'Actor' THEN (@row4:=@row4 + 1)
            END AS `row`,
            CASE
                WHEN occupation = 'Doctor' THEN `name`
            END AS Doctor,
            CASE
                WHEN occupation = 'Professor' THEN `name`
            END AS Professor,
            CASE
                WHEN occupation = 'Singer' THEN `name`
            END AS Singer,
            CASE
                WHEN occupation = 'Actor' THEN `name`
            END AS Actor
    FROM
        occupations
    ORDER BY `name`) tmp
GROUP BY `row`
