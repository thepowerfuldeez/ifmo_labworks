import numpy as np

def gaussSeidel(A, b, x, N, tol):
	"""
	:param: A – матрица коэффициентов
	:param: b – столбец свободных членов
	:param: x – начальное приближение
	:param: N – итоговая размерность
	:param: tol – точность
	"""

	# максимальное кол-во допустимых итераций
	MAX_ITERATIONS = 1000000
	EPSILON = 1e-13

    # инициализируем список ответов нулями
	xprev = [0.0 for i in range(N)]
	for i in range(MAX_ITERATIONS):
    	# заполняем значениями из x
		for j in range(N):
			xprev[j] = x[j]
        # накапливаем сумму
		for j in range(N):
			summ = 0.0
			for k in range(N):
				if (k != j):
					summ += A[j][k] * x[k]
			x[j] = (b[j] - summ) / (A[j][j] + EPSILON)

		diff1norm = []
		oldnorm = []
		for j in range(N):
			diff1norm.append(abs(x[j] - xprev[j]))
			oldnorm.append(abs(xprev[j]))
		if sum(oldnorm) == 0.0:
			norm = diff1norm
		else:
			norm = [a / (b + EPSILON) for a, b in zip(diff1norm, oldnorm)]

		# выход из цикла – проверка условия на погрешность
		if (sum(norm) < tol) and i != 0:
			x_format = ', '.join([f"{a:.4E}" for a in x])
			print(f"Итеративный процесс сходится к [{x_format}].")
			print(f"Заняло {i + 1} итераций.")
			norm_format = ', '.join([f"{a:.4E}" for a in norm])
			print(f"Столбец погрешностей: [{norm_format}].")
			return
	print("Итеративный процесс не сошелся.")

if __name__ == '__main__':
	n = input("Введите размерность: (Enter для 2): ")
	if not n:
		n = 2
	n = int(n)

	tol = input("Введите точность (Enter для 1e-13): ")
	if not tol:
		tol = 1e-13
	tol = float(tol)

	if input("Хотите ввести свои значения коэффициентов? д/н ")[0].lower() == "д":
		matrix = []
		for _ in range(n):
			matrix.append(list(map(float, input().split())))
		vector = list(map(float, input().split()))
	else:
		if input("Хотите использовать случайные значения коэффициентов? д/н ")[0].lower() == "д":
			matrix = np.random.random((n, n)).tolist()
			vector = np.random.random(n).tolist()
			print("\n".join([" ".join(list(map(str, a))) for a in matrix]))
			print(vector)
			gaussSeidel(matrix, vector, np.zeros(n).tolist(), n, tol)
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

			n, tol = 6, 1e-13
			gaussSeidel(matrix6, vector6, np.zeros(n).tolist(), n, tol)
			print()
			n, tol = 2, 1e-13
			gaussSeidel(matrix2, vector2, np.zeros(n).tolist(), n, tol)
			print()
