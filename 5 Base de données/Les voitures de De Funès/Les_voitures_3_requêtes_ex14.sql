--1)La liste des voitures disponibles.
SELECT modele
FROM Voiture
WHERE disponible = True;


--2)Le nombre de voitures disponibles.
SELECT COUNT(modele)
FROM Voiture
WHERE disponible = True;

--3)La liste des voitures avec leur numéro ayant des réparations à prévoir. On affichera également les réparations à prévoir.
SELECT modele, n_voiture, reparation
FROM Voiture
WHERE reparation <>'';


--4)La liste des modèles non diesel.
SELECT nom
FROM modele
WHERE NOT carburant = 'diesel';


--5)La liste des modèles non diesel avec leur prix de location par ordre décroissant.
SELECT nom, prix_location
FROM modele
WHERE NOT carburant = 'diesel'
ORDER BY prix_location DESC;


--6)La liste des voitures avec leur caractéristiques de peinture noire
SELECT nom, caracteristiques
FROM modele
WHERE caracteristiques LIKE '%noire%';
