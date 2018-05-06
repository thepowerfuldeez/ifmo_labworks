<%--
  Created by IntelliJ IDEA.
  User: thepowerfuldeez
  Date: 06/05/2018
  Time: 17:02
  To change this template use File | Settings | File Templates.
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"
        import="java.util.ArrayList, java.io.IOException, Lab.RequestBean, Lab.PointArrayBean"
%>
<jsp:useBean id="Points" class="Lab.PointArrayBean" scope="application"/>


<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lab2_PIP</title>
    <link rel="stylesheet" href="css/main.css">
    <script src="js/jquery-3.2.1.js"></script>
    <script src="js/scripts.js"></script>
</head>
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
            <form id="form" method="post" target="points">
                <div class="x">
                    X: <div id="X_s"></div>
                    <br/>
                    <input class="x_b" type="button" value="-4" name="X" title="-4">
                    <input class="x_b" type="button" value="-3" name="X" title="-3">
                    <input class="x_b" type="button" value="-2" name="X" title="-2">
                    <input class="x_b" type="button" value="-1" name="X" title="-1">
                    <input class="x_b" type="button" value="0" name="X" title="0">
                    <input class="x_b" type="button" value="1" name="X" title="1">
                    <input class="x_b" type="button" value="2" name="X" title="2">
                    <input class="x_b" type="button" value="3" name="X" title="3">
                    <input class="x_b" type="button" value="4" name="X" title="4">
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
                ArrayList<RequestBean> list = PointArrayBean.getRequests();

                if (list != null) {
                    for (int i = list.size() - 1; i >= 0; i--) {
                        out.println("<tr>\n<td>");
                        out.println(list.get(i).getX());
                        out.println("</td>\n<td>");
                        out.println(list.get(i).getY());
                        out.println("</td>\n<td>");
                        try {
                            out.println(list.get(i).getR());
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        out.println("</td>\n<td>");
                        if (list.get(i).getResult()) {
                            out.println("Yes");
                        } else {
                            out.println("No");
                        }
                        out.println("</td>\n</tr>");
                    }
                }
            %>
        </table>
    </div>
    <footer class="back">
        <a id="clear_b" href=".">Reset</a>
    </footer>
    <script>
        $("#clear_b").click(clearTable());
        $(".x_b").each(function () {
            $(this).on("click", function () {
                $("#X_s").text($(this).attr("value"));
            });
        });
    </script>
</div>
</body>
</html>
