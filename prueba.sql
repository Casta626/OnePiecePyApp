
create table capvistos (
id INTEGER PRIMARY KEY NOT NULL,
capname VARCHAR (200),
day varchar(50),
people Varchar (150)
);

Create table images(
id integer PRIMARY key not NULL,
name Varchar(50)
);



INSERT into capvistos values ("1", "¡Yo soy Luffy, el próximo rey de los piratas!", "04/07/2022", "Casta");
INSERT into capvistos values ("2", "¡Entra el gran espadachín! ¡El Cazador de Piratas Roronoa Zoro!" ,"05/07/2022", "Casta");
INSERT into capvistos values ("3", "¡Morgan vs Luffy! ¿Quién es esta linda joven?", "06/07/2022", "Casta");
INSERT into capvistos values ("4", "El pasado de Luffy! Emerge el 'Pelirrojo' Shanks!", "07/07/2022", "Casta");

INSERT into images values ("1", "luffyultrainstinto.jpg");
añadir otra variable para guardar la posicion en nel array o guardar
las imagenes en una carpeta.