-- Creates the MySql server user "user_0d_1"
-- The user should have all privilleges

-- User creation
CREATE USER IF NOT EXISTS
	'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';

-- Grant user all privilleges
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
