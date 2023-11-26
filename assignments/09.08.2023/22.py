class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def gp(left,right,count,temp):
            if left==right==0:
                result.append(temp)
            if left>0:
                gp(left-1,right,count+1,temp+"(")
            if right>0 and count>0:
                gp(left,right-1,count-1,temp+")")
        gp(n,n,0,"")
        return result