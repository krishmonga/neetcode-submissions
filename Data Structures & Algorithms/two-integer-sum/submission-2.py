class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicr={}
        
        for i in range(len(nums)):
            
            complement = target - nums[i]
            if complement in dicr:
                return [dicr[complement], i]
            dicr[nums[i]]=i
            