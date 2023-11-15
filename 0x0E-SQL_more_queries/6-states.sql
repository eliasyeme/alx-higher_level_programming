-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) in MySQL server.
-- If the database hbtn_0d_usa already exists, script will not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select hbtn_0d_usa to run the query 
USE hbtn_0d_usa;

-- states description:
--      id INT unique, auto generated, can’t be null and is a primary key
--      name VARCHAR(256) can’t be null
-- If the table states already exists, script will not fail
CREATE TABLE
    IF NOT EXISTS states (
        id INT UNIQUE NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    );