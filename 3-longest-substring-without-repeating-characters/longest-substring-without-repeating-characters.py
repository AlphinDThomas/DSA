class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        left = 0
        seen = set()
        maxlen = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            elif s[right] in seen:
                maxlen = max(maxlen,len(seen))
               
                while s[right] in seen:
                    seen.remove(s[left])
                    left = left + 1
                seen.add(s[right])
        maxlen = max(maxlen,len(seen))
        if maxlen == 0:
            return len(seen)
        return maxlen
