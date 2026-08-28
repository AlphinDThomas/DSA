class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = set()
        list2 = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                if i not in list1:
                    list1.add(i)
        for j in nums2:
            if j not in nums1:
                if j not in list2:
                    list2.add(j)
        return [list(list1),list(list2)]