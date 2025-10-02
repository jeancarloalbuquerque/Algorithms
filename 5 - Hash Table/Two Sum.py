class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}

        for num in nums:
            complement = target - num
            
            if num in hashtable:
                return [hashtable[num], num]
            
            hashtable[complement] = num

        return False

    
nums = [2, 2, 7, 11, 15]
target = 17

print(Solution().twoSum(nums, target))