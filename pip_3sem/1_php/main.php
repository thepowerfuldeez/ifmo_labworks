<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Generated</title>
    </head>
    <body>
        <table border="1" width="100%" cellpadding="5">
            <tr>
                <th>X</th>
                <th>Y</th>
                <th>R</th>
                <th>Result</th>
                <th>Query time</th>
                <th>Script time</th>
            </tr>
            <?php
            @session_start();
            $arrX = (isset($_SESSION["arrX"])) ? $_SESSION["arrX"] : array();
            $arrY = (isset($_SESSION["arrY"])) ? $_SESSION["arrY"] : array();
            $arrR = (isset($_SESSION["arrR"])) ? $_SESSION["arrR"] : array();
            $arrRes = (isset($_SESSION["arrR"])) ? $_SESSION["arrRes"] : array();
            $arrD = (isset($_SESSION["arrD"])) ? $_SESSION["arrD"] : array();
            $arrT = (isset($_SESSION["arrT"])) ? $_SESSION["arrT"] : array();

            $arr = array();
            $x = $_POST["X"];
            $y = $_POST["Y"];
            $r = $_POST["R"];
            $start = microtime(true);
            $date = date("H:i:s", strtotime('-1 hour'));
            $result = "";
            $flag = true;

            if ($x < -3 || $x > 3 || $y < -5 || $y > 3 || $r < 1 || $r > 3)
                 $flag = false;
            if (($x <= 0 && $x >= -$r && $y <= 0) ||
                ($x > 0 && $x <= $r && $y >= -$r / 2.0) ||
                ($x > 0 && $y * $y <= $r * $r - $x * $x))
               $result = "OK";
            else
               $result = "MISS";
            if (!$flag)
               $result = "Incorrect values";

            array_push($arrX, $x);
            array_push($arrY, $y != 0 ? trim($y, "0") : 0);
            array_push($arrR, $r);
            array_push($arrD, $date);
            array_push($arrRes, $result);
            $stime = round(microtime(true) - $start, 5);
            array_push($arrT, $stime);

            for($i = count($arrX) - 1; $i >= 0 ; $i--){
                echo "<tr>";
                echo "<td>$arrX[$i]</td>";
                echo "<td>$arrY[$i]</td>";
                echo "<td>$arrR[$i]</td>";
                echo "<td>$arrRes[$i]</td>";
                echo "<td>$arrD[$i]</td>";
                echo sprintf("<td>"."%.7f" . "</td>", $arrT[$i]);
                echo "</tr>";
            }
            $_SESSION["arrX"] = $arrX;
            $_SESSION["arrY"] = $arrY;
            $_SESSION["arrR"] = $arrR;
            $_SESSION["arrRes"] = $arrRes;
            $_SESSION["arrD"] = $arrD;
            $_SESSION["arrT"] = $arrT;
            ?>
        </table>
    </body>
</html>



<!-- 
old
Для расположения текстовых и графических элементов необходимо использовать табличную верстку.
Данные формы должны передаваться на обработку посредством POST-запроса.
Таблицы стилей должны располагаться в отдельных файлах.
При работе с CSS должно быть продемонстрировано использование селекторов атрибутов, селекторов псевдоклассов, селекторов псевдоэлементов, селекторов потомств а также такие свойства стилей CSS, как наследование и каскадирование.
HTML-страница должна иметь "шапку", содержащую ФИО студента, номер группы и новер варианта. При оформлении шапки необходимо явным образом задать шрифт (sans-serif), его цвет и размер в каскадной таблице стилей.
Отступы элементов ввода должны задаваться в пикселях.
Страница должна содержать сценарий на языке JavaScript, осуществляющий валидацию значений, вводимых пользователем в поля формы. Любые некорректные значения (например, буквы в координатах точки или отрицательный радиус) должны блокироваться.