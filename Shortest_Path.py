class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for nei in range(n):
            graph[nei].append(nei + 1)
        
        def BSF(graph):
            q = deque([0])
            seen = {0}
            count = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == n-1:
                        return count
                    for nei in graph[curr]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
                count += 1 
        
        result = []
        for u, v in queries:
            graph[u].append(v)
            result.append(BSF(graph))
        
        return result
