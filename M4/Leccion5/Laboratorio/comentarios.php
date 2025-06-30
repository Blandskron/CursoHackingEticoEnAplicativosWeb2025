<?php
require 'conexion.php';
require 'init.php';

// Verificación de token CSRF
if (!isset($_POST['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
    die("❌ Token CSRF inválido.");
}

// Sanitizar entradas para prevenir XSS
$nombre = htmlspecialchars($_POST['nombre'], ENT_QUOTES, 'UTF-8');
$comentario = htmlspecialchars($_POST['comentario'], ENT_QUOTES, 'UTF-8');

// Usar prepared statements para prevenir SQLi
$stmt = $conexion->prepare("INSERT INTO comentarios (nombre, comentario) VALUES (?, ?)");
$stmt->bind_param("ss", $nombre, $comentario);
$stmt->execute();

// Confirmación
echo "✅ Comentario guardado correctamente y de forma segura.";
?>
