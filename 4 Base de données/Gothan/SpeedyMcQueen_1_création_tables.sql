-- création des tables
CREATE TABLE Client
(n_client INT PRIMARY KEY,
nom TEXT NOT NULL,
adresse TEXT NOT NULL);

CREATE TABLE Modele
(nom TEXT PRIMARY KEY,
caracteristiques TEXT NOT NULL,
prix_location REAL NOT NULL,
carburant TEXT NOT NULL,
CHECK (prix_location>0) );

CREATE TABLE Voiture
(n_voiture INT PRIMARY KEY,
modele TEXT REFERENCES Modele(nom),
reparation TEXT,
disponible BOOLEAN NOT NULL);

CREATE TABLE Location
(n_location INT PRIMARY KEY,
n_client INT REFERENCES Client(n_client),
n_voiture INT REFERENCES Voiture(n_voiture),
debut_loc DATE NOT NULL,
fin_loc DATE,
paye BOOLEAN NOT NULL);