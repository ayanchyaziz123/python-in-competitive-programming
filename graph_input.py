from collections import defaultdict
import sys
sys.stdin = open("input.txt", "r")
graph = defaultdict(list)
N, E = map(int, input().split())
for i in range(E):
    U, V = map(str, input().split())
    graph[U].append(V)
    graph[V].append(U)
for v in graph:
    print(v, "-->", graph[v])    