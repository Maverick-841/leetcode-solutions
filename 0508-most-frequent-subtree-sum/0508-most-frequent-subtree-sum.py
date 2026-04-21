# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        freq = {}
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            total = node.val + left + right

            if total in freq:
                freq[total] += 1
            else:
                freq[total] = 1
            return total
        dfs(root)
        max_freq = 0
        for val in freq:
            if freq[val] > max_freq:
                max_freq = freq[val]
        result = []
        for i in freq:
            if max_freq == freq[i]:
                result.append(i)
        return result
        