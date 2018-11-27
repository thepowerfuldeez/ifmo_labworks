package ru.ifmo.lab3;

import org.primefaces.context.RequestContext;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.ViewScoped;
import java.io.Serializable;
import java.math.BigDecimal;

@ManagedBean
@ViewScoped
public class PointBean implements Serializable {
    private int x;
    private String y;
    private int r;

    @ManagedProperty("#{checkHitBean}")
    private CheckHitBean checkHitBean;

    public void setCheckHitBean(CheckHitBean checkHitBean) {
        this.checkHitBean = checkHitBean;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public void incrementX() {
        if (++x > 4)
            x = -4;
    }

    public void checkHit() {
        boolean hit = checkHitBean.checkHit(new BigDecimal(x), new BigDecimal(y), new BigDecimal(r));
        RequestContext.getCurrentInstance().execute(PlotBean.getJsDrawPointFunction(Integer.toString(x), y, Boolean.toString(hit)));
    }

    public PointBean() {
        x = 0;
        y = "0";
        r = 1;
    }
}
