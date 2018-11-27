package ru.ifmo.lab3;

import ru.ifmo.lab3.model.ResultModel;

import javax.faces.bean.ApplicationScoped;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import java.math.BigDecimal;

@ManagedBean
@ApplicationScoped
public class CheckHitBean {
    private static final BigDecimal TWO = new BigDecimal("2");

    @ManagedProperty("#{pointListBean}")
    private PointListBean service;

    public void setService(PointListBean service) {
        this.service = service;
    }

    /**
     * Условия проверки:
     * 1 четверть: x =< R/2 и y =< R
     * 2 четверть: y <= x + R
     * 3 четверть: x ^ 2 + y ^ 2 < (r/2)^2
     */
    public boolean checkHit(BigDecimal x, BigDecimal y, BigDecimal r) {
        BigDecimal halfR = r.divide(TWO);
        boolean inArea =
                (x.compareTo(BigDecimal.ZERO) >= 0 && y.compareTo(BigDecimal.ZERO) >= 0 && x.compareTo(halfR) <= 0 && y.compareTo(r) <= 0)
                        || (x.compareTo(BigDecimal.ZERO) <= 0 && y.compareTo(BigDecimal.ZERO) >= 0 && y.compareTo(x.add(r)) <= 0)
                        || (x.compareTo(BigDecimal.ZERO) <= 0 && y.compareTo(BigDecimal.ZERO) <= 0 && x.pow(2).add(y.pow(2)).compareTo(halfR.pow(2)) <= 0);
        service.addModel(new ResultModel(x, y, r, inArea));
        return inArea;
    }
}
