package ru.ifmo.lab3.database;

import org.hibernate.Session;
import org.hibernate.SessionException;
import ru.ifmo.lab3.model.ResultModel;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ResultRepository {
    private Session session;

    public ResultRepository() {
        try {
            session = HibernateUtil.getSessionFactory().openSession();
        } catch (Throwable ex) {
            System.err.println("Opening session failed" + ex.getMessage());
            throw new SessionException(ex.getMessage());
        }
    }

    public void closeSession() {
        session.close();
    }

    public void store(ResultModel model) {
        session.beginTransaction();
        session.save(model.toEntity());
        session.getTransaction().commit();
    }

    private List<ResultEntity> getListFromDataBase() {
        return session.createQuery("from ResultEntity order by id").list();
    }

    public List<ResultModel> get() {
        List<ResultModel> models = new ArrayList<ResultModel>();
        for (ResultEntity entity: getListFromDataBase()) {
            models.add(new ResultModel(entity));
        }
        return models;
    }

    public void deleteAllFromTable() {
        session.createQuery("delete from ResultEntity");
    }
}
