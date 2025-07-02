CREATE DATABASE vuln_lab;

USE vuln_lab;

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    comentario TEXT
);
