class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        maxm = -1
        mind = -1
        for i in range(N):
            if A[i] > maxm and A[i] <= X:
                maxm = A[i]
                mind = i
        #print(maxm, X)
        return mind