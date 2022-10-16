#keep reducing consective numbers until you get a number with none
number = "6664439133"

def helper(number):
    newStr = ""
    total = 1
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            total += 1
        else:
            newStr += str(int(number[i]) * total)
            total = 1

        if i == len(number) - 2 and number[i] == number[i + 1]:
            newStr += str(int(number[i]) * total)
        elif i == len(number) - 2 and number[i] != number[i + 1]:
            newStr += number[len(number) - 1]

    return newStr


#figure out a way to repeat these calls via loop/recursion
result = helper(number)
result2 = helper(result)
result3 = helper(result2)
print(result3)

        
            









