import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ols(xs, ys):
	n = len(xs)
	a = (n * np.sum(xs * ys) - np.sum(xs) * np.sum(ys)) / (n * np.sum(xs**2) - np.sum(xs) ** 2)
	b = (np.sum(ys) - a * np.sum(xs)) / n

	return a, b

if __name__ == '__main__':
	# n = int(input("Enter n: (sample size) "))
	xs = np.array(list(map(float, input("Enter X: \n").split())))
	ys = np.array(list(map(float, input("Enter Y: \n").split())))

	# ordinary least squares
	a, b = ols(xs, ys)
	print(f"Results 1: {a} * x + {b}")
	# mse
	residuals = (ys - (a*xs + b)) ** 2
	print(f"Residuals: {residuals}")
	max_resid_arg = np.argmax(residuals)

	x, y = xs[max_resid_arg], ys[max_resid_arg]
	print(f"Point with max error: ({x}, {y})")
	xs = list(xs)
	ys = list(ys)
	xs_new = np.array(xs[:max_resid_arg] + xs[max_resid_arg + 1:])
	ys_new = np.array(ys[:max_resid_arg] + ys[max_resid_arg + 1:])
	xs = np.array(xs)
	ys = np.array(ys)
	a_new, b_new = ols(xs_new, ys_new)
	print(f"Results 2: {a_new} * x + {b_new}")

	plt.scatter(xs_new, ys_new, marker='o', c='blue', label='Initial data')
	plt.plot(xs, a * xs + b, c='brown', label='First fit')
	plt.plot(xs, a_new * xs + b_new, c='green', label='Second fit')
	plt.plot(x, y, marker='x', c='red', label='Bad point')
	plt.title("OLS Approximation")
	print("To exit from plot press Q")
	plt.legend()
	plt.show();
