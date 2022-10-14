

def threeSum(self, nums):
        #Combine solutions from two sum and two sum 2
        #left and right pointers

        result = []

        nums.sort() #O(nlogn)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1 
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #need to update pointer to get out of the loop
                    left += 1
                    #cannot acccept duplicates
                    while nums[left] == nums[left - 1] and left < right: #UNDERSTAND THIS CONDITION
                        left += 1

        return result