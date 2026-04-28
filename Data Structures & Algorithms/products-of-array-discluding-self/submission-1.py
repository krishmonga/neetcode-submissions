class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[None]*len(nums)
        news=[None]*len(nums)
        ews=[None]*len(nums)
        prefix=1
        for i in range(len(nums)):
            new[i] =prefix
            prefix *=nums[i]
        
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            news[j]=postfix
            postfix*=nums[j]
        for k in range(len(nums)):
            ews[k]=new[k]*news[k]
        return ews

        