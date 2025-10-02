class Solution(object):
    def twoSum(self, nums, target):
        complement = {}

        for i in range(len(nums)):
            num = nums[i]
            c = target - num

            if num in complement:
                return [complement[num], i]
            
            complement[c] = i
            
        return False
    
nums = [2,7,11,15]
target = 17

print(Solution().twoSum(nums, target))


