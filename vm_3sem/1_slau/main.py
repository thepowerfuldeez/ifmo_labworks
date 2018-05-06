import numpy as np
from math import sqrt
np.seterr("ignore")

def seidel(A, b, eps):
	"""
	:param: A – матрица коэффициентов
	:param: b – столбец свободных членов
	:param: eps – точность
	"""
	MAX_ITERATIONS = 10000
	n = len(A)
	x = np.zeros(n)

	converge = False
	cur_iter = 0
	while not converge:
		cur_iter += 1
		if cur_iter > MAX_ITERATIONS:
			return None, None, None
		x_new = np.copy(x)
		for i in range(n):
			s1 = np.sum([np.nan_to_num(A[i][j] * x_new[j]) for j in range(i)])
			s2 = np.sum([np.nan_to_num(A[i][j] * x[j]) for j in range(i + 1, n)])
			# итерационный шаг
			x_new[i] = np.nan_to_num(np.divide((b[i] - s1 - s2), A[i][i]))

		# столбец погрешностей
		norm = np.nan_to_num(x_new - x)
		# условие на выход из цикла
		converge = np.sqrt(np.sum(norm ** 2)) <= eps
		x = x_new

	return x, norm.tolist(), cur_iter

if __name__ == '__main__':
	n = input("Введите размерность: (Enter для 2): ")
	if not n:
		n = 2
	n = int(n)

	eps = input("Введите точность (Enter для 1e-13): ")
	if not eps:
		eps = 1e-13
	eps = float(eps)

	if input("Хотите ввести свои значения коэффициентов? д/н ")[0].lower() == "д":
		matrix = []
		for _ in range(n):
			matrix.append(list(map(float, input().split())))
		vector = list(map(float, input().split()))
		x, norm, n_iter = seidel(matrix, vector, eps)
		if x is not None:
			x_format = ', '.join([f"{a:.4E}" for a in x])
			print(f"Итеративный процесс сходится к [{x_format}].")
			print(f"Заняло {n_iter} итераций.")
			norm_format = ', '.join([f"{a:.4E}" for a in norm])
			print(f"Столбец погрешностей: [{norm_format}].")
		else:
			print("Итеративный процесс не сошелся")
		print()
	else:
		if input("Хотите использовать случайные значения коэффициентов? д/н ")[0].lower() == "д":
			matrix = np.random.random((n, n)) * 10
			vector = np.random.random(n) * 10
			print("\n".join([" ".join(list(map(str, a))) for a in matrix]))
			print(vector)
			x, norm, n_iter = seidel(matrix, vector, eps)
			if x is not None:
				x_format = ', '.join([f"{a:.4E}" for a in x])
				print(f"Итеративный процесс сходится к [{x_format}].")
				print(f"Заняло {n_iter} итераций.")
				norm_format = ', '.join([f"{a:.4E}" for a in norm])
				print(f"Столбец погрешностей: [{norm_format}].")
			else:
				print("Итеративный процесс не сошелся")
			print()
		else:
			matrix2 = [
			[1, 2],
			[0, 0]]
			vector2 = [3, 0]

			matrix6 = [
			[15, 1, -6, 2, 1, 4],
			[1, 40, 3, -8, 4, 3],
			[2, 7, 62, 4, -7, 3],
			[1, 3, 1, 48, 3, -5],
			[4, 7, 5, 5, 99, 6],
			[1, 1, 1, 1, 1, -7]]
			vector6 = [0, 2, 1, 1, 4, -8]

			n, eps = 6, 1e-13
			x, norm, n_iter = seidel(matrix6, vector6, eps)
			x_format = ', '.join([f"{a:.4E}" for a in x])
			print(f"Итеративный процесс сходится к [{x_format}].")
			print(f"Заняло {n_iter} итераций.")
			norm_format = ', '.join([f"{a:.4E}" for a in norm])
			print(f"Столбец погрешностей: [{norm_format}].")
			print()
			n, eps = 2, 1e-13
			x, norm, n_iter = seidel(matrix2, vector2, eps)
			x_format = ', '.join([f"{a:.4E}" for a in x])
			print(f"Итеративный процесс сходится к [{x_format}].")
			print(f"Заняло {n_iter} итераций.")
			norm_format = ', '.join([f"{a:.4E}" for a in norm])
			print(f"Столбец погрешностей: [{norm_format}].")
			print()
