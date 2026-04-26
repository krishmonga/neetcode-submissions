from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A=Counter(nums)
        result=[]
        for num, freq in A.most_common(k):
            result.append(num)
        return result

        