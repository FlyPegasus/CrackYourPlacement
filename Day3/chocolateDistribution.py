#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        i = 0
        minm = 999999999999999999
        while i + M -1 < N:
            diff = A[i+M -1] - A[i]
            if diff < minm:
                minm = diff
            i += 1
        return minm