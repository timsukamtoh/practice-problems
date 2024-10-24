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

# leetcode 49. Group Anagrams
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mapping = collections.defaultdict(list)

    for st in strs:
        key = tuple(sorted(st))
        mapping[key].append(st)

    return list(mapping.values())