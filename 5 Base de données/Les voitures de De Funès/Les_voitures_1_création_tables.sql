-- création des tables
CREATE TABLE Client
(n_client INTEGER PRIMARY KEY AUTOINCREMENT,
nom TEXT NOT NULL,
prenom TEXT NOT NULL,
adresse TEXT NOT NULL);

CREATE TABLE Modele
(nom TEXT PRIMARY KEY,
caracteristiques TEXT NOT NULL,
prix_location REAL NOT NULL,
carburant TEXT NOT NULL,
CHECK (prix_location>0) );

CREATE TABLE Voiture
(n_voiture INTEGER PRIMARY KEY AUTOINCREMENT,
modele TEXT REFERENCES Modele(nom),
reparation TEXT,
disponible BOOLEAN NOT NULL);

CREATE TABLE Location
(n_location INTEGER PRIMARY KEY AUTOINCREMENT,
n_client INTEGER REFERENCES Client(n_client),
n_voiture INTEGER REFERENCES Voiture(n_voiture),
debut_loc DATE NOT NULL,
fin_loc DATE,
paye BOOLEAN NOT NULL);
