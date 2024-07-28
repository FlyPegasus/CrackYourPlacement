class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        for i in range(n):
            dp.append(-1)
        def ways(n, dp):
            if n < 3:
                if dp[n] == -1:
                    dp[n] = n
                return dp[n]
            else:
                if dp[n] == -1:
                    dp[n] = ways(n-1, dp) + ways(n-2, dp)
                return dp[n]
        return ways(n, dp)