# #super_digit(9875)   	9+8+7+5 = 29 
# 	super_digit(29) 	2 + 9 = 11
# 	super_digit(11)		1 + 1 = 2
# 	super_digit(2)		= 2  


#Brute Force
# def superDigit(n, k):
    
#     n = n * k
    
#     while True:
#         total = 0
    
#         for i in range(len(n)):
#             total = total + int(n[i])
            
#         n = str(total)
#         if len(n) == 1:
#             break
    
#     return int(n)

def superDigit(n, k):
    
    def helper(n):
        total = 0
        for i in range(len(n)):
            total += int(n[i])
        total = str(total)
            
        if len(total) == 1:
            return total
        else:
            return helper(total)
        
    n = str(helper(n) * k) ###UNDESTAND
    
    return helper(n)