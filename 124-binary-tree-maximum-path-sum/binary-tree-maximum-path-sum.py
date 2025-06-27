# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = float("-inf") #This gives -ve infinity. float("inf") gives +ve infinity
        
        def dfs(root):
            #indates path_sum is a nonlocal/global variable name
            nonlocal path_sum
            if root is None:
                return 0
            
            #ignore negative contributions -- indicates we don't conside a child branch which yields -ve sum
            left_sum = max(dfs(root.left), 0)
            right_sum = max(dfs(root.right), 0)
            #current path sum
            current_path_sum = root.val+left_sum+right_sum
            path_sum = max(path_sum, current_path_sum)
            # Return max extendable path
            return root.val+max(left_sum, right_sum)
        
        dfs(root)
        return path_sum