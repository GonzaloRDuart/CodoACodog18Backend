CREATE DATABASE IF NOT EXISTS democraticNews;
USE democraticNews;

CREATE TABLE news (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    gender VARCHAR(1),
    title VARCHAR(100),
    subtitle VARCHAR(100),
    type VARCHAR(20),
    imageUrl VARCHAR(255),
    body TEXT,
    upVotes INT,
    downVotes INT,
    PRIMARY KEY(id)
)

drop table news;