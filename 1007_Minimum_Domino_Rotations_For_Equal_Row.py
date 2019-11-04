# 四种情况，要么A list的数字都等于A[0], 要么都等于B[0]。 B list同理
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def count_swap(A_num, B_num):
            A_swap = B_swap = 0
            for i in range(1, len(A)):
                if A[i] != A_num and B[i] == A_num:
                    A_swap += 1
                elif A[i] != A_num and B[i] != A_num:
                    A_swap = float('inf')
                if B[i] != B_num and A[i] == B_num:
                    B_swap += 1
                elif B[i] != B_num and A[i] != B_num:
                    B_swap = float('inf')
            return min(A_swap, B_swap)
        result = min(count_swap(A[0], B[0]), 1 + count_swap(B[0], A[0]))
        return result if result != float('inf') else -1
