CREATE DATABASE neighborhoodDB CHARACTER SET utf8mb4;
CREATE USER neighborhoodAdmin@localhost IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON neighborhoodDB.* TO neighborhoodAdmin@localhost;
FLUSH PRIVILEGES;

use neighborhoodDB;
CREATE TABLE IF NOT EXISTS person (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    id_card VARCHAR(20) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    status TINYINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;
