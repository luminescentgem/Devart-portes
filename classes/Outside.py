import Room

class Outside(Room):
    def __init__(self, mainroom):
        self.name = "outside"
        self.dialogue = ["", ""]
        self.exits = mainroom
    
    