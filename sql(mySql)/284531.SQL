# -- 코드를 작성해주세요
SELECT s.route AS 'ROUTE', 
CONCAT(ROUND(SUM(d_between_dist), 1),'km') AS 'TOTAL_DISTANCE', 
CONCAT(ROUND(AVG(d_between_dist), 2), 'km') AS 'AVERAGE_DISTANCE'
FROM subway_distance s
GROUP BY s.route
ORDER BY SUM(d_between_dist) DESC;