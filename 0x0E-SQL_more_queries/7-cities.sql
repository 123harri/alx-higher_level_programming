-- Create database hbtn_0d_usa and table cities in a specified MySQL server.
-- Check if the database hbtn_0d_usa already exists
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Switch to the database hbtn_0d_usa
USE `hbtn_0d_usa`;
-- If cities doesn't exist, create the table
CREATE TABLE IF NOT EXISTS `cities` (
  `id` INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
  `state_id` INT NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);
