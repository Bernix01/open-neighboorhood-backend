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


create table if not exists blockk(
	block_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(20)
    );


create table if not exists house(
	house_id INT AUTO_INCREMENT PRIMARY KEY,
    block_id INT NOT NULL,
    phone VARCHAR(10),
	FOREIGN KEY (block_id)
        REFERENCES blockk (block_id)    
);

create table if not exists landlord(
	landlord_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT NOT NULL,
    house_id INT NOT NULL,
    FOREIGN KEY (person_id)
        REFERENCES person (person_id),
	FOREIGN KEY (house_id)
        REFERENCES house (house_id)    
);

create table if not exists guest(
	guest_id INT AUTO_INCREMENT PRIMARY KEY,
    landlord_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    entry_date TIMESTAMP ,
	departure_date TIMESTAMP,
    FOREIGN KEY (landlord_id)
        REFERENCES landlord (landlord_id)    
)ENGINE=INNODB;