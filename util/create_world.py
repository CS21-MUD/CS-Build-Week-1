from adventure.models import Player, Room

Room.objects.all().delete()

rooms = [
    {'title': 'Room A', 'description': 'Testing out Room A'},
    {'title': 'Room B', 'description': 'Testing out Room B'},
    {'title': 'Room C', 'description': 'Testing out Room C'},
    {'title': 'Room D', 'description': 'Testing out Room D'},
    {'title': 'Room E', 'description': 'Testing out Room E'},
    {'title': 'Room F', 'description': 'Testing out Room F'},
    {'title': 'Room G', 'description': 'Testing out Room G'},
    {'title': 'Room H', 'description': 'Testing out Room H'},
    {'title': 'Room I', 'description': 'Testing out Room I'},
    {'title': 'Room J', 'description': 'Testing out Room J'},
    {'title': 'Room K', 'description': 'Testing out Room K'},
    {'title': 'Room L', 'description': 'Testing out Room L'},
    {'title': 'Room M', 'description': 'Testing out Room M'},
    {'title': 'Room N', 'description': 'Testing out Room N'},
    {'title': 'Room O', 'description': 'Testing out Room O'},
    {'title': 'Room P', 'description': 'Testing out Room P'},
    {'title': 'Room Q', 'description': 'Testing out Room Q'},
    {'title': 'Room R', 'description': 'Testing out Room R'},
    {'title': 'Room S', 'description': 'Testing out Room S'},
    {'title': 'Room T', 'description': 'Testing out Room T'},
    {'title': 'Room U', 'description': 'Testing out Room U'},
    {'title': 'Room V', 'description': 'Testing out Room V'},
    {'title': 'Room W', 'description': 'Testing out Room W'},
    {'title': 'Room X', 'description': 'Testing out Room X'},
    {'title': 'Room Y', 'description': 'Testing out Room Y'},
]

connectedCitiesIndex = [[0, 1, "e"], [0, 2, "s"], [1, 0, "w"], [1, 10, "e"], [1, 8, "s"], [2, 0, "n"], [2, 3, "s"],
                        [3, 2, "n"], [3, 5, "e"], [3, 4, "s"], [4, 3, "n"], [4, 6, "e"], [4, 7, "s"], [5, 3, "w"],
                        [5, 9, "e"], [6, 4, "w"], [6, 9, "e"], [7, 4, "w"], [7, 15, "e"], [8, 2, "n"], [8, 12, "e"],
                        [8, 9, "s"], [9, 5, "w"], [9, 8, "n"], [9, 6, "s"], [9, 14, "e"], [10, 1, "w"], [10, 12, "s"],
                        [10, 11, "e"], [11, 10, "w"], [11, 16, "e"], [12, 8, "w"], [12, 10, "n"], [12, 13, "e"],
                        [13, 12, "w"], [13, 14, "s"], [14, 13, "n"], [14, 9, "w"], [14, 15, "s"], [14, 20, "e"],
                        [15, 7, "w"], [15, 14, "n"], [15, 22, "s"], [16, 11, "w"], [16, 18, "s"], [16, 17, "e"],
                        [17, 16, "w"], [18, 16, "n"], [18, 19, "s"], [19, 18, "n"], [19, 20, "s"], [20, 14, "w"],
                        [20, 19, "n"], [20, 23, "e"], [20, 21, "s"], [21, 20, "n"], [21, 22, "s"], [22, 21, "n"],
                        [22, 24, "e"], [22, 15, "w"], [23, 20, "w"], [24, 22, "e"]]

saved_rooms = []

for i in range(len(rooms)):
    saved_rooms.append(Room(title=rooms[i]['title'], description=rooms[i]['description']))
    saved_rooms[i].save()

for i in range(len(connectedCitiesIndex)):
    saved_rooms[connectedCitiesIndex[i][0]].connect_rooms(saved_rooms[connectedCitiesIndex[i][1]], connectedCitiesIndex[i][2])

players = Player.objects.all()
for p in players:
    p.currentRoom = saved_rooms[0].id
    p.save()