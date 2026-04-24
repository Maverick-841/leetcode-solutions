class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()  # important for pruning
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # pruning (key for speed)
                if candidates[i] > remaining:
                    break
                
                # choose
                path.append(candidates[i])
                
                # stay on same index (reuse allowed)
                backtrack(i, path, remaining - candidates[i])
                
                # undo
                path.pop()

        backtrack(0, [], target)
        return res