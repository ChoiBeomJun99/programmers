-- 코드를 작성해주세요
SELECT i.id, n.fish_name, i.length
FROM fish_info i JOIN fish_name_info n ON i.fish_type = n.fish_type
WHERE (i.fish_type, i.length) in (SELECT fish_type, MAX(length)
                                  FROM fish_info 
                                  group by fish_type)
ORDER BY i.id;