----La liste des voitures disponibles.
SELECT modele
FROM Voiture
WHERE disponible = True;


--Le nombre de voitures disponibles.
SELECT COUNT(modele)
FROM Voiture
WHERE disponible = True;

--La liste des voitures avec leur numéro ayant des réparations à prévoir.
SELECT modele, n_voiture, reparation
FROM Voiture
WHERE reparation <>'';


--La liste des modèles non diesel.
SELECT nom
FROM modele
WHERE NOT carburant = 'diesel';


--La liste des modèles non diesel avec leur prix de location par ordre décroissant.
SELECT nom, prix_location
FROM modele
WHERE NOT carburant = 'diesel'
ORDER BY prix_location DESC;


--La liste des voitures de peinture noire
SELECT nom, caracteristiques
FROM modele
WHERE caracteristiques LIKE '%noire%';