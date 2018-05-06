package Lab;

import javax.servlet.ServletConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class AreaCheckServlet extends HttpServlet {

    public ServletConfig config;

    public void init (ServletConfig config) {
        this.config = config;
    }

    public void destroy() {}

    public ServletConfig getServletConfig()
    {
        return config;
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        if (PointArrayBean.requests == null){
            config.getServletContext().setAttribute("list", PointArrayBean.getInstance().getRequests());
        }

        if (request.getParameter("cx").equals("-999.99") || request.getParameter("cy").equals("-999.99") ||
                request.getParameter("cy").equals("-999.99")) {
            config.getServletContext().setAttribute("list", new ArrayList<RequestBean>());
        }

        response.setHeader("Content-Type", "text/html; charset=UTF-8");
        PrintWriter sout = response.getWriter();
        double x = Double.parseDouble(request.getParameter("cx"));
        double y = Double.parseDouble(request.getParameter("cy"));
        double r = Double.parseDouble(request.getParameter("cr"));
        boolean flag = checkArea(x, y, r);
        RequestBean p = new RequestBean(x, y, r, flag);
//        add new point in bean
        PointArrayBean.getInstance().getRequests().add(p);
        sout.print(flag ? "1" : "0");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.sendRedirect("control");

    }

    public static boolean checkArea(double x, double y, double R){
        if (x < 0 && y < 0 && x + y >= -R) {
            return true;
        }
        if (x >= 0 && y >= 0 && x * x + y * y <= R * R / 4) {
            return true;
        }
        return x >= 0 && y <= 0 && x <= R / 2 && y >= -R;
    }

}
