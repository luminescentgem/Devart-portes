from classes.Game import Game
from classes.Room import Room

def main():
    # Create rooms
    room1 = Room("Room 1", "This is the first room.", {"north": None, "east": None, "south": None, "west": None})
    room2 = Room("Room 2", "This is the second room.", {"north": None, "east": None, "south": None, "west": None})

    # Set exits
    room1.exits["east"] = room2
    room2.exits["west"] = room1

    # Load game
    game = Game()
    game.load_room(room1)

    # Play game
    game.play()


if __name__ == "__main__":
    main()
