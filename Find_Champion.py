class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
        
        teams = [False] * n
        vis = [False] * n

        def dfs(node):
            for nei in graph[node]:
                if not vis[nei]:
                    teams[nei] = True
                    vis[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if not vis[i]:
                dfs(i)
        
        count = Counter(vis)
        if count[False] == 1:
            for i in range(len(vis)):
                if not vis[i]:
                    return i
        
        return -1
