class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        visited = set([0])
        locked = set(range(1,len(rooms)))
        while keys and len(locked) > 0:
            k = keys.pop()
            if k not in visited:
                locked.remove(k)
                keys.update(rooms[k])
                visited.add(k)
        return len(locked) == 0
