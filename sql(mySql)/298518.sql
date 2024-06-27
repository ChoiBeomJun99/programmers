-- 코드를 작성해주세요
SELECT count(*) as 'FISH_COUNT' 
FROM fish_info f
WHERE f.fish_type in (SELECT n.fish_type
                      FROM fish_name_info n
                      WHERE n.fish_name in ('BASS', 'SNAPPER'));