def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first - traverse through array normally and calculate prefix products of all numbers
        #second - traverse through array backwards and calculate postfix products of all numbers
        #finally - once you have updated your output array, you will be left with the answer
        output = [1] * len(nums)

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(len(output) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output