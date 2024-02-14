DROP TABLE IF EXISTS users;

CREATE TABLE users (
    username TEXT PRIMARY KEY,
    dateCreated TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
);