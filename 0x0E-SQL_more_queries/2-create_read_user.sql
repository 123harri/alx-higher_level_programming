-- Create MySQL database hbtn_0d_2 and user user_0d_2 with SELECT privilege.
-- If hbtn_0d_2 doesn't exist, create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- If user_0d_2 doesn't exist, create the user and grant SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege to user_0d_2 on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';
