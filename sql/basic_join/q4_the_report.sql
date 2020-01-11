SELECT
    IF(grade >= 8, `name`, NULL), grade, marks
FROM
    students
        JOIN
    grades ON students.marks >= grades.min_mark
        AND students.marks <= grades.max_mark
ORDER BY grade DESC , `name` ASC;
