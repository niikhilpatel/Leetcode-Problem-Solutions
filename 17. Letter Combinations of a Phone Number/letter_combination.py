class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index,path):
            if len(path) == len(digits):
                result.append(path)
                return
        
            for letter in phone_dict[digits[index]]:
                backtrack(index+1, path+letter)
        
        result = []
        backtrack(0, '')
        return result