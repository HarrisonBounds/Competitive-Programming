#USE BINARY SEARCH TREE
def searchInsert(self, nums, target) -> int:
        high = len(nums) - 1
        low = 0
        mid = 0

        #edge cases
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif high == low:
                if nums[mid] > target:
                    return mid
                else:
                    return mid + 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid

            

        return mid + 1
