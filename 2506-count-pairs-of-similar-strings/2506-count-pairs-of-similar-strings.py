class Solution(object):
    def similarPairs(self, words):
        freq = {}
        for word in words:
            key = frozenset(word)
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
        res = 0
        for f in freq.values():
            res += f * (f - 1) // 2
        return res   