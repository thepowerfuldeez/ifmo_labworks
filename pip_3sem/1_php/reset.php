<?php
session_start();
unset($_SESSION["arrX"]);
unset($_SESSION["arrY"]);
unset($_SESSION["arrR"]);
unset($_SESSION["arrRes"]);
unset($_SESSION["arrD"]);
unset($_SESSION["arrT"]);
session_destroy();
header("Location: index.html");
?>