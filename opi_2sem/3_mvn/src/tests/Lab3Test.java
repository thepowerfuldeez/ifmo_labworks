import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;
import static org.junit.Assert.assertEquals;
import static org.junit.runners.Parameterized.*;

import java.io.IOException;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;
import java.io.ByteArrayInputStream;
import java.util.Arrays;
import java.util.Collection;


import lab3.Lab3;

@RunWith(Parameterized.class)
public class Lab3Test {
	@Parameter(0)
	public String input;
	@Parameter(1)
	public String expected;

	@Parameters
    public static Collection<Object[]> data() {
        Object[][] data = new Object[][] {
        	{"0", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; 4,0}%n  {-1,0; -1,0}%n  {2,0; 1,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n  {2,0; -1,0}%n")},
        	{"0.5", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; 4,0}%n  {-1,0; -1,0}%n  {2,0; 1,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n  {2,0; -1,0}%n")},
        	{"2", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; 4,0}%n  {2,0; 1,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n  {2,0; -1,0}%n")},
        	{"4", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; 4,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n  {2,0; -1,0}%n")},
        	{"4.48", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; 4,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n")},
        	{"8", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; -5,0}%n  {4,0; -4,0}%n  {-5,0; 3,0}%n")},
        	{"10", String.format("Enter a number: Points not included in the defined area are:%n  {4,0; -4,0}%n  {-5,0; 3,0}%n")},
        	{"11.32", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; 3,0}%n")},
        	{"12", String.format("Enter a number: Points not included in the defined area are:%n  {-5,0; 3,0}%n")},
        	{String.format("fwef%n12"), String.format("Enter a number: Entered string is not a number, try again.%nEnter a number: Points not included in the defined area are:%n  {-5,0; 3,0}%n")},
        	{String.format("-1%n12"), String.format("Enter a number: Radius cant't be negative, try again.%n Enter a number: Points not included in the defined area are:%n  {-5,0; 3,0}%n")}
        };
        return Arrays.asList(data);
    }

	@Test
	public void testLab3() throws IOException {
		Lab3 l3 = new Lab3();
		ByteArrayOutputStream out = new ByteArrayOutputStream();
		ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes());

		System.setOut(new PrintStream(out));
		System.setIn(in);
		String[] args = new String[] {};

		l3.main(args);

		assertEquals("Check input " + input, expected, out.toString());
	}
}