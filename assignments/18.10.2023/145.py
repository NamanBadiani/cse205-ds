# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        if root is not None:
            list += self.postorderTraversal(root.left)
            list += self.postorderTraversal(root.right)
            list.append(root.val)
        return list
