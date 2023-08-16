class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #for i in range (1,n+1):
        if n<=0:
            return False
        if n%2==0:
            n=n/2
            return self.isPowerOfTwo(n)
        if n==1:
            return True
       
            return False     