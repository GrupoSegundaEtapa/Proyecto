<?php
$servername = "localhost";
$database = "academia";
$username = "root";
$password = "";
// Cse crea la coneccion
$conn = mysqli_connect($servername, $username, $password, $database);
// comprobamos coneccion
if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
}
 
echo "Conectado" . " <br>";


$user = $_POST["userMail"];
$pw = $_POST["userPw"];

$sql="SELECT * FROM `usuarios` WHERE usuario = '$user' and pass = '$pw'";
$result=mysqli_query($conn, $sql);

 $filas=mysqli_num_rows($result);
 	if($filas>0) {
 	session_start();
 	$_SESSION['user'] = '$sesuser';
 	header("location:index2.php");
 }
 else
 	header("location:login-error.html");


?>