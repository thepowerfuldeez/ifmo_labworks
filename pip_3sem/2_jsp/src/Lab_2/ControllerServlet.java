package Lab_2;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ControllerServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
     throws ServletException, IOException {
		request.getServletContext().getRequestDispatcher("/index.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
		String xString=request.getParameter("cx");
		String yString=request.getParameter("cy");
		String RString=request.getParameter("cr");

		if(xString == null || yString == null || RString == null){
			request.getServletContext().getRequestDispatcher("/index.jsp").forward(request, response);
		} else {
			request.getServletContext().getRequestDispatcher("/checking").forward(request, response);
		}
    }
}
