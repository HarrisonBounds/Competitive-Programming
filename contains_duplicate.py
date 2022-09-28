#217. Contains Duplicate

nums = [2, 14, 18, 22, 22]

def containsDuplicate(nums) -> bool:
        nums.sort()
       
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            
        return False