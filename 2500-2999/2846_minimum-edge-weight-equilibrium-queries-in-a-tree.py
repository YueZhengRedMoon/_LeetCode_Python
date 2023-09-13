from typing import List

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 建图
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w - 1))
            g[y].append((x, w - 1))

        # 树上倍增数组
        m = n.bit_length()  # 总共有n个节点，则树中每个节点最多有2^log(n)个祖先
        pa = [[-1] * m for _ in range(n)]   # pa[x][i]: 从x出发经过2^i个节点后到达的节点
        cnt = [[[0] * 26 for _ in range(m)] for _ in range(n)]  # cnt[x][i][w]: 从x出发到x的第2^i个祖先节点经过的边中权值为w的边的数量
        depth = [0] * n

        # x: 当前dfs遍历到的节点, fa: 当前节点x的父节点
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa                   # 初始化树上倍增算法中x的父节点
            for y, w in g[x]:               # 遍历与x连接的边, 它们将是x的子节点
                if y != fa:                 # 避免将父节点作为子节点
                    cnt[y][0][w] = 1
                    depth[y] = depth[x] + 1
                    dfs(y, x)

        dfs(0, -1)  # 无向树中任何一个节点都可以作为根节点, 将0号节点作为根节点, 其父节点被视为-1

        # 树上倍增
        for i in range(m - 1):  # 枚举经过的节点数
            for x in range(n):  # 枚举出发的节点
                p = pa[x][i]
                if p != -1:
                    pa[x][i + 1] = pa[p][i]
                    # 计算从x出发, 经过2^(i+1)个节点后经过的边的权值的种数
                    for j, (c1, c2) in enumerate(zip(cnt[x][i], cnt[p][i])):
                        cnt[x][i + 1][j] = c1 + c2

        ans = []
        for x, y in queries:
            path_len = depth[x] + depth[y]  # 从x到y经过的路径长度(边的数量)，最后要减去2 * depth[lca], lca是x与y的最近公共祖先
            cw = [0] * 26
            # 为便于统一处理，使x的深度小于y的深度
            if depth[x] > depth[y]:
                x, y = y, x

            # 使x, y 在同一深度
            k = depth[y] - depth[x] # y比x深k层
            for i in range(k.bit_length()):
                if (k >> i) & 1:    # 二进制位从低到高第i位是1
                    p = pa[y][i]
                    # 在y向上走的时候记录经过的边的权值的种数
                    for j, c in enumerate(cnt[y][i]):
                        cw[j] += c
                    y = p

            # 现在x, y在同一深度，如果它们不相同，则同步向上找x与y的最近公共祖先
            if y != x:
                for i in range(m - 1, -1, -1):
                    px, py = pa[x][i], pa[y][i]
                    if px != py:
                        for j, (c1, c2) in enumerate(zip(cnt[x][i], cnt[y][i])):
                            cw[j] += c1 + c2
                        x, y = px, py   # 同时向上跳2^i步
                for j, (c1, c2) in enumerate(zip(cnt[x][0], cnt[y][0])):
                    cw[j] += c1 + c2
                x = pa[x][0]

            lca = x # 最近公共祖先
            path_len -= depth[lca] * 2
            ans.append(path_len - max(cw))

        return ans
