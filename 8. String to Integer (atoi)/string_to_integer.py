class Solution:
    def myAtoi(self, s: str) -> int:

        # step 1: Remove leading and trailing whitespaces
        s = s.strip()

        # step 2 : check if the string is empty
        if not s:
            return 0

        # step 3: check if the first non-whitespaces character is a sign
        i = 0
        if s[0] in ["+", "-"]:
            i += 1
            if i == len(s): # string ends with sign
                return 0

        # step 4: Convert consecutive digits to an integer
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # step 5: Apply sign and checks for overflow
        if s[0] == "-":
            num = -num
            if num < -2**31:
                return -2**31
        else:
                if num > 2**31 - 1:
                    return 2**31 - 1

        return num