-- Le nom et l'adresse du client n'a pas rendu la voiture de la location n°16.
SELECT nom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.n_voiture = 16;


-- Le nom et l'adresse de tous les clients qui n'ont pas rendu leur voiture de location.
SELECT nom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.fin_loc = '';


-- Le nom et l'adresse de tous les clients qui n'ont pas encore payé.
SELECT nom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.paye = False;


-- Le prix des locations par ordre croissant et le modèle des voitures disponibles.
SELECT prix_location, nom
FROM Modele
JOIN Voiture ON Voiture.modele = Modele.nom
WHERE Voiture.disponible = True
ORDER BY prix_location ASC;


-- Le prix des locations par ordre croissant sans répétitions.
SELECT DISTINCT prix_location
FROM Modele
JOIN Voiture ON Voiture.modele = Modele.nom
WHERE Voiture.disponible = True
ORDER BY prix_location ASC;


-- Les caractéristiques et le carburant de toutes les voitures qui sont en attente de réparation.
SELECT Voiture.n_voiture, Voiture.modele, Modele.caracteristiques, Modele.carburant
FROM Voiture
JOIN Modele ON Voiture.modele = Modele.nom
WHERE Voiture.reparation <> '';
