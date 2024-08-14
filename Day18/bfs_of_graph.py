from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = Queue()
        visited = []
        q.put(0)
        visited.append(0)
        while not q.empty():
            s = q.get()
            
            for i in adj[s]:
                if i not in visited:
                    q.put(i)
                    visited.append(i)
        return visited