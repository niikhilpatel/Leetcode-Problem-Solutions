class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        for i in range(len(prev)):
            # If the current digit is the same as the next digit
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                # Append the count and digit to the result
                result += str(count) + prev[i]
                count = 1

        return result
