-- 1251. Average Selling Price
-- Write your MySQL query statement below
select p.product_id, ROUND(SUM(u.units * p.price)/SUM(u.units),2) as average_price
from UnitsSold u
left join Prices p 
on u.product_id = p.product_id 
and u.purchase_date >= p.start_date
and u.purchase_date <= p.end_date
group by p.product_id;
