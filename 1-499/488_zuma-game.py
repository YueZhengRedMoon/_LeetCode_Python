from functools import cache


# 超时
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        self.memo = {}
        hand = ''.join(sorted(hand))
        ans = self.dfs(board, hand)
        return ans if ans != float('inf') else -1

    @cache
    def dfs(self, board: str, hand: str) -> int:
        n = len(board)
        if n == 0:
            return 0

        ans = float('inf')
        for j in range(len(hand)):
            new_hand = hand[0:j] + hand[j + 1:]
            for i in range(n):
                new_board = self.remove(board[:i] + hand[j] + board[i:], i, i)
                res = self.dfs(new_board, new_hand)
                ans = min(ans, res + 1)

        return ans

    def remove(self, board: str, x: int, y: int) -> str:
        if x < 0 or y >= len(board) or board[x] != board[y]:
            return board

        i = x
        while i >= 0 and board[i] == board[x]:
            i -= 1

        j = y
        while j < len(board) and board[j] == board[y]:
            j += 1

        # board(i, j)是相同的
        if j - i - 1 >= 3:
            return self.remove(board[0:i + 1] + board[j:], i, i + 1)
        else:
            return board


if __name__ == "__main__":
    solution = Solution()
    board = "RRYRRYYRYYRRYYRR"
    hand = "YYRYY"
    ans = solution.findMinStep(board, hand)
    print(ans)