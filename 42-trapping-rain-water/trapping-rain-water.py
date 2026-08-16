class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]* len(height)
        maxright = [0]* len(height)

        for i in range(1,len(height)):
            maxleft[i] = max(maxleft[i-1],height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            maxright[i] = max(maxright[i+1],height[i+1])

        

        intermediate = []

        for k in range(len(maxright)):
            temp = min(maxright[k],maxleft[k])
            intermediate.append(temp)
        
        res = []
        for k in range(0,len(intermediate)):
            temp = intermediate[k] - height[k]
            if temp>0:
                res.append(temp)
        return sum(res)