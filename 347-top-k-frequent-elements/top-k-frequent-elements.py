class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dicte = dict()

        list1 = list(set(nums))

        for i in list1:
            dicte[i] = nums.count(i)
        print(dicte)

        freq = []
        for i in list1:
            freq.append(dicte[i])
        
        freq.sort(reverse=True)
        print(freq)
        res = []

        for f in freq:
            for i in nums:
                if dicte[i]== f and i not in res:
                    res.append(i)
                    break
        return res[0:k]

            