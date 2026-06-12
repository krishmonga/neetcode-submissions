class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            differnce=target-nums[i]
            if differnce in seen:
                return [seen[differnce],i]
            seen[nums[i]]=i
        



           

        