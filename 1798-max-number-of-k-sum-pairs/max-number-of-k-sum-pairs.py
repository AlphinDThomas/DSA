class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dicte = dict()
        pairs = 0
        
        for num in nums:
            if (k-num) in dicte:
                if dicte[k-num]>0:
                    pairs += 1
                    dicte[k-num] -= 1
                elif dicte[k-num]==0:
                    if num in dicte:
                        dicte[num]+=1
                    else:
                        dicte[num] = 1
            elif (k-num) not in dicte:
                if num in dicte:
                    dicte[num]+=1
                else:
                    dicte[num] = 1
        return pairs
            