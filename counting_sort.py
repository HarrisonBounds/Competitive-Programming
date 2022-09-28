#frequency array - counting sort

def countingSort(arr):
    result = [0] * 100 #use this method to get an array of zeros
    print(result)
    
    for i in range(len(arr)):
        result[arr[i]] = result[arr[i]] + 1 #use the value in arr as the index for the result, and increment by 1 each time number appears in arr
    return result