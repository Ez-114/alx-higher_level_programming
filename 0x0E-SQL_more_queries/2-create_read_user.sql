-- Creates user "user_0d_2"@"localhost" and database "htbn_0d_2"
-- and granting user "user_0d_2" his required privilleges

-- Creating "htbn_0d_2" database on local machine
CREATE DATABASE IF NOT EXISTS htbn_0d_2;

-- Create "user_0d_2" user on "localhost"
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant the created user the SELECT privellege only
GRANT SELECT ON `htbn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
