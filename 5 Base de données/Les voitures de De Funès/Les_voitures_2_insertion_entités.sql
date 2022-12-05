-- insertion d'entités dans les tables


-- pour la table Client
INSERT INTO Client(nom, prenom, adresse) VALUES
('de Funès', 'Louis', '85 rue de la Barre'),
('de Funès', 'Olivier', '85 rue de la Barre'),
('Grosso', 'Guy', '1 boulevard Foch'),
('Modo', 'Michel', '3 boulevard Foch');


-- pour la table modele
INSERT INTO Modele VALUES
('Citroën 2CV', 'peinture bleue', 50, 'essence'),
('Citroën DS 21 Pallas', 'peinture noire avec un bateau sur le toit', 500, 'essence'),
('Cadillac DeVille 1964', 'convertible', 400, 'sans plomb'),
('Citroën Méhari', '4 x 4 vert', 250, 'diesel'),
('Soucoupe volante', 'trop top', 1500, 'hydrogène'),
('Citroën DS', 'voiture volante', 750, 'éléctricité'),
('Chenard et Walcker T4 Torpédo', 'peinture verte', 1500, 'essence'),
('Chevrolet Impala SS', 'décapotable', 600, 'essence');


-- pour la table Voiture
INSERT INTO Voiture(modele, reparation, disponible) VALUES
('Citroën 2CV', '', True),
('Citroën 2CV', '', True),
('Citroën 2CV', '', True),
('Cadillac DeVille 1964', 'moteur explosé', False),
('Cadillac DeVille 1964', '', True),
('Cadillac DeVille 1964', '', True),
('Citroën DS 21 Pallas', 'roue AD arrachée', False),
('Citroën DS 21 Pallas', 'siège griffé', False),
('Citroën DS 21 Pallas', '', True),
('Citroën DS', '', False),
('Citroën DS', '', True),
('Citroën DS', '', True),
('Citroën Méhari', 'siège griffée', False),
('Citroën Méhari', 'inondée', False),
('Citroën Méhari', '', True),
('Soucoupe volante', '', False),
('Chenard et Walcker T4 Torpédo', '', True),
('Chevrolet Impala SS', '', True),
('Chevrolet Impala SS', '', True);



-- pour la table Location
INSERT INTO Location(n_client, n_voiture, debut_loc, fin_loc, paye) VALUES
(1, 1, '2022-08-05', '2022-08-08', True),
(1, 7, '2022-08-10', '2022-08-12', True),
(2, 4, '2022-08-10', '2022-08-12', True),
(3, 13, '2022-08-13', '2022-08-22', False),
(1, 1, '2022-08-14', '2022-08-25', True),
(4, 16, '2022-08-20', '', False),
(2, 14, '2022-08-20', '2022-08-25', False),
(1, 8, '2022-08-30', '2022-09-01', True),
(2, 10, '2022-08-30', '', False);
