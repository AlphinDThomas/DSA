class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        inter = [nums[0]]
        res = []
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                inter.append(nums[i])
            else:
                if len(inter)==1:
                    res.append(str(inter[0]))
                else:
                    a = inter[0]
                    b = inter[-1]
                    res.append(str(a)+"->"+str(b))
                inter = [nums[i]]
        if len(inter)==1:
            res.append(str(inter[0]))
        else:
            a = inter[0]
            b = inter[-1]
            res.append(str(a)+"->"+str(b))
        return res