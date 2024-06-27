-- 코드를 작성해주세요
SELECT f.id, f.length
FROM fish_info f
WHERE f.length IS NOT NULL
ORDER BY f.length DESC, f.id
LIMIT 10;