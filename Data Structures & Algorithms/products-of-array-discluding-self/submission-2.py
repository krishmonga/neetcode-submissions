class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[None]*len(nums)
        
        
        prefix=1
        for i in range(len(nums)):
            new[i] =prefix
            prefix *=nums[i]
        
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            new[j]*=postfix
            postfix*=nums[j]
        
        return new

        