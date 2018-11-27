def check(a):
    v = set(list(a.values()))
    r = 0
    res_set = set()
    for k in a:
        if k in v:
            v.remove(k)
            res_set.add(k)
            r += 1
    return res_set, r


if __name__ == '__main__':
    n = int(input())
    a = {}
    for _ in range(n):
        k, v = map(int, input().split())
        a[k] = v

    res_set, r = check(a)
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
