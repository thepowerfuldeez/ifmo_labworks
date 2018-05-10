package Lab;

import java.io.Serializable;

public class RequestBean implements Serializable {
    public double x;
    public double y;
    public double r;
    public boolean result;

    RequestBean(double x, double y, double r, boolean result){
        setX(x);
        setY(y);
        setR(r);
        setResult(result);
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getR() {
        return r;
    }

    public boolean getResult() {
        return result;
    }

    public void setR(double r) {
        this.r = r;
    }

    public void setResult(boolean result) {
        this.result = result;
    }
}
