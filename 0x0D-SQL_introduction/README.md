# SQL - Introduction

This project encompasses a series of tasks aimed at honing skills in relational databases using SQL. The tasks include introductory exercises in SQL data definitions, manipulation language, subqueries, and functions.

## Overview

The project spans a variety of SQL tasks, covering essential concepts such as database creation, table creation, data insertion, retrieval, and analysis.

## Tasks :page_with_curl:

### 0. List Databases
* [0-list_databases.sql](./0-list_databases.sql): MySQL script listing all databases.

### 1. Create a Database
* [1-create_database.sql](./1-create_database.sql): MySQL script creating the database `hbtn_0c_0`.

### 2. Delete a Database
* [2-remove_databases.sql](./2-remove_databases.sql): MySQL script deleting the database `hbtn_0c_0`.

### 3. List Tables
* [3-list_tables.sql](./3-list_tables.sql): MySQL script listing all tables.

### 4. First Table
* [4-first_table.sql](./4-first_table.sql): MySQL script creating a table `first_table` with columns:
  * `id` (INT)
  * `name` (VARCHAR(256))

### 5. Full Description
* [5-full_table.sql](./5-full_table.sql): MySQL script printing the full description of the table `first_table`.

### 6. List All in Table
* [6-list_values.sql](./6-list_values.sql): MySQL script listing all rows of the table `first_table`.

### 7. First Add
* [7-insert_value.sql](./7-insert_value.sql): MySQL script inserting a new row in `first_table` with:
  * `id` = `89`
  * `name` = `Best School`

### 8. Count 89
* [8-count_89.sql](./8-count_89.sql): MySQL script displaying the number of records with `id = 89` in `first_table`.

### 9. Full Creation
* [9-full_creation.sql](./9-full_creation.sql): MySQL script creating and filling a table `second_table` with columns:
  * `id` (INT)
  * `name` (VARCHAR(256))
  * `score` (INT)
  Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

### 10. List by Best
* [10-top_score.sql](./10-top_score.sql): MySQL script listing the `score` and `name` of all records in `second_table` in descending order of `score`.

### 11. Select the Best
* [11-best_score.sql](./11-best_score.sql): MySQL script listing the `score` and `name` of records with `score >= 10` in `second_table` in descending order of score.

### 12. Cheating is Bad
* [12-no_cheating.sql](./12-no_cheating.sql): MySQL script updating the score of Bob to 10 in `second_table`.

### 13. Score Too Low
* [13-change_class.sql](./13-change_class.sql): MySQL script removing records with `score <= 5` in `second_table`.

### 14. Average
* [14-average.sql](./14-average.sql): MySQL script computing the average `score` of all records in `second_table`.

### 15. Number by Score
* [15-groups.sql](./15-groups.sql): MySQL script listing the `score` and the number of records with the same score in `second_table` in descending order of count.

### 16. Say My Name
* [16-no_link.sql](./16-no_link.sql): MySQL script listing the `score` and `name` of all records in `second_table` in descending order of `score`. Does not display rows without a `name` value.

### 17. Go to UTF8
* [100-move_to_utf8.sql](./100-move_to_utf8.sql): MySQL script converting the `hbtn_0c_0` database to UTF8.

### 18. Temperatures #0
* [101-avg_temperatures.sql](./101-avg_temperatures.sql): MySQL script displaying the average temperature (Fahrenheit) by city in descending order.

### 19. Temperatures #1
* [102-top_city.sql](./102-top_city.sql): MySQL script displaying the three cities with the highest average temperature from July to August in descending order.

### 20. Temperature #2
* [103-max_state.sql](./103-max_state.sql): MySQL script displaying the max temperature of each state in order of state name.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- MySQL server
- Any other specific requirements...

## Dump File :dolphin:
* Tasks 101-103 queries from the database [temperatures.sql](./temperatures.sql).

