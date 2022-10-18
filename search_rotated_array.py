def search(self, nums, target: int):
        #step 1 - figure out which sorted portion you are in
        #step 2 - depending on which portion you are in, update your high or low
        #Always check if your target equals your middle value

        #BINARY SEARCH

        #OR use binary search to find a way to get target
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2

            if target == nums[middle]:
                return middle

            #left sorted portion
            if nums[low] <= nums[middle]:
                if target < nums[low] or target > nums[middle]: #search the right sorted portion
                    low = middle + 1
                else:
                    high = middle - 1

            else:
                if target < nums[middle] or target > nums[high]: #search the left side
                    high = middle - 1
                else:
                    low = middle + 1


        return -1