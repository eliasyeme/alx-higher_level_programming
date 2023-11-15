-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) in MySQL server.
-- If the database hbtn_0d_usa already exists, script will not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select hbtn_0d_usa to run the query 
USE hbtn_0d_usa;

-- cities description:
--      id INT unique, auto generated, can’t be null and is a primary key
--      state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
--      name VARCHAR(256) can’t be null
-- If the table cities already exists, script will not fail
CREATE TABLE
    IF NOT EXISTS cities (
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (state_id) REFERENCES states (id)
    );