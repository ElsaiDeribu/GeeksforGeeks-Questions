from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, v: int, adj: List[List[int]]) -> bool:
		#Code here
        color = [0] * v
        
        def dfs(node, parent):
            
            if color[node] == 1:
                return True
                
            color[node] = 1
            
            for child in adj[node]:
                if child != parent :
                    if dfs(child, node):
                        return True
            
            return False
            
      
        
        for i in range(v):
            if color[i] == 0:
                if dfs(i, -1):
                    return 1
                    
        return 0
                
