-- 코드를 작성해주세요
SELECT d.dept_id, d.dept_name_en, ROUND(AVG(e.sal)) AS 'AVG_SAL'
FROM hr_department d, hr_employees e
WHERE d.dept_id = e.dept_id
GROUP BY d.dept_id
ORDER BY 3 desc;
