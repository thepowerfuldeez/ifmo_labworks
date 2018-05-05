<%@page contentType="text/html" pageEncoding="UTF-8"
        language="java" import="java.util.ArrayList, Lab_2.RequestBean"
        session="true"
%>
<%@ page import="Lab_2.RequestBean" %>
<%@ page import="Lab_2.PointArrayBean" %>
<%@ page import="java.io.IOException" %>
<jsp:useBean id="Points" class="Lab_2.PointArrayBean" scope="application"/>


<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lab1_PIP</title>
    <link rel="stylesheet" href="css/main.css">
    <script src="js/jquery-3.2.1.js"></script>
    <script src="js/scripts.js"></script>
    ="css/main.css">
    <script src="js/jquery-3.2.1.js"></script>
    <script src="js/scripts.js"></script>
</head>
<body onload="drawCanvas('canvas', 1);">
<div class="container">
    <header class="back">
        <h2>Программирование интернет-приложений</h2>
        <h3> Григорьев Георгий P3217</h3>
    </header>
</div>
</body>
<body onload="drawCanvas('canvas', 1);">
<div class="container">
    <header class="back">
        <h2>Программирование интернет-приложений</h2>
        <h3> Григорьев Георгий P3217</h3>
        <h4>вар.8233</h4>
    </header>
    <div class="main back">
        <canvas id="canvas" onclick="clickCanvas(event)" class="pic" style="background-color:#ffffff;" width="300px"
                height="300px"></canvas>
        <div class="form-container">
            <form id="form" method="post" target="resultsFrame">
                <div class="x">
                    <label>
                        X:
                    </label>
                    <br/>
                    <input type="button" value="-4" name="X[]" title="-4">-4
                    <input type="button" value="-3" name="X[]" title="-3">-3
                    <input type="button" value="-2" name="X[]" title="-2">-2
                    <input type="button" value="-1" name="X[]" title="-1">-1
                    <input type="button" value="0" name="X[]" title="0">0
                    <input type="button" value="1" name="X[]" title="1">1
                    <input type="button" value="2" name="X[]" title="2">2
                    <input type="button" value="3" name="X[]" title="3">3
                    <input type="button" value="4" name="X[]" title="4">4
                </div>
                <hr/>
                <div class="y">
                    <label>Y: </label>
                    <input type="text" name="Y" id="Y" placeholder="(-5...5)" required="required" title="0">
                </div>
                <hr/>
                <div class="r">
                    <label>R: </label>
                    <input type="radio" name="R" value="1" title="1" onclick="drawCanvas('canvas', 1)">1
                    <input type="radio" name="R" value="2" title="2" onclick="drawCanvas('canvas', 2)">2
                    <input type="radio" name="R" value="3" title="3" onclick="drawCanvas('canvas', 3)">3
                    <input type="radio" name="R" value="4" title="4" onclick="drawCanvas('canvas', 4)">4
                    <input type="radio" name="R" value="5" title="5" onclick="drawCanvas('canvas', 5)">5
                </div>
                <hr/>
                <input type="button" value="submit" onclick="validate(form);">
            </form>

        </div>

    </div>
    <div class="tab back">
        <table id="points" border="1px">
            <tr id="tablehead">
                <th>X coordinate</th>
                <th>Y coordinate</th>
                <th>Radius</th>
                <th>Entrance</th>
            </tr>
            <%
                ArrayList<RequestBean> list = PointArrayBean.getInstance().getRequests();

                if (list != null) {
                    for (int i = list.size() - 1; i >= 0; i--) {
                        ssout.println("<tr>");
                        ssout.println("<td>");
                        ssout.println(list.get(i).getX());
                        ssout.println("</td>");
                        ssout.println("<td>");
                        ssout.println(list.get(i).getY());
                        ssout.println("</td>");
                        ssout.println("<td>");
                        try {
                            ServletConfig config;
                            ssout.println(list.get(i).getR());
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        ssout.println("</td>");
                        ssout.println("<td>");
                        if (list.get(i).getResult()) {
                            ssout.println("Yes");
                        } else {
                            ssout.println("No");
                        }
                        ssout.println("</td>");
                        ssout.println("</tr>");
                    }
                }
            %>
        </table>
    </div>
    <footer class="back">
        ipm
    </footer>
</div>
</body>
</html>
