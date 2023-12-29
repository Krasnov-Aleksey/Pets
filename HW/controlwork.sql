DROP DATABASE IF EXISTS human_frends;
CREATE DATABASE IF NOT EXISTS human_frends;

USE human_frends;	

DROP TABLE IF EXISTS animal;
CREATE TABLE IF NOT EXISTS animal (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
type_animals VARCHAR(45)
);
INSERT INTO animal(type_animals)
VALUES
('Pets'),
('Pack animals');

SELECT * FROM animal;

DROP TABLE IF EXISTS pets;
CREATE TABLE IF NOT EXISTS pets (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
kind_animal  VARCHAR(45),
animal_id INT NOT NULL,
FOREIGN KEY (animal_id) REFERENCES animal(id) ON DELETE CASCADE
);
INSERT INTO pets(kind_animal, animal_id)
VALUES
('Dog', 1),
("Cat", 1),
('Hamster', 1);

SELECT * FROM pets;

DROP TABLE IF EXISTS pack_animals;
CREATE TABLE IF NOT EXISTS pack_animals (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
kind_animal  VARCHAR(45),
animal_id INT NOT NULL,
FOREIGN KEY (animal_id) REFERENCES animal(id) ON DELETE CASCADE
);
INSERT INTO pack_animals (kind_animal, animal_id)
VALUES
('Horse',2),
('Camel',2),
('Donkey',2);

SELECT * FROM pack_animals;

DROP TABLE IF EXISTS dog;
CREATE TABLE IF NOT EXISTS dog (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pets(id) ON DELETE CASCADE
);
INSERT INTO dog (name_a, type_id, birthday, commands)
VALUES
('Fido', 1, '2020-01-01','Sit,Stay,Fetch'),
('Buddy', 1, '2018-12-10', 'Sit, Paw, Bark'),
('Bella',1,'2019-11-11','Sit, Stay, Roll');

SELECT * FROM dog;

DROP TABLE IF EXISTS cat;
CREATE TABLE IF NOT EXISTS cat (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pets(id) ON DELETE CASCADE
);
INSERT INTO cat (name_a, type_id, birthday, commands)
VALUES
('Whiskers',2,'2019-05-15','Sit, Pounce'),
('Smudge',2,'2020-02-20','Sit, Pounce, Scratch'),
('Oliver',2,'2020-06-30','Meow, Scratch, Jump');

SELECT * FROM cat;

DROP TABLE IF EXISTS hamster;
CREATE TABLE IF NOT EXISTS hamster (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pets(id) ON DELETE CASCADE
);
INSERT INTO hamster (name_a, type_id, birthday, commands)
VALUES
('Hammy',3,'2021-03-10','Roll, Hide'),
('Peanut',3,'2021-08-01','Roll, Spin');

SELECT * FROM hamster;

DROP TABLE IF EXISTS horse;
CREATE TABLE IF NOT EXISTS horse (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pack_animals(id) ON DELETE CASCADE
);
INSERT INTO horse (name_a, type_id, birthday, commands)
VALUES
('Thunder',1,'2015-07-21','Trot, Canter, Gallop'),
('Storm',1,'2014-05-05','Trot, Canter'),
('Blaze',1,'2016-02-29','Trot, Jump, Gallop');

SELECT * FROM horse;

DROP TABLE IF EXISTS camel;
CREATE TABLE IF NOT EXISTS camel (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pack_animals(id) ON DELETE CASCADE
);
INSERT INTO camel (name_a, type_id, birthday, commands)
VALUES
('Sandy',2,'2016-11-03','Walk, Carry Load'),
('Dune',2,'2018-12-12','Walk, Sit'),
('Sahara',2,'2015-08-14','Walk, Run');

SELECT * FROM camel;

DROP TABLE IF EXISTS donkey;
CREATE TABLE IF NOT EXISTS donkey (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name_a VARCHAR(45),
type_id INT,
birthday DATE,
commands VARCHAR(45),
FOREIGN KEY (type_id) REFERENCES pack_animals(id) ON DELETE CASCADE
);
INSERT INTO donkey (name_a, type_id, birthday, commands)
VALUES
('Eeyore',3,'2017-09-18','Walk, Carry Load, Bray'),
('Burro',3,'2019-01-23','Walk, Bray, Kick');

SELECT * FROM donkey;

DELETE FROM pack_animals WHERE kind_animal='Camel';

SELECT * FROM pack_animals;

SELECT * FROM horse
UNION SELECT * FROM donkey;


DROP TABLE IF EXISTS age_animal;
CREATE TABLE IF NOT EXISTS age_animal AS
SELECT *, TIMESTAMPDIFF(month,birthday,curdate()) AS m FROM dog
UNION ALL SELECT *, TIMESTAMPDIFF(month,birthday,curdate()) AS m FROM cat 
UNION ALL SELECT *, TIMESTAMPDIFF(month,birthday,curdate()) AS m FROM hamster
UNION ALL SELECT *, TIMESTAMPDIFF(month,birthday,curdate()) AS m FROM horse
UNION ALL SELECT *, TIMESTAMPDIFF(month,birthday,curdate()) AS m FROM donkey;

SELECT * FROM age_animal;

DROP TABLE IF EXISTS y_animal;
CREATE TABLE IF NOT EXISTS y_animal AS
SELECT * FROM age_animal
WHERE m>12 AND m<36;

SELECT * FROM y_animal;











