--1)La location n°16 n'a pas été rendu. Quel est le nom et l'adresse du client.
SELECT nom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.n_voiture = 6;


--2)Le nom, le prénom et l'adresse de tous les clients qui n'ont pas rendu leur voiture de location.
SELECT nom, prenom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.fin_loc = '';


--3)Le nom et l'adresse de tous les clients qui n'ont pas encore payé.
SELECT nom, adresse
FROM Client
JOIN Location ON Location.n_client = Client.n_client
WHERE Location.paye = False;


--4)Pour aider le client, afficher le prix des locations par ordre croissant et le modèle des voitures disponibles.
SELECT prix_location, nom
FROM Modele
JOIN Voiture ON Voiture.modele = Modele.nom
WHERE Voiture.disponible = True
ORDER BY prix_location ASC;


--5)Le prix des locations des voitures disponibles par ordre croissant sans répétitions.
SELECT DISTINCT prix_location
FROM Modele
JOIN Voiture ON Voiture.modele = Modele.nom
WHERE Voiture.disponible = True
ORDER BY prix_location ASC;


--6)Pour aider le garagiste, le numéro de la voiture, le modèle, les caractéristiques et le carburant de toutes les voitures qui sont en attente de réparation.
SELECT Voiture.n_voiture, Voiture.modele, Modele.caracteristiques, Modele.carburant
FROM Voiture
JOIN Modele ON Voiture.modele = Modele.nom
WHERE Voiture.reparation <> '';


--7)On souhaite avoir la liste des numéros de location ainsi que le modèle de la voiture louée pour toutes les locations.
SELECT Location.n_location, Modele.nom
FROM Location
JOIN Voiture ON Location.n_voiture = Voiture.n_voiture
JOIN Modele ON  Modele.nom = Voiture.modele;



--8)On souhaite avoir la liste des numéros de location ainsi que le modèle de la voiture louée pour toutes les locations qui ont débutées entre le 8 et 15 août 2022.
SELECT Location.n_location, Modele.nom
FROM Location
JOIN Voiture ON Location.n_voiture = Voiture.n_voiture
JOIN Modele ON  Modele.nom = Voiture.modele
WHERE Location.debut_loc >= '2022-08-08' AND Location.debut_loc <= '2022-08-15';  



































