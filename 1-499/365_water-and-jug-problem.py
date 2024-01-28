class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        memo = set()

        def dfs(jug1: int, jug2: int) -> bool:
            if (jug1, jug2) in memo:
                return False

            if jug1 + jug2 == targetCapacity:
                return True

            # 记录当前状态
            memo.add((jug1, jug2))

            # 装满水壶1
            if jug1 != jug1Capacity and dfs(jug1Capacity, jug2):
                return True

            # 装满水壶2
            if jug2 != jug2Capacity and dfs(jug1, jug2Capacity):
                return True

            # 清空水壶1
            if jug1 != 0 and dfs(0, jug2):
                return True

            # 清空水壶2
            if jug2 != 0 and dfs(jug1, 0):
                return True

            # 水壶1倒向水壶2
            if jug1 > 0 and jug2 != jug2Capacity:
                water = min(jug1, jug2Capacity - jug2)
                if dfs(jug1 - water, jug2 + water):
                    return True

            # 水壶2倒向水壶1
            if jug2 > 0 and jug1 != jug1Capacity:
                water = min(jug1Capacity - jug1, jug2)
                if dfs(jug1 + water, jug2 - water):
                    return True

            return False

        return dfs(0, 0)



