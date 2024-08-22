class Solution:
	def dfs(self, adjList: List[List[int]]) -> List[int]:
		# add your logic here
		result = []
		def DFS(start, vis):
			vis[start] = True
			
			result.append(start)
			
			for neighbour in adjList[start]:
				if not vis[neighbour]:
				    DFS(neighbour, vis)
		
		vis = [False] * len(adjList)
		DFS(0, vis)
		return result


