class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = cur_max = 0
        for idx, i in enumerate(arr):
            cur_max = max(cur_max, i)
            if idx == cur_max:
                result += 1
        return result