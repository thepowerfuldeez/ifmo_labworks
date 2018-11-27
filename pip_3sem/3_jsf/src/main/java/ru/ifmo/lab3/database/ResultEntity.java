package ru.ifmo.lab3.database;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "Results")
public class ResultEntity implements Serializable {
    public ResultEntity() {

    }

    public ResultEntity(double x, double y, double r, int included) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.included = included;
    }

    @Id
    @SequenceGenerator(name = "SEQ", sequenceName = "Results_seq", allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "SEQ")
    @Column(name = "ID")
    private long id;

    @Basic
    @Column(name = "X", nullable = false)
    private double x;

    @Basic
    @Column(name = "Y", nullable = false)
    private double y;

    @Basic
    @Column(name = "R", nullable = false)
    private double r;

    @Basic
    @Column(name = "Included", nullable = false)
    private int included;

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }

    public int isIncluded() {
        return included;
    }

    public void setIncluded(int included) {
        this.included = included;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }
}
