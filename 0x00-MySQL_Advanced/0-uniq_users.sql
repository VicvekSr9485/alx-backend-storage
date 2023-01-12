-- SQL script that creates a table users
-- all data are unique
CREATE TABLE IF NOT EXISTS users
INSERT INTO users (
	id INT NOT NULL AUTO INCREMENT PRIMARY KEY
	email VARCHAR(255) NOT NULL UNIQUE
	name VARCHAR(255)
)
