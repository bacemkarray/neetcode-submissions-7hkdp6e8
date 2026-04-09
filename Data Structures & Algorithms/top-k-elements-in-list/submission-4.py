class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for n in nums:
            freq_dict[n] = 1 + freq_dict.get(n, 0)

        buckets = [[] for n in range(len(nums)+1)]

        for num, freq in freq_dict.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res