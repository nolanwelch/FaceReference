DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS images;
DROP TABLE IF EXISTS imagetags;
DROP TABLE IF EXISTS tags;

CREATE TABLE users (
    username TEXT PRIMARY KEY,
    dateCreated TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
);

CREATE TABLE images (
    id INT PRIMARY KEY,
    uri TEXT NOT NULL,
    height INT NOT NULL,
    width INT NOT NULL,
    altText TEXT
);

CREATE TABLE imagetags (
    imageId INT,
    tagId INT,
    FOREIGN KEY(imageId) REFERENCES images(id),
    FOREIGN KEY(tagId) REFERENCES tags(id)
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag TEXT
);