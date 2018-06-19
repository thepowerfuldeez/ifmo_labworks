from itertools import combinations

def check(a, r):
	print(f"checking {r}")
	if not a:
		return True, None
	for set1 in combinations(a.keys(), r):
		for set2 in combinations(a.values(), r):
			if set(list(set1)) == set(list(set2)):
				return True, set1
	return False, None


if __name__ == '__main__':
	n = int(input())
	a = {}
	for _ in range(n):
		k, v = map(int, input().split())
		a[k] = v
	r = 0
	cond, set1 = check(a, r)
	while cond:
		res_set = set1
		cond, set1 = check(a, r)
		if cond:
			r += 1
	print(r)
	print(*res_set, sep='\n')

"""
20
1 3
2 3
3 2
4 4
5 2
6 3
7 5
8 4
9 3
10 9
11 3
12 4
13 9
14 10
15 13
16 7
17 8
18 11
19 17
20 19
"""