from collections import defaultdict

fact = [1] * 20001
mod = 10 ** 9 + 7

for i in range(2, 10001):
    fact[i] = fact[i - 1] * i % mod
    fact[-i] = pow(fact[i], mod - 2, mod)

class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1

        vs = list(cnt.values())
        mx = max(vs)
        ans = 0

        for p in range(1, mx + 1):
            cur = 1
            for v in vs:
                cur = cur * (self.comb(v, p) + 1) % mod
            ans = (ans + cur - 1) % mod

        return ans

    def comb(self, n: int, m: int) -> int:
        if n < m:
            return 0
        return fact[n] * fact[-m] * fact[m - n] % mod

