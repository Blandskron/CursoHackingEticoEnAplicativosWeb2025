CREATE DATABASE IF NOT EXISTS seguridad_lab;
USE seguridad_lab;

CREATE TABLE IF NOT EXISTS comentarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  comentario TEXT
);
