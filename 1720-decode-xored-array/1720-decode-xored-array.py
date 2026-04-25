class Solution(object):
    def decode(self, encoded, first):
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr
        