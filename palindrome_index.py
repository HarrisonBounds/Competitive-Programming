#Determine if an index of the string can be removed to make the string a palindrome
#if the string is alreadya plaidrome, return -1
#else, return the index of the letter to remove


def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    
    n = len(s)
    
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n - 1 - i
            elif s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i