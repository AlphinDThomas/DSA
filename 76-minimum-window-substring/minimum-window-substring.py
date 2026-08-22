class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dictet = Counter(t)
        dictesub = Counter()

        left = 0
        temp = ""

        for right in range(len(s)):
            
            char = s[right]
            dictesub[char]+=1
            
            valid =  True

            for char in dictet:
                if dictesub[char]<dictet[char]:
                    valid = False
                    break

            while valid:
                
                substring = s[left:right+1]
                if temp == "" or len(substring)<len(temp):
                    temp =  substring
                
                dictesub[s[left]]= dictesub[s[left]]-1
                left+=1

                valid = True

                for char in dictet:
                    if dictesub[char]<dictet[char]:
                        valid = False
                        break
        return temp