-- insertion d'entités dans les tables


-- pour la table Client
INSERT INTO Client VALUES
(1, 'Batman', '85 rue de la Barre, Gotham City'),
(2, 'Robin', '85 rue de la Barre, Gotham City'),
(3, 'Catwoman', '49 rue des Mystères, Gotham City'),
(4, 'The Joker', '3 boulevard Foch, Gotham City'),
(5, 'Le Pinguoin', '12 place du Ralliement, Gotham City'),
(6, 'Robin', '85 rue de la Barre, Gotham City');


-- pour la table modele
INSERT INTO Modele VALUES
('Batmobile modèle 1950', 'peinture violette', 250, 'essence'),
('Batmobile modèle 1990', 'peinture noire', 250, 'sans plomb'),
('Batmobile modèle 2000', 'peinture noire, 6 roues', 500, 'hydrogène'),
('Batmobile modèle 2010', 'look impressionnant', 750, 'éléctricité'),
('Batmobile modèle 2020', 'wouaoum', 1000, 'eau'),
('Jeep', '4 x 4', 250, 'diesel'),
('Limousine', 'hyper Deluxe', 1500, 'diesel');


-- pour la table Voiture
INSERT INTO Voiture VALUES
(1, 'Batmobile modèle 1950', '', True),
(2, 'Batmobile modèle 1950', '', True),
(3, 'Batmobile modèle 1950', '', True),
(4, 'Batmobile modèle 1990', 'moteur explosé', False),
(5, 'Batmobile modèle 1990', '', True),
(6, 'Batmobile modèle 1990', '', True),
(7, 'Batmobile modèle 2000', 'roue AD arrachée', False),
(8, 'Batmobile modèle 2000', 'siège griffé', False),
(9, 'Batmobile modèle 2000', '', True),
(10, 'Batmobile modèle 2010', '', False),
(11, 'Batmobile modèle 2010', '', True),
(12, 'Batmobile modèle 2010', '', True),
(13, 'Jeep', 'siège griffée', False),
(14, 'Jeep', 'inondée', False),
(15, 'Jeep', '', True),
(16, 'Limousine', '', False),
(17, 'Batmobile modèle 2020', '', True),
(18, 'Batmobile modèle 2020', '', True),
(19, 'Batmobile modèle 2020', '', True);



-- pour la table Location
INSERT INTO Location VALUES
(1, 1, 1, '2020-08-05', '2020-08-08', True),
(2, 1, 7, '2020-08-10', '2020-08-12', True),
(3, 2, 4, '2020-08-10', '2020-08-12', True),
(4, 3, 13, '2020-08-13', '2020-08-22', False),
(5, 1, 1, '2020-08-14', '2020-08-25', True),
(6, 4, 16, '2020-08-20', '', False),
(7, 5, 14, '2020-08-20', '2020-08-25', False),
(8, 1, 8, '2020-08-30', '2020-09-01', True),
(9, 6, 10, '2020-08-30', '', False);