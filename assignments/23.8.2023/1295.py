class Solution(object):
    def findNumbers(self, nums):
        def digits(num):
            count = 0

            while num !=0:
                num//= 10
                count += 1
            return count

        count2 = 0
        for i in nums:
            if digits(i)%2 ==0:
                count2 += 1
        return count2