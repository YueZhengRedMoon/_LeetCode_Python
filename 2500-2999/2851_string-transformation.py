from typing import List

class Solution:
    '''
    f[i][0]:s经过i次操作变成t的方案数
    f[i][1]:s经过i次操作后，没有变成t的方案数

    操作相当于循环右移，为了方便求s循环右移几次可以得到t，可以将s复制一份接在s后面，即s+s，记为s2，
    然后使用字符串匹配算法，例如KMP算法，在其中寻找t的出现次数

    f[i-1][0] -> f[i][0]:
        - 有c-1种方案，其中c为t在s2[0:-1]中的出现次数，
          例如s和t都为"ababab","ababab,ababa"中出现了3次“ababab"，相当于按这几种方式操作: "ab|abab", "abab|ab"。
    f[i-1][1] -> f[i][0]:
        - 有c种方案，例如"bababa"要变成"ababab"，有这几种操作方法: "babab|a", "bab|aba", "b|ababa"。
    f[i-1][1] -> f[i][1]:
        - 有c-1种方案使不等于t的串变成等于t的串，总共有n-1种操作方法，所以有n-1-c种方法使不等于t的串变为不等于t的串。
    f[i-1][0] -> f[i][1]:
        - 同理，有n-1-(c-1) = n-c 中方案使等于t的串变为不等于t的串。

    综上，可以得到状态转移方程:
    f[i][0] = f[i-1][0] * (c-1) + f[i-1][1] * c
    f[i][1] = f[i-1][0] * (n-c) + f[i-1][1] * (n-1-c)

    上式可以转换为矩阵的乘法:
    | f[k][0] | = | c-1 c     | . | f[k-1][0] | = ... = | c-1 c     |^k . | f[0][0] |
    | f[k][1] |   | n-c n-1-c |   | f[k-1][1] |         | n-c n-1-c |     | f[0][1] |

    其中矩阵的幂，可以使用快速幂算法在O(logn)的时间内求出。

    初始化:
    如果s==t,则f[0][0] = 1, f[0][1] = 0;
    如果s!=t,则f[0][0] = 0, f[0][1] = 1;

    设最终的结果矩阵为m,如果s==t,则答案为m[0][0],否则,答案为m[0][1]
    '''

    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        c = self.kmp_search(s + s[:-1], t)
        m = [
            [c - 1, c],
            [n - c, n - 1 - c]
        ]
        m = self.pow(m, k)
        return m[0][s != t]

    # KMP模板，计算next数组
    def calc_max_match(self, s: str) -> List[int]:
        match = [0] * len(s)
        c = 0
        for i in range(1, len(s)):
            v = s[i]
            while c and s[c] != v:
                c = match[c - 1]
            if s[c] == v:
                c += 1
            match[i] = c
        return match

    # KMP模板，返回text中出现了多少次pattern
    def kmp_search(self, text: str, pattern: str) -> int:
        match = self.calc_max_match(pattern)
        match_cnt = c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = match[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                match_cnt += 1
                c = match[c - 1]
        return match_cnt

    # 矩阵乘法
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % (10 ** 9 + 7)
        return c

    # 矩阵快速幂
    def pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        res = [[1, 0], [0, 1]]  # 单位矩阵
        while n:
            if n % 2:
                res = self.multiply(res, a)
            a = self.multiply(a, a)
            n //= 2
        return res
