-- 1661. Average Time of Process per Machine
-- Write your MySQL query statement below
select Activity.machine_id, ROUND(SUM(e.timestamp - Activity.timestamp)/COUNT(Activity.process_id),3) as processing_time 
from Activity 
inner join Activity e 
    on Activity.machine_id = e.machine_id 
    and Activity.process_id = e.process_id 
    and Activity.activity_type = 'start'
    and e.activity_type = 'end'
group by machine_id;
