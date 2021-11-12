# Write your MySQL query statement below

select Email from (
    select email as Email, count(*) as total
    from Person
    group by email
) as t
where total > 1;