# leetcode 347. Top K Frequent Elements
def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq_counter = collections.Counter(nums)
        sorted_nums = sorted(freq_counter.items(), key=lambda x: (x[1],x[0]), reverse=True)
        top_k = []
        for i in range(k):
            top_k.append(sorted_nums[i][0])
        return top_k