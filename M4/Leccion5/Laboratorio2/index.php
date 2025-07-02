<?php include "db.php"; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Comentarios Vulnerables</title>
</head>
<body>
    <h1>💬 Comentarios</h1>

    <form method="POST" action="submit.php">
        <input type="text" name="usuario" placeholder="Tu nombre">
        <br><br>
        <textarea name="comentario" placeholder="Escribe un comentario..."></textarea>
        <br><br>
        <input type="submit" value="Enviar">
    </form>

    <hr>

    <h2>Comentarios anteriores:</h2>
    <?php
    $res = $mysqli->query("SELECT * FROM comentarios ORDER BY id DESC");
    while ($row = $res->fetch_assoc()) {
        echo "<p><strong>" . $row['usuario'] . "</strong>: " . $row['comentario'] . "</p>";
    }
    ?>
</body>
</html>
