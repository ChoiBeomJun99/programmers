-- 코드를 작성해주세요
SELECT SUM(g.score) AS 'SCORE', e.emp_no, e.emp_name, e.position, e.email
FROM hr_employees e, hr_grade g
WHERE 1=1
AND e.emp_no = g.emp_no
AND g.year = 2022
GROUP BY e.emp_no
ORDER BY 1 DESC
LIMIT 1;