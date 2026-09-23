class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for value, frequency in freq.items():
            buckets[frequency].append(value)

        result = []

        for frequency in range(len(nums), 0, -1):
            for element in buckets[frequency]:
                result.append(element)

                if len(result) == k:
                    return result