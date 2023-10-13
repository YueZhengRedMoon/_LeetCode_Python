from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        def dfs(x: int, fa: int) -> int:
            s = values[x]
            for y in g[x]:
                if y != fa:
                    s += dfs(y, x)
            nonlocal ans
            ans += (s % k == 0)
            return s
        dfs(0, -1)

        return ans
