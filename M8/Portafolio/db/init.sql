CREATE TABLE IF NOT EXISTS clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  email VARCHAR(200) NOT NULL,
  notes TEXT
);

-- Datos de ejemplo
INSERT INTO clients (name, email, notes) VALUES
('Alice Example','alice@example.com','Cliente VIP <b>no borrar</b>'),
('Bob Test','bob@test.com','<script>alert("xss-notes")</script>');
