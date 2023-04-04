class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_parentheses_helper(n, 0, "", result)
        return result

    def generate_parentheses_helper(self, left, right, curr, result):
        if left == right == 0:
            result.append(curr)
            return
        if left > 0:
            self.generate_parentheses_helper(left-1, right+1, curr+'(', result)
        if right > 0:
            self.generate_parentheses_helper(left, right-1, curr+')', result)