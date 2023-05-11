class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        s = sorted(nums)
        for n in range(len(s)):
            if target == s[n]: 
                l.append(n)
        return l
        