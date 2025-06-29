# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #this solution uses BFS
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """Encodes a tree to a single string."""
        if not root:
            return ""

        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        # Optional: Trim trailing "null"s to reduce size
        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        index = 1


        while queue and index < len(nodes):
            current = queue.pop(0)
            
            # Left child
            if nodes[index] != "null":
                left = TreeNode(int(nodes[index]))
                current.left = left
                queue.append(left)
            index += 1

            # Right child
            if index < len(nodes) and nodes[index] != "null":
                right = TreeNode(int(nodes[index]))
                current.right = right
                queue.append(right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))