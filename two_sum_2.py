#Take advantage of the sorted list 

def twoSum(self, numbers, target: int):
        big = len(numbers) - 1
        small = 0

        while True:
            diff = numbers[big] + numbers[small]

            if diff > target:
                big -= 1
            elif diff < target:
                small += 1
            else:
                return [small+1, big+1]

        
        
        
        #Original two sum solution
        # d = {}

        # for i, val in enumerate(numbers):
        #     diff = target - val

        #     if diff not in d:
        #         d[val] = i
        #     else:
        #         return [d[diff] + 1, i + 1]
