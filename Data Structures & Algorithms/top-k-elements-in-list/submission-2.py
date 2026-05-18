class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1
        print("frequency ", frequency)

        frequency_by_number = [[n, f] for f, n in frequency.items()]
        frequency_by_number.sort()
        print("frequency_by_number", frequency_by_number)

        most_frequent = []
        for i in range(k):
            most_frequent.append(frequency_by_number.pop()[1])

        return most_frequent