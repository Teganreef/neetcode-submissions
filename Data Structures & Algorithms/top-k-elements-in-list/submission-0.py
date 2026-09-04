class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # STEP 1: Tally up the frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 
            
        # STEP 2: Create buckets and dump the numbers in
        freq = [[] for i in range(len(nums) + 1)]
        for number, c in count.items():
            freq[c].append(number)
            
        # STEP 3: Scan backwards and grab the top k
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
