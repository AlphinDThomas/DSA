class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = "[.]"
        substring = ""
        for i in address:
            if i == ".":
                substring+=addr
            else:
                substring+=i
        return substring