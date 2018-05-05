package Lab_2;


import java.io.Serializable;
import java.util.ArrayList;

public class PointArrayBean implements Serializable {

    public static ArrayList<RequestBean> requests;
    public static PointArrayBean ourInstance = new PointArrayBean();

    public static PointArrayBean getInstance() {
        if (ourInstance == null) {
            synchronized (PointArrayBean.class) {
                if (ourInstance == null) {
                    ourInstance = new PointArrayBean();
                }
            }
        }
        return ourInstance;
    }
    public static ArrayList<RequestBean> getRequests() {
        if (requests != null)
            return requests;
        else
            return requests = new ArrayList<RequestBean>();
    }
    public static void setRequests(ArrayList<RequestBean> requests) {
        PointArrayBean.requests = requests;
    }
    public PointArrayBean() {
        requests = new ArrayList<RequestBean>();
    }
}
