# leetcode 347. Top K Frequent Elements
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    counter = collections.Counter(nums)

    freq = [[] for i in range(len(nums)+1)]
    for num,count in counter.items():
        freq[count].append(num)

    res = []
    for i in range(len(freq)-1,-1,-1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res