import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import ru.ifmo.lab3.CheckHitBean;
import ru.ifmo.lab3.PointListBean;
import ru.ifmo.lab3.model.ResultModel;

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Collection;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;

@RunWith(value = Parameterized.class)
public class CheckHitBeanTest {
    private PointListBean service;
    private CheckHitBean bean;

    private BigDecimal x;
    private BigDecimal y;
    private BigDecimal r;
    private boolean inArea;

    public CheckHitBeanTest(BigDecimal x, BigDecimal y, BigDecimal r, boolean inArea) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.inArea = inArea;
    }

    @Before
    public void setup() {
        service = mock(PointListBean.class);

        bean = new CheckHitBean();
        bean.setService(service);
    }

    @After
    public void after() {
        bean = null;
    }

    @Parameterized.Parameters
    public static Collection primeNumbers() {
        return Arrays.asList(new Object[][]{
                {new BigDecimal(5), new BigDecimal(6), new BigDecimal(3), false},
                {new BigDecimal(1.5), new BigDecimal(3), new BigDecimal(3), true},
                {new BigDecimal(1.5), new BigDecimal(0), new BigDecimal(3), true},

                {new BigDecimal(-1), new BigDecimal(2), new BigDecimal(5), true},
                {new BigDecimal(-4), new BigDecimal(2), new BigDecimal(4), false},

                {new BigDecimal(-1), new BigDecimal(-1), new BigDecimal(5), true},
                {new BigDecimal(-5), new BigDecimal(-3), new BigDecimal(1), false},

        });
    }

    @Test
    public void testAreaChecking() {
        bean.checkHit(x, y, r);
        verify(service).addModel(new ResultModel(x, y, r, inArea));
    }

}
