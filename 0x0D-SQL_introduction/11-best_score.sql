-- Script to list records with score >= 10 in the table second_table
-- List records with score >= 10 ordered by score (top first)
SELECT score, name
FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;