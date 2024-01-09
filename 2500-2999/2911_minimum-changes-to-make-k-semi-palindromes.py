# 预处理n的所有真因子d, 真因子: 1 <= d < n并且n % d == 0
MAX_N = 201
divisors = [[] for _ in range(MAX_N)]
for i in range(1, MAX_N):
    for j in range(i * 2, MAX_N, i):
        divisors[j].append(i)

# 将字符串s（s的长度至少为2）变成半回文串所需要的最少修改次数,O(nlogn)
def get_modify(s: str) -> int:
    n = len(s)
    min_cnt = inf
    for d in divisors[n]:   # 枚举字符串s的长度n的每一个真因子d, O(logn)
        cnt = 0
        for i in range(d):  # d个半回文串的起始索引, O(n)
            t = s[i::d]     # t = s[i] + s[i+d] + s[i+2*d] + ...
            # 计算将t变为回文串需要的修改次数
            for j in range(len(t) // 2):
                cnt += (t[j] != t[-1 - j])
        if cnt < min_cnt:
            min_cnt = cnt
    return min_cnt

class Solution:
    '''
    划分型DP
    dfs(i, j)
    i 定义成剩余需要切割的次数，i+1就是切出来的子串的个数
    j 从s[0]到s[j]是现在需要切割的部分
    返回值 修改的最少字符数目
    枚举当前这一段的左端点L
        - L最小是2 * i，因为半回文串的长度至少为2，如果还需要切割i次，会切出i+1个子串，
          去除当前得到的子串还有i个子串，即至少还需要2 * i长度来切剩下的串
        - L最大是j-1，即当前切出的子串为s[j-1:j]
    设 modify[i][j] = s[i:j]的最小修改次数
    dfs(i, j) <- min dfs(i-1, L-1) + modify[L][j]
    递归终点：i=0 return modify[0][j]
    递归入口：dfs(k-1, n-1)
    '''

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # 预处理modify数组
        modify = [[0] * n for _ in range(n)]
        for left in range(n - 1):
            for right in range(left + 1, n):
                modify[left][right] = get_modify(s[left:right + 1])

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return modify[0][j]
            res = inf
            for L in range(i * 2, j):
                res = min(res, dfs(i - 1, L - 1) + modify[L][j])
            return res

        return dfs(k - 1, n - 1)

