class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        if t=="":
            return False
        if len(s)==1:
            if s[0] in t:
                return True
            else:
                return False
        substring = ""
        substring += s[0]
        s = list(s)
        t = list(t)
        seen = []
        prevpos = t.index(s[0])
        for i in range(1,len(s)):
            if s[i] in t:
                if s[i] in seen:
                    if s[i] in t[prevpos+1:]:
                        temp =  t[prevpos+1:]
                        pos = prevpos + 1 +  temp.index(s[i])
                    if prevpos<pos:
                        substring+=s[i]
                        prevpos = pos
                    else:
                        return False
                elif s[i] not in seen:
                    if s[i] in t[prevpos+1:]:
                        tem = t[prevpos+1:]
                        pos = prevpos + 1+ tem.index(s[i])
                        if prevpos<pos:
                            substring+=s[i]
                            prevpos = pos
                    else:
                        return False
                    
                    seen.append(s[i])
        if substring == "".join(s):
            return True
        else:
            return False