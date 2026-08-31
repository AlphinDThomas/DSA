class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        

        minele = min(nums)
        maxele = max(nums)


        indexofmax = nums.index(maxele)
        indexofmini = nums.index(minele)

        #from left
        valuthfromleft = max(indexofmax,indexofmini)
        fromleft = valuthfromleft + 1

        #from right
        valuthfromright = min(indexofmax,indexofmini)
        fromright = len(nums) - valuthfromright

        #frombothsides

        leftnaduth = min(indexofmax,indexofmini)
        rightnaduth = max(indexofmax,indexofmini)

        bothsidetotal = (leftnaduth+1)+ (len(nums)-rightnaduth)

        return min(bothsidetotal,fromright,fromleft)