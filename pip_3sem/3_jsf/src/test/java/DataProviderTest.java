import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import ru.ifmo.lab3.database.ResultRepository;
import ru.ifmo.lab3.model.ResultModel;

import java.util.List;

public class DataProviderTest {
    private ResultRepository repository;

    @Before
    public void init() {
        repository = new ResultRepository();
    }

    @After
    public void dispose() {
        repository.closeSession();
    }

    @Test
    public void storePoint() {
        repository.store(new ResultModel(0, 0, 0, true));
    }

    @Test
    public void getPoint() {
        List<ResultModel> results = repository.get();
        Assert.assertNotNull(results);
    }
}
