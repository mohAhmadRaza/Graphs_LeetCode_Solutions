class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Calling DFS function to to traverse neighbours
        def DFS(currNode, vis):

            # Keep Track of every traversed node
            vis[currNode] = True
            
            # Now check all the neighbours of node
            for nei in rooms[currNode]:

                # If it is not already visited, visit it now
                if not vis[nei]:
                    DFS(nei, vis)
        
        # Initially all the nodes are unvisited
        vis = [False] * len(rooms)

        # Firstly traversing unlocked room : 0
        DFS(0, vis)

        # returning if any room is not visited
        return len(set(vis)) == 1

        

