from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A=Counter(s)
        B=Counter(t)
        if A==B:
            return True
        else:
            return False


        