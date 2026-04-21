# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        def build(pre,post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            left_node = pre[1]

            idx = post.index(left_node)
            left_size = idx + 1
            root.left = build(pre[1:1+left_size],post[:left_size])
            root.right = build(pre[1+left_size:],post[left_size:-1])
            return root
        return build(preorder,postorder)
                