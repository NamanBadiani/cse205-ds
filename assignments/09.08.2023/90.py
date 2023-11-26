class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result =[[]]
        for i in nums:
            result+=[j+[i] for j in result]
        return result