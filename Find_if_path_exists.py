class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        visited = [False]* n

        #converision in adjacency List
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def valid(node):
            if node == destination:
                return True
        
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[node] = True
                    if valid(neighbour):
                        return True
            return False        
        return valid(source)


