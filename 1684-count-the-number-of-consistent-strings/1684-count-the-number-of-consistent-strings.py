class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0
        for word in words:
            valid = True
            for ch in word:
                if ch not in allowed_set:
                    valid = False
                    break
            if valid == True:
                count += 1
        return count
        