import Room

class MainRoom(Room):
    def __init__(self):
        self.name = "main"
        self.dialogue = ["", ""]
        self.door = None
        self.exit = None

    def linkExit(self, exit):
        self.exit = exit
    
    def closeRoom(self):
        if self.door:
            self.door.fadeOut()
        self.door = None