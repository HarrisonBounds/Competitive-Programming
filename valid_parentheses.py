def isValid(self, s: str) -> bool:
        
        stack = []
        d= {"(" : ")", "{" : "}", "[" : "]"}

        for element in s:
            if element in d.keys():
                stack.append(element)
            
            if element in d.values():
                if len(stack) == 0:
                    return False
                opener = stack[-1]

                if d[opener] == element:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
                    