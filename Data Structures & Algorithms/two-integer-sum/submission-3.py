class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for idx, n in enumerate(nums):
            desired_complement = target - n
            if desired_complement in complement:
                return [complement[desired_complement], idx]
            
            complement[n] = idx
        

        