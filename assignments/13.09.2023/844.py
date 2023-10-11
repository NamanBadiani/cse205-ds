class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        
        for i in (s):
            if i != '#':
                stack1.append(i)
            else:
                stack1.pop()
        
        for i in (s):
            if i!= '#':
                stack2.append(i)
            else:
                stack2.pop()

        s= "".join(stack1)
        t= "".join(stack2)

        if s==t:
            return True
        else:
            return False
        