-- 코드를 작성해주세요
SELECT r.item_id, r.item_name, r.rarity
FROM  item_info AS r
WHERE r.item_id IN (SELECT t.item_id
                    FROM item_info i JOIN item_tree t on i.item_id = t.parent_item_id
                    WHERE i.rarity = 'RARE')
ORDER BY 1 desc;