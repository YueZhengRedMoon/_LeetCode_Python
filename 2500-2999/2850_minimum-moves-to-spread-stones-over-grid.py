from itertools import permutations
from math import inf
from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        from_ = []
        to = []
        for i, row in enumerate(grid):
            for j, cnt in enumerate(row):
                # 移出石头的总量和移入石头的总量是相同的，所以from_数组和to数组的长度一定是相同的
                if cnt > 1:
                    from_.extend([(i, j)] * (cnt - 1))
                elif cnt == 0:
                    to.append((i, j))

        ans = inf
        for from2 in permutations(from_):
            total = 0
            for (x1, y1), (x2, y2) in zip(from2, to):
                total += abs(x1 - x2) + abs(y1 - y2)
            ans = min(ans, total)
        return ans

# 错误
class Solution2:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        deltas = [[(1, 0), (0, 1), (-1, 0), (0, -1)],
                  [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 2), (0, -2), (2, 0), (-2, 0)],
                  [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]]

        ans = 0
        for move, delta in enumerate(deltas, 1):
            for i in range(3):
                for j in range(3):
                    if grid[i][j] > 1:
                        for dx, dy in delta:
                            x = i + dx
                            y = j + dy
                            if (0 <= x < 3) and (0 <= y < 3) and grid[x][y] == 0:
                                ans += move
                                grid[i][j] -= 1
                                grid[x][y] = 1
                                print("move ({}, {}) to ({}, {}) with {}".format(i, j, x, y, move))
                                if grid[i][j] == 1:
                                    break

        def diagonal(fx: int, fy: int, tx: int, ty: int) -> int:
            if grid[fx][fy] > 1 and grid[tx][ty] == 0:
                grid[fx][fy] -= 1
                grid[tx][ty] = 1
                return 4
            return 0

        ans += diagonal(0, 0, 2, 2)
        ans += diagonal(0, 2, 2, 0)
        ans += diagonal(2, 0, 0, 2)
        ans += diagonal(2, 2, 0, 0)

        return ans

if __name__ == "__main__":
    solution = Solution()
    grid = [[4, 0, 0], [0, 0, 2], [3, 0, 0]]
    ans = solution.minimumMoves(grid)
    print(ans)
    print(grid)
