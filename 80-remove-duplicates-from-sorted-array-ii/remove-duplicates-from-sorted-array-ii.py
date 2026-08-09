class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        stack = []
        countstack = []

        for i in range(len(nums)):

            if stack and stack[-1] == nums[i]:
                countstack[-1]+=1
            else:
                stack.append(nums[i])
                countstack.append(1)
            
            if countstack[-1]>2:
                countstack[-1]=2
        print(countstack)
        print(stack)
        res = []
        i = 0
        for i in range(len(countstack)):
            for j in range(countstack[i]):
                res.append(stack[i])
        nums[:] = res
