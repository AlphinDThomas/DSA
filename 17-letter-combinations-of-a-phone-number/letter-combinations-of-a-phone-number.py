class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dicte = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = [""]

        for digit in digits:
            temp = []
            for combinations in res:
                for letter in dicte[digit]:
                    temp.append(combinations+letter)
            res= temp
        
        return res