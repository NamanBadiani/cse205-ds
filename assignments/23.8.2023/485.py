class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxone = []
        for i in range (len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxone.append(count)
                count = 0
        maxone.append(count)        
        return max(maxone)            
        