<?php

$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$email = $_POST['email'];
$date = $_POST['date'];
$time = $_POST['time'];

//database connection

$conn = new mysqli(URL);
if($conn->connect_error){
    die("Error connecting to database" . $conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into registration(firstName, lastName, email, date, time)
        values(?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssss",$firstName,$lastName,$email,$date,$time);
    $stmt->execute();
    echo "success";
    $stmt->close();
    $conn->close();
}
?>