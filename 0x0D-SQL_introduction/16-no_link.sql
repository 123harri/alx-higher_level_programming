-- Script to list records of the table second_table with names
-- List records with names, displaying score and name, ordered by descending score
SELECT score, name
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
