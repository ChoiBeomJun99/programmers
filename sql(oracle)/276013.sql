-- 코드를 작성해주세요
# SELECT d.id, d.email, d.first_name, d.last_name
# FROM developer_infos d
# WHERE CONCAT(d.skill_1, d.skill_2, d.skill_3) like '%Python%'
# ORDER BY d.id;

SELECT d.id, d.email, d.first_name, d.last_name
  FROM developer_infos d
WHERE d.skill_1 = 'Python' 
   OR d.skill_2 = 'Python'
   OR d.skill_3 = 'Python'
ORDER BY d.id;