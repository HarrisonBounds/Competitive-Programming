#1. Two Sum

def twoSum(nums, target):
    h = {} #val : index
    
    for i, val in enumerate(nums):
        difference = target - val
        
        if difference not in h:
            h[val] = i
        else:
            return [h[difference], i]