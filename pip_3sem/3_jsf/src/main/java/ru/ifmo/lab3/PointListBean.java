package ru.ifmo.lab3;

import ru.ifmo.lab3.database.ResultRepository;
import ru.ifmo.lab3.model.ResultModel;

import javax.faces.bean.ApplicationScoped;
import javax.faces.bean.ManagedBean;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

@ManagedBean
@ApplicationScoped
public class PointListBean implements Serializable {
    private ResultRepository repository;
    private List<ResultModel> cache;

    public PointListBean() {
        repository = new ResultRepository();
        cache = null;
    }


    public List<ResultModel> getPoints() {
        if (cache == null) {
            cache = new ArrayList<ResultModel>();
            cache.addAll(repository.get());
        }
        return cache;
    }

    public void addModel(ResultModel model) {
        repository.store(model);
        cache.add(model);
    }
}
