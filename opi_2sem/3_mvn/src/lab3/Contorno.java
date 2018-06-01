package lab3;

public class Contorno {
	Double r;

	public Contorno(Double r) {
		this.r = r;
	}

	public boolean includes(Punctum p) {
		if (p.x >= 0 && p.x <= r/2 && p.y > 0 && p.y < r ||
		    p.x >= 0 && p.y <= 0 && (p.x*p.x + p.y*p.y) <= r*r/4 ||
		    p.x <= 0 && p.y <= 0 && p.y >= -p.x - r)
		{
			return true;
		}
		else
			return false;
	}
}