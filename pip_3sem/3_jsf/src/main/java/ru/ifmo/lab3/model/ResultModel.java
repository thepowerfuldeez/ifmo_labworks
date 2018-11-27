package ru.ifmo.lab3.model;

import ru.ifmo.lab3.database.ResultEntity;

import java.io.Serializable;
import java.math.BigDecimal;

public class ResultModel implements Serializable {
    private BigDecimal x;
    private BigDecimal y;
    private BigDecimal r;
    private boolean inArea;

    public BigDecimal getX() {
        return x;
    }

    public BigDecimal getY() {
        return y;
    }

    public BigDecimal getR() {
        return r;
    }

    public boolean isInArea() {
        return inArea;
    }

    public ResultModel(BigDecimal x, BigDecimal y, BigDecimal r, boolean inArea) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.inArea = inArea;
    }

    public ResultModel(double x, double y, double r, boolean inArea) {
        this.x = new BigDecimal(x);
        this.y = new BigDecimal(y);
        this.r = new BigDecimal(r);
        this.inArea = inArea;
    }

    public ResultModel(ResultEntity entity) {
        x = new BigDecimal(entity.getX());
        y = new BigDecimal(entity.getY());
        r = new BigDecimal(entity.getR());
        inArea = entity.isIncluded() == 1;
    }

    public ResultEntity toEntity() {
        ResultEntity entity = new ResultEntity();
        entity.setX(x.doubleValue());
        entity.setY(y.doubleValue());
        entity.setR(r.doubleValue());
        entity.setIncluded(inArea ? 1 : 0);
        return entity;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        ResultModel that = (ResultModel) o;

        if (inArea != that.inArea) return false;
        if (x != null ? !x.equals(that.x) : that.x != null) return false;
        if (y != null ? !y.equals(that.y) : that.y != null) return false;
        return r != null ? r.equals(that.r) : that.r == null;
    }

    @Override
    public int hashCode() {
        int result = x != null ? x.hashCode() : 0;
        result = 31 * result + (y != null ? y.hashCode() : 0);
        result = 31 * result + (r != null ? r.hashCode() : 0);
        result = 31 * result + (inArea ? 1 : 0);
        return result;
    }
}
