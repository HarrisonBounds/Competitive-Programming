#Use Two Pointers - Start from the middle of the substring and expand out (user cases for even and odd)

def longestPalindrome(self, s: str) -> str:
        
        #O(n^2)
        pStr = ""
        result = ""
        for i in range(len(s)):
            #odd length
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pStr = s[l:r+1]
                if len(pStr) > len(result):
                    result = pStr
                l -= 1
                r += 1

            #even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pStr = s[l:r+1]
                if len(pStr) > len(result):
                    result = pStr
                l -= 1
                r += 1

        return result
        
        
        
        #BRUTE FORCE - (O(n^3))
        
        # result = ""
        # for i in range(len(s)):
        #     valid = ""
        #     for j in range(i, len(s)):
        #         valid += s[j]
        #         print(valid)
        #         if valid == valid[::-1]:
        #             if len(valid) > len(result):
        #                 result = valid

        # return result