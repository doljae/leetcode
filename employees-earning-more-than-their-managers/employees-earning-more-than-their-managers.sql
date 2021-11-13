select name as Employee
from Employee a 
where salary > (select salary from Employee where id = a.managerid);