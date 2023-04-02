class Solution:
    def isPalindrome(self, x: int) -> bool:

        # check if the integer is negative
        if x < 0:
            return False


        # convert the integer to a string and reverse it
        x_str = str(x)
        x_str_reverse = x_str[::-1]


        # compare the original string and its reverse
        if x_str == x_str_reverse:
            return True
        else:
            return False