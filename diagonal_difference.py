#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0
    counter = 0
    other_counter = 0
    
    while counter <= (n - 1):
        l_to_r += arr[counter][counter]
        counter += 1
    
        
    counter = n - 1 #start counter at 2 for a (3x3)
    while counter > -1:
        r_to_l += arr[other_counter][counter]
        counter -= 1
        other_counter += 1
        
    return(abs(l_to_r - r_to_l))