
import random

from utils import Queue


class Graph():
    def __init__(self, player):
        self.rooms = {}
        self.player = player
        self.traversal_path = []

    # Add a room (vertex) to graph
    def add_room(self, room_id, exits):
        if room_id not in self.rooms:
            self.rooms[room_id] = [{}, ()]
            for exit in exits:
                self.rooms[room_id][0][exit] = '?'
        if room_id == 0:
            self.rooms[room_id][1] = (0, 0)

    # Add directed connection (edges) between two exits
    def add_connection(self, room1_id, room2_id, direction):
        opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        if room1_id in self.rooms and room2_id in self.rooms:
            self.rooms[room1_id][0][direction] = room2_id
            self.rooms[room2_id][0][opposite_direction[direction]] = room1_id
        else:
            raise IndexError('That room does not exist!')

    # Get all exits (edges) of a room (vertex)
    def get_exits(self, room_id):
        return self.rooms[room_id][0]

    # Get coordinates of a room (vertex)
    def get_coordinates(self, room_id):
        return self.rooms[room_id][1]

    # Navigate to next room and update graph
    def take_exit(self, direction):
        previous_room = self.player.current_room
        self.player.travel(direction)
        self.traversal_path.append(direction)

        new_room = self.player.current_room
        self.add_room(new_room.id, new_room.get_exits())
        self.add_connection(previous_room.id, new_room.id, direction)

        prev_coordinates = self.get_coordinates(previous_room.id)

        if direction == 'n':
            new_coordinates = (prev_coordinates[0], prev_coordinates[1] + 1)
        if direction == 's':
            new_coordinates = (prev_coordinates[0], prev_coordinates[1] - 1)
        if direction == 'e':
            new_coordinates = (prev_coordinates[0] + 1, prev_coordinates[1])
        if direction == 'w':
            new_coordinates = (prev_coordinates[0] - 1, prev_coordinates[1])

        self.rooms[new_room.id][1] = new_coordinates
        self.check_coordinates()

        return new_room

    # Navigate to each room in depth-first order beginning from starting room, done using recursion
    def dft_recursive(self, starting_room=None, finished=None):
        starting_room = starting_room or self.player.current_room
        finished = finished or set()

        if starting_room not in finished:
            self.add_room(starting_room.id, starting_room.get_exits())

            current_room_id = starting_room.id
            current_exits = self.get_exits(current_room_id)

            directions = ['s', 'w', 'n', 'e']
            # directions = ['s', 'e', 'n', 'w']

            random.shuffle(directions)

            if directions[0] in current_exits and current_exits[directions[0]] == '?':
                new_room = self.take_exit(directions[0])
                self.dft_recursive(new_room, finished)
            elif directions[1] in current_exits and current_exits[directions[1]] == '?':
                new_room = self.take_exit(directions[1])
                self.dft_recursive(new_room, finished)
            elif directions[2] in current_exits and current_exits[directions[2]] == '?':
                new_room = self.take_exit(directions[2])
                self.dft_recursive(new_room, finished)
            elif directions[3] in current_exits and current_exits[directions[3]] == '?':
                new_room = self.take_exit(directions[3])
                self.dft_recursive(new_room, finished)
            else:
                finished.add(starting_room)

    # Find path to shortest unexplored room using breadth-first search
    def bfs(self, starting_room=None):
        starting_room = starting_room or self.player.current_room
        queue = Queue()
        queue.enqueue([starting_room.id])
        visited = set()

        while queue.size() > 0:
            self.add_room(starting_room.id, starting_room.get_exits())

            current_path = queue.dequeue()
            current_room_id = current_path[-1]
            current_exits = self.get_exits(current_room_id)

            if '?' in current_exits.values():
                self.convert_path_to_directions(current_path)
                return

            if current_room_id not in visited:
                visited.add(current_room_id)
                for exit in current_exits:
                    path_to_next_room = [*current_path, current_exits[exit]]
                    queue.enqueue(path_to_next_room)

    # Convert list of room IDs to lists of directions to add to traversal path
    def convert_path_to_directions(self, list_rooms):
        steps_in_path = len(list_rooms) - 1
        for index in range(steps_in_path):
            current_exits = self.get_exits(list_rooms[index]).items()
            next_room = list_rooms[index + 1]
            direction = next(
                (direction for direction, room in current_exits if room == next_room), None)
            self.player.travel(direction)
            self.traversal_path.append(direction)
            self.check_coordinates()

    # Check coordinates in each room to review for adjacency
    def check_coordinates(self, starting_room=None):
        starting_room = starting_room or self.player.current_room

        current_coordinates = self.get_coordinates(starting_room.id)
        current_exits = self.get_exits(starting_room.id)
        current_room_id = starting_room.id

        directions = ['n', 's', 'e', 'w']

        if directions[0] in current_exits and current_exits[directions[0]] == '?':
            coordinates_to_check = (
                current_coordinates[0], current_coordinates[1] + 1)
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[0])

        if directions[1] in current_exits and current_exits[directions[1]] == '?':
            coordinates_to_check = (
                current_coordinates[0], current_coordinates[1] - 1)
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[1])

        if directions[2] in current_exits and current_exits[directions[2]] == '?':
            coordinates_to_check = (
                current_coordinates[0] + 1, current_coordinates[1])
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[2])

        if directions[3] in current_exits and current_exits[directions[3]] == '?':
            coordinates_to_check = (
                current_coordinates[0] - 1, current_coordinates[1])
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[3])

    # Check if an adjacent room already exists; if so, add a connection
    def check_for_adjacent_room(self, current_room_id, adjacent_coordinates, direction):
        room_id = next(
            (id for id, value in self.rooms.items() if value[1] == adjacent_coordinates), None)

        if room_id:
            self.add_connection(current_room_id, room_id, direction)