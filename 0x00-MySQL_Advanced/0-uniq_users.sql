-- script that creates a table users with follwing fields
-- id, email, name
CREATE DATABASE IF NOT EXISTS `holberton`;
USE `holberton`;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)

    )
