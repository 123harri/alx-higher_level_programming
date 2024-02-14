-- Create database hbtn_0d_usa and table states in a specified MySQL server
-- Check if the database hbtn_0d_usa already exists
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Switch to the database hbtn_0d_usa
USE `hbtn_0d_usa`;
-- If states doesn't exist, create the table
CREATE TABLE IF NOT EXISTS `states` (
  `id` INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL
);
