class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def solve(current,used):
            if len(nums)==len(current):
                res.append(current)
                return
            for j in range(len(nums)):
                if nums[j] not in used:
                    solve(current+[nums[j]],used+[nums[j]])
        solve([],[])
        return res