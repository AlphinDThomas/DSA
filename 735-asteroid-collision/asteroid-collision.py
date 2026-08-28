class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for ast in asteroids:
            survived = True
            while stack and stack[-1]>0 and ast<0:
                
                if stack[-1]<abs(ast):
                    stack.pop()
                        
                    
                elif stack[-1] == abs(ast):
                    stack.pop()
                    survived = False
                    break
                
                else:
                    survived = False
                    break
                
            if survived:
                stack.append(ast)

        return stack
        
                





                        