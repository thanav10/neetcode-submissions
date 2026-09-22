class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        c = []
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        b = sorted(a,key = lambda num : a[num], reverse = True)
        for j in range(k):
            c.append(b[j])
        return c
