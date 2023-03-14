-- creates a table and inserts some rows in it
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- row 1
INSERT INTO second_table
VALUES (1, 'John', 10);
-- row 2
INSERT INTO second_table
VALUES (2, 'Alex', 3);
-- row 3
INSERT INTO second_table
VALUES (3, 'Bob', 14);
-- row 4
INSERT INTO second_table
VALUES (4, 'George', 8);
