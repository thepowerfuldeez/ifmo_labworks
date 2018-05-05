<%@page contentType="text/html" pageEncoding="UTF-8"
        language="java" import="java.util.ArrayList, Lab_2.RequestBean"
        session="true"
%>
<%@ page import="Lab_2.RequestBean" %>
<%@ page import="Lab_2.PointArrayBean" %>
<jsp:useBean id="Points" class="Lab_2.PointArrayBean" scope="application" />

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Lab1_PIP</title>
  <link rel="stylesheet" href="css/main.css">
  <script src="js/jquery-3.2.1.js"></script>
  <script src="js/scripts.js"></script>
</head>
<body onload="drawCanvas('canvas', 1);">
<div class="container">
  <header class="back">
    <h2>Программирование интернет-приложений</h2>
    <h3> Рахимов Айдар P3218</h3>
    <h4>v.8061</h4>
  </header>
  <div class="main back">
    <canvas id="canvas" onclick="clickCanvas(event)" class="pic" style="background-color:#ffffff;" width="300px" height="300px"></canvas>
    <div class="form-container">
      <form id="form" method="post" target="resultsFrame">
        <div class="x">
          <lable>
            X:
          </lable>
          <br/>
          <input type="checkbox" value="-2" name="X[]" title="-2">-2
          <input type="checkbox" value="-1.5" name="X[]" title="-1.5">-1.5
          <input type="checkbox" value="-1" name="X[]" title="-1">-1
          <input type="checkbox" value="-0.5" name="X[]" title="-0.5">-0.5
          <input type="checkbox" value="0" name="X[]" title="0">0
          <input type="checkbox" value="0.5" name="X[]" title="0.5">0.5
          <input type="checkbox" value="1" name="X[]" title="1">1
          <input type="checkbox" value="1.5" name="X[]" title="1.5">1.5
          <input type="checkbox" value="2" name="X[]" title="2">2
        </div>
        <hr/>
        <div class="y">
          <label>Y: </label>
          <input type="text" name="Y" id="Y" placeholder="(-5...3)" required="required" title="0">
        </div>
        <hr/>
        <div class="r">
          <lable>R: </lable>
          <input type="radio" name="R" value="1" title="1" onclick="drawCanvas('canvas', 1)">1
          <input type="radio" name="R" value="1.5" title="1.5" onclick="drawCanvas('canvas', 1.5)">1.5
          <input type="radio" name="R" value="2" title="2" onclick="drawCanvas('canvas', 2)">2
          <input type="radio" name="R" value="2.5" title="2.5" onclick="drawCanvas('canvas', 2.5)">2.5
          <input type="radio" name="R" value="3" title="3" onclick="drawCanvas('canvas', 3)">3
        </div>
        <hr/>
        <input type="button" value="submit" onclick="validate(form);">
      </form>

    </div>

  </div>
  <div class="tab back">
    <table  id="points" border="1px">
      <tr id="tablehead">
        <th>X coordinate</th>
        <th>Y coordinate</th>
        <th>Radius</th>
        <th>Entrance</th>
      </tr>
      <%
        ArrayList<RequestBean> list = PointArrayBean.getInstance().getRequests();

        if(list != null) {
          for (int i = list.size() - 1; i >= 0; i--) {
            out.println("<tr>");
            out.println("<td>");
            out.println(list.get(i).getX());
            out.println("</td>");
            out.println("<td>");
            out.println(list.get(i).getY());
            out.println("</td>");
            out.println("<td>");
            out.println(list.get(i).getR());
            out.println("</td>");
            out.println("<td>");
            if (list.get(i).getResult()) {
              out.println("Yes");
            } else {
              out.println("No");
            }
            out.println("</td>");
            out.println("</tr>");
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