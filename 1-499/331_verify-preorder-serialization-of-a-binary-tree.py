class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True

        nodes = preorder.split(',')
        stack = []
        for i in range(0, len(nodes)):
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#':
                if stack[-3] != '#':
                    stack[-3] = '#'
                    stack.pop()
                    stack.pop()
                else:
                    return False
            if nodes[i] == '#' and len(stack) == 0:
                return False
            stack.append(nodes[i])

        while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#':
            if stack[-3] != '#':
                stack[-3] = '#'
                stack.pop()
                stack.pop()
            else:
                return False

        return len(stack) == 1 and stack[0] == '#'

if __name__ == "__main__":
    solution = Solution()
    ans = solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(ans)