from collections import defaultdict
# from heapq import *

# def dijkstra(edges, f, t):
#     g = defaultdict(list)
#     for l,r,c in edges:
#         g[l].append((c,r))
#     q, seen = [(0,f,())], set()
#     while q:
#         (cost,v1,path) = heappop(q)
#     if v1 not in seen:
#         seen.add(v1)
#         path = (v1, path)
#     if v1 == t: 
#         return (cost, path)
#     for c, v2 in g.get(v1, ()):
#         if v2 not in seen:
#             heappush(q, (cost+c, v2, path))
#     return float("inf")

# if __name__ == "__main__":
#     edges = [
#         ("A", "B", 7),
#         ("A", "D", 5),
#         ("B", "C", 8),
#         ("B", "D", 9),
#         ("B", "E", 7),
#         ("C", "E", 5),
#         ("D", "E", 15),
#         ("D", "F", 6),
#         ("E", "F", 8),
#         ("E", "G", 9),
#         ("F", "G", 11)
#     ]
# print("=== Dijkstra ===")
# print(edges)
# print("A -> E:")
# print(dijkstra(edges, "A", "E"))
# print("F -> G:")
# print(dijkstra(edges, "F", "G"))



import heapq

def dijkstra(adj, costs, s, t, capacity=5):
    ''' Return predecessors and min distance if there exists a shortest path 
        from s to t; Otherwise, return None '''
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        if len(Q) >= capacity:
            spilled = heapq.heappushpop(Q, item)
            # print(spilled)
        else:
            heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
        # print(Q)
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            # print('visit:', u)
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost


import numpy as np
import random
def gen_graph(n, m=10, q=1, r=1e6):
    # m = n * n / 10
    # m = n * n
    g = defaultdict(list)
    for k in range(1, n + 1):
        # g[k] = np.random.choice(n, n // m)
        g[k] = [random.randint(1, n) for _ in range(n // m)]
    
    cost = {}
    for a, b in g.items():
        for c in b:
            cost[(a, c)] = random.randint(q, r)
    return g, cost

import time


def benchmark(n, m=10):
    g, cost = gen_graph(n, m)
    cost = make_undirected(cost)

    s, t = 1, 7
    t1 = time.time()
    predecessors, min_cost = dijkstra(g, cost, s, t, 5)

    # c = t
    # path = [c]
    # print('min cost:', min_cost)
    t1 = time.time() - t1
    # while predecessors.get(c):
    #     path.insert(0, predecessors[c])
    #     c = predecessors[c]

    # print('shortest path:', path)

    t3 = time.time()
    predecessors, min_cost = dijkstra(g, cost, s, t, 6)

    # print('min cost:', min_cost)
    t2 = time.time() - t3
    return t1, t2

if __name__=='__main__':
    for n in range(4500, 10001, 500):
        print(n)
        t1_ = []
        t2_ = []
        for _ in range(2):
            try:
                t1, t2 = benchmark(n, 10)
                t1_.append(t1)
                t2_.append(t2)
            except:
                pass
        if t1_ and t2_:
            print(np.mean(t1_), np.mean(t2_))
    for n in range(4500, 10001, 500):
        print(n)
        t1_ = []
        t2_ = []
        for _ in range(2):
            try:
                t1, t2 = benchmark(n, 1)
                t1_.append(t1)
                t2_.append(t2)
            except:
                pass
            print(np.mean(t1_), np.mean(t2_))

    # adj = { 1: [2,3,6],
    #         2: [1,3,4],
    #         3: [1,2,4,6],
    #         4: [2,3,5,7],
    #         5: [4,6,7],
    #         6: [1,3,5,7],
    #         7: [4,5,6]}

    # cost = { (1,2):7,
    #         (1,3):9,
    #         (1,6):14,
    #         (2,3):10,
    #         (2,4):15,
    #         (3,4):11,
    #         (3,6):2,
    #         (4,5):6,
    #         (5,6):9,
    #         (4,7):2,
    #         (5,7):1,
    #         (6,7):12}

    # s, t = 1, 7
    # predecessors, min_cost = dijkstra(adj, cost, s, t, 5)

    # c = t
    # path = [c]
    # print('min cost:', min_cost)
    # while predecessors.get(c):
    #     path.insert(0, predecessors[c])
    #     c = predecessors[c]

    # print('shortest path:', path)



# 1700
# 0.31527868906656903 0.3118693033854167
# 0.493225892384847 0.5655759970347086
# 0.29502105712890625 0.5142440795898438
# 0.6154301961263021 0.5326009591420492
# 0.35276373227437335 0.47057032585144043
# 0.5357812245686849 0.5072263876597086
# 0.8708019256591797 0.8300882975260416
# 0.5812235673268636 0.518105665842692
# 0.7008922894795736 0.7494751612345377
# 0.7949924468994141 0.7880473136901855
# 1.1634939908981323 1.2103888988494873
# 1.2510950565338135 1.2735601663589478
# 1.3784143129984539 1.4307483037312825
# 1.4821279843648274 1.442074219385783
# 1.3620984554290771 1.548264980316162
# 1.6099689801534016 1.617055336634318
# 1.6395799318949382 1.7931052843729656
# 1.7998727957407634 1.934468189875285
# 3500
# 1.9043269157409668 2.44659423828125
# 3600
# 2.190213998158773 2.3760294914245605
# 3800
# 2.754120111465454 2.779986619949341
# 3900
# 2.7945239543914795 3.057401657104492
# 4000
# 2.1833509604136148 1.918514569600423
# 4100
# 2.637437661488851 2.6329426765441895
# 4200
# 1.7836956183115642 2.178481340408325
# 4300
# 2.2699552377065024 2.505746285120646
# 4400


#     