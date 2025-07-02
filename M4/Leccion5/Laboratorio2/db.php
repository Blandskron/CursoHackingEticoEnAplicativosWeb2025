<?php
$mysqli = new mysqli("localhost", "root", "", "vuln_lab", 3307);

if ($mysqli->connect_error) {
    die("❌ Conexión fallida: " . $mysqli->connect_error);
}
?>
