--  script that creates a table users using the following
-- id email name country
CREATE TABLE IF NOT EXISTS users(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
	country ENUM('US','CO','TN') DEFAULT 'US'
	);
