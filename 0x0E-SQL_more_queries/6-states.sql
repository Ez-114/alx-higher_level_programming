-- Create a new database named hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use that database
USE hbtn_0d_usa;

-- Create a new table in the database
CREATE TABLE IF NOT EXISTS states (
	id	INT	AUTO_INCREMENT	PRIMARY KEY,
	name	VARCHAR(256)	NOT NULL
);
