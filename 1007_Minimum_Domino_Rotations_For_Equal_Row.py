class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(target):
            a_rotation = b_rotation = 0
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    return float('inf')
                if A[i] != target:
                    a_rotation += 1
                elif B[i] != target:
                    b_rotation += 1
            return min(a_rotation, b_rotation)
        if not A or not B or len(A) != len(B):
            return -1
        result = min(check(A[0]), check(B[0]))
        return result if result != float('inf') else -1

