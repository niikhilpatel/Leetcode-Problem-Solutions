class Solution:
    def isMatch(self, s:str, p: str) -> bool:

        # Get the lengths of the input strings
        m,n = len(s), len(p)

        # Create a boolean 2D table dp with m+1 rows and n+1 columns
        dp = [[False] * (n+1) for _ in range(m+1)]

        # set the initial value of dp[0][0] to True
        dp[0][0] = True

        # Fill the first row of dp
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the rest of dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))

        # Return the value of dp[m][n]
        return dp[m][n]