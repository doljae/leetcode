# Write your MySQL query statement below

select t.employee_id from (select * from Employees left join Salaries using (employee_id)
union
select * from Employees right join Salaries using (employee_id)) as t
where name is null or salary is null
order by t.employee_id asc;