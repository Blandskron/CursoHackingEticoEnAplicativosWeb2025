<?php require 'init.php'; ?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Formulario de Comentarios Seguro</title>
</head>
<body>
  <h2>Enviar Comentario</h2>
  <form method="POST" action="comentarios.php">
    <label>Nombre:</label><br>
    <input type="text" name="nombre" required><br><br>

    <label>Comentario:</label><br>
    <textarea name="comentario" rows="5" cols="40" required></textarea><br><br>

    <input type="hidden" name="csrf_token" value="<?php echo $_SESSION['csrf_token']; ?>">
    <input type="submit" value="Enviar">
  </form>
</body>
</html>
