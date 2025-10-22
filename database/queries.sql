-- create database gestor-dsoo;

-- CREATE
create table talleres (
	id int auto_increment not null unique,
	nombre varchar(50) not null,
	modalidad varchar(20),
	cupo int,
	fecha datetime not null,
	primary key (id)
)

create table alumnos(
	id int auto_increment not null unique,
	dni varchar(250) not null unique,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	primary key (id)
	
)

create table inscripciones(
	id int auto_increment not null unique,
	id_alumno int not null,
	id_taller int not null,
	primary key (id),
	foreign key (id_alumno) references alumnos(id),
	foreign key (id_taller) references talleres(id)	
)


-- INSERT
insert into alumnos (dni,nombre, apellido) values
("95336850","Juan","Vilcherrez"),
("45342232","Gaston","Lafuente"),
("75633478","Diego","Villagra"),
("1094576","Hector","Benitez"),
("8932673","Gabriel","Martinez");

insert into talleres(nombre,modalidad,cupo,fecha)values
("Musica","Presencial",15,'2025-11-10 11:20:00'),
("Artesanias","Presencial",5,'2025-10-10 15:00:00'),
("Artes Visuales","Presencial",10,'2025-10-20 08:00:00'),
("Fotografía","Virtual",20,'2025-10-20 08:00:00'),
("Danza","Presencial",20,'2025-10-01 09:30:00');

insert into inscripciones(id_alumno,id_taller)values
(1,4),
(2,2),
(4,2),
(1,2),
(4,3);


-- SELECT
select * from alumnos;
select * from talleres;

select u.nombre, u.apellido from alumnos u where dni='95336850';

select t.nombre, u.nombre, u.apellido
from inscripciones i
inner join talleres t on i.id_taller =t.id
inner join alumnos u on i.id_alumno =u.id;

-- UPDATE - DELETE
update alumnos set nombre="Juan Carlos" where dni="95336850"




