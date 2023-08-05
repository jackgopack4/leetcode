-- 197. Rising Temperature
-- Write your MySQL query statement below
select w2.id from Weather w2 inner join Weather w1 on 
  DATEDIFF(w2.recordDate,w1.recordDate) = 1 and w2.temperature > w1.temperature;
