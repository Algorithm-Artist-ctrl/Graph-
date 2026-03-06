def can_visit_all_rooms(rooms):
    visited = set()

    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    dfs(0)
    return len(visited) == len(rooms)
rooms = [[1], [2], [3], []]
if can_visit_all_rooms(rooms):
    print("All rooms can be visited")
else:
    print("All rooms cannot be visited")