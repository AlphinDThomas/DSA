class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack= []
        countstack = []

        stack.append(s[0])
        countstack.append(1)

        for i in s[1:]:
            count =0
            if stack and stack[-1]==i:
                countstack[-1]+=1
            else:
                stack.append(i)
                countstack.append(1)
            
            if countstack[-1]>=k:
                stack.pop()
                countstack.pop()

        substr = ""
        
        for i in range(len(stack)):
            substr += stack[i]*countstack[i]
            
        return substr