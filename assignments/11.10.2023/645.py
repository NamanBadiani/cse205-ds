class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                result.append(nums[i])
                break
        
        for i in range(len(nums)):
            if i+1 not in nums:
                result.append(i+1)
                break
        
        return result
        