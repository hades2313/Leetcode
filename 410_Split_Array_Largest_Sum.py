class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if m == n:
            return max(nums)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        sum = [0] * (n + 1)
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        for j in range(1, m + 1):
            for i in range(j, n + 1):
                for k in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum[i] - sum[k]))
        return dp[-1][-1]


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low = high = nums[0]
        for num in nums[1:]:
            low = max(low, num)
            high += num
        while low < high:
            mid = low + (high - low) // 2
            count, cur_sum = 1, nums[0]
            for num in nums[1:]:
                if cur_sum + num <= mid:
                    cur_sum += num
                else:
                    count += 1
                    cur_sum = num
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low