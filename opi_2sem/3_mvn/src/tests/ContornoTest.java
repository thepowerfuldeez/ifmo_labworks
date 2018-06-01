import org.junit.Test;
import static org.junit.Assert.*;
import java.io.ByteArrayOutputStream;
import lab3.Contorno;
import lab3.Punctum;

public class ContornoTest {
	@Test
	public void testCenter() {
		Contorno c1 = new Contorno(0.01);
		Contorno c2 = new Contorno(2.4);
		Contorno c3 = new Contorno(5.8);
		Punctum p = new Punctum(0.f, 0.f);

		assertTrue(c1.includes(p));
		assertTrue(c2.includes(p));
		assertTrue(c3.includes(p));
	}

	@Test
	public void testQurter1() {
		Contorno c1 = new Contorno(0.5);
		Contorno c2 = new Contorno(4.);
		Contorno c3 = new Contorno(5.6);
		Punctum p = new Punctum(2.f, 1.f);

		assertFalse(c1.includes(p));
		assertTrue(c2.includes(p));
		assertTrue(c3.includes(p));
	}

	@Test
	public void testQurter2() {
		Contorno c1 = new Contorno(0.5);
		Contorno c2 = new Contorno(4.);
		Contorno c3 = new Contorno(5.6);
		Punctum p = new Punctum(-2.2f, 1.4f);

		assertFalse(c1.includes(p));
		assertFalse(c2.includes(p));
		assertFalse(c3.includes(p));
	}

	@Test
	public void testQurter3() {
		Contorno c1 = new Contorno(2.4);
		Contorno c2 = new Contorno(10.);
		Contorno c3 = new Contorno(15.77);
		Punctum p = new Punctum(-5.f, -5.f);

		assertFalse(c1.includes(p));
		assertTrue(c2.includes(p));
		assertTrue(c3.includes(p));
	}

	@Test
	public void testQurter4() {
		Contorno c1 = new Contorno(0.4);
		Contorno c2 = new Contorno(4.48);
		Contorno c3 = new Contorno(10.6);
		Punctum p = new Punctum(2.f, -1.f);

		assertFalse(c1.includes(p));
		assertTrue(c2.includes(p));
		assertTrue(c3.includes(p));
	}
}