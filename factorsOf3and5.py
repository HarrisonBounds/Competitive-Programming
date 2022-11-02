#Factors of 3 and 5 - An ideal number is a positive integer with only 3 and 5 as its prime divisors. 
#It can be expressed in the form of 3^x * 5^y (15, 45, and 75 are ideal numbers, but 6, 10, and 21 are not)
#Find the number of ideal integers within the given segment (low, high)

# Function to count the number within
# a range whose prime factors are only 3 and 5
def findTwoThreePrime(l, r) :
 
    # Start with 2 so that 1
    # doesn't get counted
    if (l == 1) :
        l += 1
 
    count = 0
 
    for num in range(l, r + 1) :
        og_num = num
 
        # While num is divisible by 3,
        # divide it by 3
        while (num % 3 == 0) :
            num = num // 3
 
        # While num is divisible by 5,
        # divide it by 5
        while (num % 5 == 0) :
            num = num // 5
 
        # If num got reduced to 1 then it has
        # only 3 and 5 as prime factors
        if (num == 1) :
            count += 1
            print(og_num)
 
    return count
 
# Driver code
if __name__ == "__main__" :
 
    l = 200
    h = 405
     
    print(findTwoThreePrime(l, h))