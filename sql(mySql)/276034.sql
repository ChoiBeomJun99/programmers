-- 코드를 작성해주세요
SELECT d.id, d.email, d.first_name, d.last_name
  FROM developers d
WHERE d.skill_code & (SELECT c.code
                      FROM skillcodes c
                      WHERE c.name = 'Python')

OR d.skill_code & (SELECT c.code
                   FROM skillcodes c
                   WHERE c.name = 'C#')
ORDER BY d.id;