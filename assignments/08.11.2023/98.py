# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        stack.append([root,-1*float('inf'),float('inf')])
        while(stack):
            s=stack.pop()
            t=s[0]
            le=s[1]
            ri=s[2]
            if t.val<=le or t.val>=ri:
                return False
            if t.right!=None:
                stack.append([t.right,t.val,ri])
            if t.left!=None:
                stack.append([t.left,le,t.val])
        return True