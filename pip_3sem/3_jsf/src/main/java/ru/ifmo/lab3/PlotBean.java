package ru.ifmo.lab3;

import org.primefaces.context.RequestContext;
import ru.ifmo.lab3.model.ResultModel;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.ViewScoped;
import java.io.Serializable;
import java.math.BigDecimal;
import java.util.List;

@ManagedBean
@ViewScoped
public class PlotBean implements Serializable {

    @ManagedProperty("#{pointBean}")
    private PointBean pointBean;

    @ManagedProperty("#{checkHitBean}")
    private CheckHitBean checkHitBean;

    @ManagedProperty("#{pointListBean}")
    private PointListBean pointListBean;

    public void setCheckHitBean(CheckHitBean checkHitBean) {
        this.checkHitBean = checkHitBean;
    }

    public void setPointBean(PointBean pointBean) {
        this.pointBean = pointBean;
    }

    public void setPointListBean(PointListBean pointListBean) {
        this.pointListBean = pointListBean;
    }

    public void renderPlot() {
        RequestContext.getCurrentInstance().execute(getJsDrawPlotFunction(pointBean.getR()));
        invalidatePoints();
    }

    public void invalidatePoints() {
        List<ResultModel> points =  pointListBean.getPoints();
        BigDecimal radius = new BigDecimal(pointBean.getR());
        for(ResultModel point : points) {
            if(point.getR().compareTo(radius) == 0)
                RequestContext.getCurrentInstance()
                        .execute(getJsDrawPointFunction(point.getX().toString(), point.getY().toString(), Boolean.toString(point.isInArea())));
        }
    }

    public void checkPoint(double x, double y) {
        boolean hit = checkHitBean.checkHit(new BigDecimal(x), new BigDecimal(y), new BigDecimal(pointBean.getR()));
        RequestContext.getCurrentInstance().execute(getJsDrawPointFunction(x, y, hit));
    }

    public static String getJsDrawPointFunction(double x, double y, boolean hit) {
        return getJsDrawPointFunction(Double.toString(x), Double.toString(y), Boolean.toString(hit));
    }

    public static String getJsDrawPointFunction(String x, String y, String hit) {
        return "drawPoint("
                .concat(x)
                .concat(",")
                .concat(y)
                .concat(",")
                .concat(hit)
                .concat(");");
    }

    public static String getJsDrawPlotFunction(double radius) {
        return "renderPlot("
                .concat(Double.toString(radius))
                .concat(")");
    }
}
