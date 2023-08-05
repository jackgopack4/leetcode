-- 1934. Confirmation Rate
-- Write your MySQL query statement below
select s.user_id, round(
    SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)/
    COUNT(*),
    2) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id
