create database academia;
use academia;

create table Alumno (
	Matrícula int not null auto_increment,
    DNI int not null,
    Nombre varchar(20) not null,
    Apellido varchar(20) not null,
	Celular int(10) not null,
    Nivel varchar(99) not null,
    ID_user int not null,
    primary key (Matrícula),
    foreign key (ID_user) references Usuario(ID)
);

create table Usuario (
	ID int auto_increment not null,
    Nombre varchar(50) not null,
    Email varchar(99) not null,
    Pass varchar(50) not null,
    Permiso int(1),
    primary key (ID)
);

create table Clase (
	ID int auto_increment not null,
    Nombre varchar(250) not null,
    contenido varchar(250) not null,
    primary key (ID)
);

create table Alum_clase (
	ID int auto_increment not null,
    Matrícula_alum int not null,
    ID_clase int not null,
    primary key (ID),
    foreign key (Matrícula_alum) references Alumno (Matrícula),
    foreign key (ID_clase) references Clase(ID)
);