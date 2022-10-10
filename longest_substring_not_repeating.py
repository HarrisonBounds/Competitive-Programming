#USE a SET
#SLIDING WINDOW

def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set() #use a set becasue it cannot contain duplicates
        count = 0
        result = 0
       
        #since we are using sliding window, we will have a left pointer and a right pointer
        left = 0

        for right in range(len(s)):
            while s[right] in letterSet: #if the character we just visited is a duplicate
                letterSet.remove(s[left]) #remove the left most character
                left += 1               #increment lef tot move the window since we found a duplicate
            #after we get done checking for duplicates, we can add the character to our set
            letterSet.add(s[right])
            count = (right - left) + 1

            if count > result:
                result = count

        return result