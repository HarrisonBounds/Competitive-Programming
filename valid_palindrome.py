#125. Valid Palindrome

s = "A man, a plan, a canal: Panama"

def isPalindrome(s) -> bool:
    mod_string = ""
    for element in s:
        if element.isalnum():
            mod_string += element
    
    if mod_string.lower() == mod_string[::-1].lower():
        return True
    else:
        return False

print(isPalindrome(s))