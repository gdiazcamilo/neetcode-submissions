class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n1 in nums:
            if n1 in seen:
                return True
            seen.add(n1)

        return False