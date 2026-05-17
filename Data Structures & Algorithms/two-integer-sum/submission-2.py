class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_indexes = {n: idx for idx, n in  enumerate(nums)}

        sortedNums = sorted(nums)
        lidx = 0
        ridx = len(nums) - 1
        result = None
        while result is None:
            print("lidx=", lidx, " | ridx=", ridx)
            addition = sortedNums[lidx] + sortedNums[ridx]
            if addition == target:
                result = [sortedNums[lidx], sortedNums[ridx]]
            elif addition > target:
                ridx -= 1
            else:
                lidx += 1

        idx1 = next(i for i, n in enumerate(nums) if n == result[0])
        idx2 = next(i for i, n in enumerate(nums) if n == result[1] and i != idx1)
        return [min(idx1, idx2), max(idx1, idx2)]
        