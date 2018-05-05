package Lab_2;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class AreaCheckServlet extends HttpServlet {

    private ServletConfig config;

    public void init (ServletConfig config) throws ServletException
    {
        this.config = config;
    }

    public void destroy() {}

    public ServletConfig getServletConfig()
    {
        return config;
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        if(PointArrayBean.requests == null){
            config.getServletContext().setAttribute("list", PointArrayBean.getInstance().getRequests());
        }

        response.setHeader("Content-Type", "text/html; charset=UTF-8");
        PrintWriter sout = response.getWriter();
        double x = Double.parseDouble(request.getParameter("cx"));
        double y = Double.parseDouble(request.getParameter("cy"));
        double r = Double.parseDouble(request.getParameter("cr"));
        boolean flag = checkArea(x, y, r);
        RequestBean p = new RequestBean(x, y, r, flag);
        PointArrayBean.getInstance().getRequests().add(p);
        sout.print(flag ? "1" : "0");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.sendRedirect("control");

    }

    private static boolean checkArea(double x, double y, double R){
        if (x < 0 && y < 0 && x + y >= -R) {
            return true;
        }
        if (x >= 0 && y >= 0 && x * x + y * y <= R * R / 4) {
            return true;
        }
        if (x >= 0 && y <= 0 && x <= R / 2 && y >= -R) {
            return true;
        }
        return false;
    }

}
