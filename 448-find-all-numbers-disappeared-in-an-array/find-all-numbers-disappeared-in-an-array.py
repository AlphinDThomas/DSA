class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list1 = list(set(nums))
        newset = set()
        for i in list1:
            newset.add(i)
        res = []
        for i in range(1,len(nums)+1):
            if i not in newset:
                res.append(i)
        return res