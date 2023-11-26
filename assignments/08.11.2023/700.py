# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack,subtree=[],None
        while True:
            while root:
                if root.val==val:subtree=root
                stack.append(root)
                root=root.left
            if subtree: return subtree

            if not stack: return None

            root= stack.pop().right