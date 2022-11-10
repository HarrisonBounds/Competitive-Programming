def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set() #we use a set so there isnt repeating characters

        def dfs(r, c, i): #we pass in the row position, column position, and i (where we are at in the word)
            if i == len(word):
                return True
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in path or board[r][c] != word[i]:
                return False

            path.add((r, c)) #keeps track of the positions we have visited
            #if any of these return true, then we have found the next letter
            res = (dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True  

        return False            