from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "Sprint-Challenge--Graphs/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # empty list
visited = set() # empty set
path = [] # empty list
room = {} # empty dictionary
last_room = {'n': 's','s': 'n','e': 'w','w': 'e'} #d irections reversed
counter = 0 # setting counter to zero

# while we haven't visited all the rooms
while len(visited) < len(room_graph): # while length of visited  is less than length of room_graph
    currRoom = player.current_room.id # currRoom is set to current room_id
    if currRoom not in visited: # if currRoom id not in visited
        visited.add(currRoom) # add currRoom to visited set
        directions = player.current_room.get_exits() # directions is set to current_rooms exits
        room[currRoom] = directions # set room[currRoom] to directions

    # try all possible directions in current room
    while len(room[currRoom]) >= 0: # while length of room[currRoom] is greater than or equal to zero
        if len(room[currRoom]) > 0: # if length of room[currRoom] is greater than zero
            move = room[currRoom].pop() # set move to room[currRoom].pop()
            if player.current_room.get_room_in_direction(move).id not in visited: # if move not in visited
                path.append(move) # add move to path list
                traversal_path.append(move) # add move to traversal_path list
                player.travel(move) 
                counter += 1
                break

        if len(room[currRoom]) == 0:
            last_move = path.pop()
            prior_direction = last_room[last_move]
            traversal_path.append(prior_direction)
            player.travel(prior_direction)
            
            break

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
