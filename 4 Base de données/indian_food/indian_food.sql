--requetes
--2) plats venant de l'East
SELECT * 
  FROM indian_food
  WHERE region = 'East';

--3) uniquement le nom et les ingrédients des plats venant de l'East
SELECT name, ingredients 
  FROM indian_food
  WHERE region = 'East';

--4) nombre de plats végétariens
SELECT COUNT(*)
  FROM indian_food
  WHERE diet = "vegetarian";

--5) nombre de plats végétariens ne contenant pas de lait
SELECT COUNT(*)
  FROM indian_food
  WHERE (diet = "vegetarian") AND (ingredients NOT LIKE '%Milk%');   
