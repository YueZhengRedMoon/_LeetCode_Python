from functools import cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 数位DP
        s = str(n)

        # 返回从i开始填数字，前面填的数字的集合是mask，能构造出的特殊整数的数目
        # is_limit 表示从前面填的数字是否都是n对应位上的，如果为true,那么当前位之多为int(s[i])，否则至多为'9'
        # is_num 表示前面是否填了数字（是否跳过），如果为true，那么当前位可以从0开始，如果为false，则当前可以跳过，或者从1开始填数字
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)

            res = 0
            if not is_num:
                # 选择跳过，不填数字
                res = f(i + 1, mask, False, False)

            up = int(s[i]) if is_limit else 9   # 当前可填数字的上界
            for d in range(1 - int(is_num), up + 1):
                if (mask >> d) & 1 == 0:    # mask里面没有d
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)

            return res

        return f(0, 0, True, False)
