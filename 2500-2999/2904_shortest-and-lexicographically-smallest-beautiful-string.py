class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = "2"
        ans_len = n

        i = 0
        while i < n and s[i] == '0':
            i += 1
        cnt = 0
        for j in range(i, n):
            if s[j] == '1':
                if cnt == k:
                    i += 1
                    while s[i] != '1':
                        i += 1
                else:
                    cnt += 1

                if cnt == k:
                    cur_len = j + 1 - i
                    if cur_len < ans_len:
                        ans = s[i:j + 1]
                        ans_len = cur_len
                    elif cur_len == ans_len:
                        ans = min(ans, s[i:j + 1])

        return "" if ans == "2" else ans
