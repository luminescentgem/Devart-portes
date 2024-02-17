import Room

rooms = [
    Room()
]

class Game:
    def __init__(self, index=0):
        self.current_room = rooms[index]
        self.index = index

    def load_next_room(self):
        self.index += 1
        self.current_room = rooms[self.index]

    def play(self):
        print("Welcome to the game!")
        if self.current_room:
            self.current_room.nextLine()
