from functools import cache

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        low_s = str(low)
        high_s = str(high)
        low_s = "0" * (len(high_s) - len(low_s)) + low_s

        @cache
        def f(begin: int, end: int, cnt: int, is_min: bool, is_max: bool) -> int:
            if begin > end:
                return 1

            if cnt != 0 and (cnt + end - begin + 1) % 2 != 0:
                return 0

            res = 0
            if cnt == 0 and int(low_s[begin]) == 0:
                res = f(begin + 1, end, 0, is_min, False)

            down = max(int(low_s[begin]), int(low_s[end])) if is_min else 0
            up = min(int(high_s[begin]), int(high_s[end])) if is_max else 9

            if down > up:
                return res

            cnt += 2
            for d in range(down, up + 1):
                res += f(begin + 1, end - 1, cnt, is_min and int(low_s[begin]) == d, is_max and int(high_s[begin]) == d)

            return res

        return f(0, len(high_s) - 1, 0, True, True)

