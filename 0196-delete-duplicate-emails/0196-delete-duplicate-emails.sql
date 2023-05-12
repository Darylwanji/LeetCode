# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE P
FROM Person P, Person Q
WHERE P.id > Q.id and P.email = Q.email;

