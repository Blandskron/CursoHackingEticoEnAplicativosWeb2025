CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100)
);

INSERT INTO usuarios (nombre) VALUES ('Ana'), ('Luis'), ('Carlos'), ('Valeria');
