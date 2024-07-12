CREATE DATABASE IF NOT EXISTS democraticNews;
USE democraticNews;

drop table if exists noticias;
CREATE TABLE IF NOT EXISTS noticias (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    gender VARCHAR(20),
    titulo VARCHAR(100),
    subtitulo VARCHAR(100),
    tipo VARCHAR(100),
    imagen TEXT,
    cuerpo TEXT,
    
    PRIMARY KEY(id)
);

INSERT INTO noticias (nombre, apellido, correo, gender, titulo, subtitulo, tipo, imagen, cuerpo)
VALUES ('Maria', 'Robledo', 'maria@example.com', 'M', 'Titulo1', 'subtitulo1', 'tipo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwDoVYH_Q2wJicyLMNXpjz4r2jeOue5Tr8qQ&s', 'cuerpo noticia');