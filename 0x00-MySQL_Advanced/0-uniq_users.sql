-- Uniquie Users
CREATE DATABASE IF NOT EXISTS `holberton`;
USE `holberton`;
CREATE TABLE  users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)

    )
