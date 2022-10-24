#This binary search will return the left most element in the array if the target occurs more than once or in a sequence
#If the target is not in the array, it will return where the element should be
def binarySearch(nums, target: int) -> int:

    l, r = 0, len(nums)

    while l < r :

        m = (l + r) // 2

        if nums[m] < target:
            l = m + 1
        else: 
            r = m

    return l

print(binarySearch([1, 2, 3, 4, 5, 78, 89, 89, 89, 103], 99))