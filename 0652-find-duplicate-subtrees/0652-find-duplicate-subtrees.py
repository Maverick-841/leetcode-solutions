class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        
        count = defaultdict(int)
        result = []

        def dfs(node):
            if not node:
                return "null"
            
            serial = (
                str(node.val) + "," +
                dfs(node.left) + "," +
                dfs(node.right)
            )
            
            count[serial] += 1
            
            if count[serial] == 2:
                result.append(node)
            
            return serial
        
        dfs(root)
        return result