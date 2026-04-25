class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=len((list(set(nums))))
        y=len(nums)
        if x<y:
            return True
        else:
            return False
        



        