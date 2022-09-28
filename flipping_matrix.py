#Return the greatest sum you can have at the top left corner by revesing rows and columns
#HINT - Use a mirror image to visualize 


def flippingMatrix(matrix):
    n = len(matrix)
    result = 0
    
    for i in range(n // 2):
        for j in range(n // 2):
            max_num = max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
            result += max_num
    return result