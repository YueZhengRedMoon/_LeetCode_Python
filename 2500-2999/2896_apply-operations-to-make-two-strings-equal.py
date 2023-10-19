from functools import cache
import math

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        # 反转两个字符的操作无法改变字符串中1的个数的奇偶性，
        # 如果s1和s2的'1'的个数的奇偶性不同，则s1不可能转变为s2
        if s1.count('1') % 2 != s2.count('1') % 2:
            return -1

        # s1和s2中'1'的个数的奇偶性相同，一定可以通过若干次操作将s1变为s2
        # 从右到左遍历字符串，对于s1[i]和s2[i]:
        #   - 如果s1[i] == s2[i]，则无需反转
        #   - 如果s1[i] != s2[i]，则可以进行以下操作：
        #       1.花费x的代价反转s1[i]，同时记录该操作的次数（记作j）
        #       2.如果j>0，表示此前进行了一次代价为x的反转操作，此次反转操作的代价相当于0
        #       3.花费代价1反转s1[i]和s1[i-1]，用一个bool变量pre_rev记录该操作，
        #         当在遍历到s1[i]时，如果发现pre_rev == true，则表明在s1[i+1]进行了代价为1的反转操作，现在需要反转s1[i]

        @cache
        def dfs(i: int, j: int, pre_rev: bool) -> int:
            # 已经遍历完了所有字符
            if i < 0:
                # 还有未消耗完的反转次数，该状态不合法
                if j > 0 or pre_rev:
                    return math.inf
                # 转换完成，不再有字符需要反转
                return 0

            # 当 当前字符相等((s1[i] == s2[i]) == True)且s1[i+1]没有进行代价为1的反转操作((not pre_rev) == True)
            # 或 当前字符不相等((s1[i] == s2[i]) == False)且s1[i+1]进行了代价为1的反转操作((not pre_rev) == False)
            # 时，当前字符不需要进行反转操作
            if (s1[i] == s2[i]) == (not pre_rev):
                return dfs(i - 1, j, False)

            # 第一种操作：进行一次代价为x的翻转操作
            res1 = dfs(i - 1, j + 1, False) + x
            # 第二种操作：进行一次代价为1的翻转操作
            res2 = dfs(i - 1, j, True) + 1
            res = min(res1, res2)
            # 使用“免费”的反转操作
            if j > 0:
                res3 = dfs(i - 1, j - 1, False)
                res = min(res, res3)

            return res

        return dfs(len(s1) - 1, 0, False)
