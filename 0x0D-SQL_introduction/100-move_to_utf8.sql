-- Script to convert hbtn_0c_0 database, first_table table, and name field to UTF8
-- Replace 'hbtn_0c_0' with the actual database name
USE hbtn_0c_0;
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
