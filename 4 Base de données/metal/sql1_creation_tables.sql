--création des conteneurs
CREATE TABLE bands(
  id INT NOT NULL PRIMARY KEY,
  name TEXT,
  country TEXT,
  status TEXT,
  formed_in TEXT,
  genre TEXT,
  theme TEXT,
  active TEXT
);

CREATE TABLE albums(
  id INT NOT NULL PRIMARY KEY,
  band INT,
  title TEXT,
  year INT,
  FOREIGN KEY(band) REFERENCES bands(id) 
);


CREATE TABLE reviews(
  id INT NOT NULL PRIMARY KEY,
  album INT,
  title TEXT,
  score DECIMAL(3,2),
  content TEXT,
  FOREIGN KEY(album) REFERENCES albums(id)
);