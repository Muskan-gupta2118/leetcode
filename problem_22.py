#Given the root of a binary tree and an integer targetSum,
#  return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#A leaf is a node with no children.
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def hasPathSum(root, targetSum):
    if not root:
        return False

    # If it's a leaf node
    if not root.left and not root.right:
        return targetSum == root.val

    # Check left and right subtree
    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))


# Creating example tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \       \
# 7    2       1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22

# Function call
result = hasPathSum(root, targetSum)

# Output
print("Output:", result)