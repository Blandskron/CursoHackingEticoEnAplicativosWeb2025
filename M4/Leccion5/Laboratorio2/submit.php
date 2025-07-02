<?php
include "db.php";

// ⚠️ sin protección deliberadamente
$usuario = $_POST['usuario'];
$comentario = $_POST['comentario'];

// ⚠️ construir la consulta manualmente vulnerable
$sql = "INSERT INTO comentarios (usuario, comentario) VALUES ('$usuario', '$comentario');";

// ⚠️ permite múltiples consultas (DROP TABLE, etc.)
if ($mysqli->multi_query($sql)) {
    echo "✅ Comentario enviado.";
} else {
    echo "❌ Error: " . $mysqli->error;
}
?>
