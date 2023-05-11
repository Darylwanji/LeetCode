# Write your MySQL query statement below
SELECT name as Employee
FROM Employee P
WHERE P.salary > ( SELECT salary 
               FROM Employee Q
               WHERE Q.id = P.managerId)