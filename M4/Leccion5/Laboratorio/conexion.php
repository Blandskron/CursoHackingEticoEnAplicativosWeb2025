<?php
$conexion = new mysqli("127.0.0.1", "root", "", "seguridad_lab", 3307);

// Verifica si falló la conexión
if ($conexion->connect_error) {
    die("Conexión fallida: " . $conexion->connect_error);
}
?>
