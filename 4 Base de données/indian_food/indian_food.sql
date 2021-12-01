--requetes
--2) plats venant de l'East
SELECT * 
  from indian_food
  where region = 'East';

--3) uniquement le nom et les ingrédients des plats venant de l'East
SELECT name, ingredients 
  from indian_food
  where region = 'East';

--4) nombre de plats végétariens
SELECT COUNT(*)
  from indian_food
  where diet = "vegetarian";

--5) nombre de plats végétariens ne contenant pas de lait
SELECT COUNT(*)
  from indian_food
  where (diet = "vegetarian") AND (ingredients NOT LIKE '%Milk%');   
