class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        def recur(num1,num2):
                val1 = abs(num2)
                val2 = abs(num1)
                while len(stack)>=2:
                    if val1 == val2:
                        stack.pop()
                        stack.pop()
                        return
                    elif val1<val2:
                        stack.pop()
                        stack.pop()
                        stack.append(num1)
                        if len(stack)>=2:
                            if stack[-1]<0 and stack[-2]>0:
                                recur(stack[-1],stack[-2])
                        return
                    elif val1>val2:
                        stack.pop()
                        return
                    
                    
                        
                    
        
        for i in asteroids:
            if not stack:
                stack.append(i)
            elif stack:
                
                if stack[-1]<0 and i<0:
                    stack.append(i)
                elif stack[-1]>0 and i>0:
                    stack.append(i)
                elif stack[-1]<0 and i>0:
                    stack.append(i)
                else:
                    stack.append(i)
                   
                    num1 = stack[-1]
                    num2 = stack[-2]

                    recur(num1,num2)
        return stack
        
                





                        