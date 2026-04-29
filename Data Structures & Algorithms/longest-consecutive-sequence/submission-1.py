class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new=[None]*len(nums)
        new=list(set(nums))
        longest=0
        for num in new:
            if num - 1 not in new:
                curr = num
                length = 1

                while curr + 1 in new:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest
