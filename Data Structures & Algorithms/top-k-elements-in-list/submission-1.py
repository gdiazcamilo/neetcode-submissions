class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_by_frequency = defaultdict(int)
        for n in nums:
            numbers_by_frequency[n] += 1

        frequency_by_numbers = defaultdict(list)
        for n, f in numbers_by_frequency.items():
            frequency_by_numbers[f].append(n)

        sorted_frequencies = sorted(numbers_by_frequency.values(), reverse=True)
        most_frequent = []
        for i in range(k):
            frequency = sorted_frequencies[i]
            most_frequent.append(frequency_by_numbers[frequency].pop())
        
        return most_frequent