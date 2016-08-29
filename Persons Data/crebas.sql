

CREATE TABLE Persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    birthDate Date
);

INSERT INTO Persons VALUES (NULL, 'Jorge', 'jorge@example.com', "2010-11-23");
