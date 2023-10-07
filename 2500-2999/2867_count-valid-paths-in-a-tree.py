from math import isqrt
from typing import List

MAX_N = 10 ** 5 + 1
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i + i, MAX_N, i):
            is_prime[j] = False

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> None:
            nodes.append(x)
            for y in g[x]:
                if y != fa and not is_prime[y]:
                    dfs(y, x)

        ans = 0
        size = [0] * (n + 1)
        for x in range(1, n + 1):
            if not is_prime[x]:
                continue
            s = 0
            for y in g[x]:
                if is_prime[y]:
                    continue
                if size[y] == 0:
                    nodes = []
                    dfs(y, -1)
                    for z in nodes:
                        size[z] = len(nodes)
                ans += size[y] * s
                s += size[y]
            ans += s

        return ans
