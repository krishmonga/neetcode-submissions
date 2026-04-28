class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[None]*len(nums)
        preffix=1
        for i in range(len(nums)):
            res[i]=preffix
            preffix *=nums[i]
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=postfix
            postfix *=nums[j]
        return res