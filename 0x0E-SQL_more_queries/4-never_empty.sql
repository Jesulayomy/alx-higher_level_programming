-- creates a new table with a default id value
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
