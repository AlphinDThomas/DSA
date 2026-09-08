class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = -1
        if len(set(nums))==1:
            return 0
        psum = 0
        dicte = {0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                psum = psum -1
            else:
                psum+=1

            if psum in dicte:
                length = i - dicte[psum]
                maxlen = max(maxlen,length)
            else :
                dicte[psum] = i
        return maxlen
            