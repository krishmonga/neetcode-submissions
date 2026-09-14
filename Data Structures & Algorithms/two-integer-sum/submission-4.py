class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for num in range(len(nums)):
            differnce=target-nums[num]
            if differnce in seen:
                return[seen[differnce],num]
            seen[nums[num]]=num



        