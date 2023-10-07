from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        suf = [0] * (n + 1)     # 后缀和，大小多加1以便于处理后缀为空的情况
        st = [n]                # 严格单调递增栈，栈中存放maxHeights的下标，栈中存放一个哨兵
        s = 0                   # 元素和
        for i in range(n - 1, - 1, -1):     # 从右往左遍历maxHeights数组
            x = maxHeights[i]   # 当前遍历到的山峰
            while len(st) > 1 and x <= maxHeights[st[-1]]:     # 栈不为空，且当前山峰小于等于栈顶
                j = st.pop()    # 弹出栈顶，山峰的右侧必须是单调不递增的
                s -= maxHeights[j] * (st[-1] - j)   # 减去去掉的山的部分的元素和
            s += x * (st[-1] - i)   # 加上新增的山的部分的元素和
            suf[i] = s
            st.append(i)

        ans = s
        st = [-1]
        pre = 0
        for i, x in enumerate(maxHeights):
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()
                pre -= maxHeights[j] * (j - st[-1])
            pre += x * (i - st[-1])
            ans = max(ans, pre + suf[i + 1])
            st.append(i)

        return ans
