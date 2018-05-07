import math

def rect_rule_l(f, a, b, n):
	total = 0.0
	dx = (b-a) / n
	for k in range(0, n):
		total += f((a + (k*dx)))
	return dx * total

def rect_rule_r(f, a, b, n):
	total = 0.0
	dx = (b-a) / n
	for k in range(n, 1, -1):
		total += f((b - (k*dx)))
	return dx * total

def rect_rule_m(f, a, b, n):
	total = 0.0
	dx = (b-a) / n
	for k in range(0, n):
		total += f((a + (2*k*dx)) / 2)
	return dx * total

def trapezoidal(f, a, b, n):
	h = float(b - a) / n
	s = 0.0
	s += f(a)/2.0
	for i in range(1, n):
		s += f(a + i*h)
	s += f(b)/2.0
	return s * h

def simpson(f, a, b, n):
	if n % 2:
		raise ValueError("n must be even (received n=%d)" % n)

	h = (b - a) / n
	s = f(a) + f(b)

	for i in range(1, n, 2):
		s += 4 * f(a + i * h)
	for i in range(2, n-1, 2):
		s += 2 * f(a + i * h)

	return s * h / 3

f1 = lambda x: x**4 + x**2 - x + 7
f2 = lambda x: math.sin(x)
f3 = lambda x: x**2

if __name__ == '__main__':
	multiplier = 1
	n = input("Select n (Enter for 10000)")
	if not n:
		n = 10000
	else:
		n = int(n)
	a, b = [int(a) for a in input("Choose a, b: ").split()]
	if a > b:
		a, b = b, a
		multiplier = -1
	f = [f1, f2, f3][int(input('Choose function: \nx**4 + x**2 - x + 7 (1)\nsin(x) (2)\nx**2 (3)\n')) - 1]
	res = [rect_rule_l, rect_rule_r, rect_rule_m, trapezoidal, simpson][int(input('Choose method: \nrect_rule_l (1)\nrect_rule_r (2)\nrect_rule_m (3)\ntrapezoidal (4)\nsimpson (5)\n')) - 1](f, a, b, n)
	print(f"Result: {multiplier * res}")

