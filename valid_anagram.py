#242. Valid Anagram
s = "anagram"
t = "nagaram"

def isAnagram(s, t) -> bool:

    if len(s) != len(t):
        return False
    
    for letter in set(s): #use a set becasue it cannot contain duplicates
        if letter not in t:
            return False
        else:
            if s.count(letter) != t.count(letter):#checks for duplicates
                return False
            
    return True

print(isAnagram(s, t))