class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        
        res = []
        stack = [chars[0]]
        
        for i in chars[1:]:
            
            if stack[-1]==i:
                stack.append(i)
            elif stack[-1]!=i:
                ch = stack[0]
                res.append(ch)
                if len(stack)>1 and len(stack)<10:
                    res.append(str(len(stack)))
                elif len(stack)>=10:
                    for j in str(len(stack)):
                        res.append(j)
                stack = [i]
        if stack:
            ch = stack[0]
            res.append(ch)
            if len(stack)>1 and len(stack)<10:
                res.append(str(len(stack)))
            elif len(stack)>=10:
                for j in str(len(stack)):
                    res.append(j)
        
        chars[:] = res