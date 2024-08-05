class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m1 = 0
        
        for j in range(len(cardPoints) - k, len(cardPoints)):
            m1 += cardPoints[j]
        l = -k
        maxm = m1
        for i in range(k):
            m1 += cardPoints[i] - cardPoints[l]
            if m1 > maxm:
                maxm = m1
            l += 1
        #print(m1, m2)
        return maxm