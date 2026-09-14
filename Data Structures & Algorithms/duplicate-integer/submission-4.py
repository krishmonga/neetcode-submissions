class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set(nums)
        # for num in nums:
        #     if num is seen:
        #         return True
        #     else:
        #         return False
        return (len(nums)!=len(set(nums)))
        