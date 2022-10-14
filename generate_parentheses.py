#Move through problem like a tree
#always have to start with an open and end with a closed
#if open>=closed, you can only add an open
#study backtracking algorithms


def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        

        def backtrack(openCount, closeCount):
            if openCount == n and closeCount == n:
                result.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)

        return result
