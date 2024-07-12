CREATE DATABASE IF NOT EXISTS democraticNews;
USE democraticNews;

CREATE TABLE noticias (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    titulo VARCHAR(100),
    subtitulo VARCHAR(100),
    imagen VARCHAR(100),
    cuerpo VARCHAR(2000),
    
    PRIMARY KEY(id)
);

INSERT INTO noticias (nombre, apellido, correo, titulo, subtitulo, imagen, cuerpo)
VALUES ('Maria', 'Robledo', 'maria@example.com', 'Titulo1', 'subtitulo1', 'imagen1.png', 'cuerpo noticia');
select * from news;
drop table noticia;