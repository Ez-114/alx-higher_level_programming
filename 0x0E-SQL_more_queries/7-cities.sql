-- create a new database hbtn_0d_usa and check its existens
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- create a table in hbtn_0d_usa named cities
CREATE TABLE IF NOT EXISTS cities (
	id		INT	AUTO_INCREMENT	PRIMARY KEY,
	state_id	INT		NOT NULL,
	name 		VARCHAR(256)	NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
