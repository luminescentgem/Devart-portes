class Room:
    def __init__(self, name, dialogue, mainroom, size=[64, 64, 64]):
        self.name = name
        self.dialogue = dialogue
        self.dialogueIndex = -1
        self.door = mainroom
        self.size = size
        self.elements = [[[None for _ in range(size[2])] for _ in range(size[1])] for _ in range(size[0])]

    def getElementAt(self, position):
        return self.elements[position[0]][position[1]][position[2]]
    
    def setElementAt(self, element, position, size=(1, 1, 1)):
        for x in range(position[0], position[0] + size[0] + 1):
            for y in range(position[1], position[1] + size[1] + 1):
                for z in range(position[2], position[2] + size[2] + 1):
                    self.elements[x][y][z] = element
    
    def removeElementAt(self, position, size=(1, 1, 1)):
        for x in range(position[0], position[0] + size[0] + 1):
            for y in range(position[1], position[1] + size[1] + 1):
                for z in range(position[2], position[2] + size[2] + 1):
                    self.elements[x][y][z] = None
    
    def findElement(self, element, size=(1, 1, 1)):
        for x in range(0, self.size[0], size[0]):
            for y in range(0, self.size[1], size[1]):
                for z in range(0, self.size[2], size[2]):
                    if self.elements[x][y][z] == element:
                        return (x, y, z)
        return -1
    
    def findOrigin(self, element, inacurate_position):
        pos = list(inacurate_position)
        
        while pos[0] > 0 and self.elements[pos[0]-1][pos[1]][pos[2]] == element:
            pos[0] -= 1
            
        while pos[1] > 0 and self.elements[pos[0]][pos[1]-1][pos[2]] == element:
            pos[1] -= 1
            
        while pos[2] > 0 and self.elements[pos[0]][pos[1]][pos[2]-1] == element:
            pos[2] -= 1
        
        return tuple(pos)
                 
    def getSizeOfElement(self, position):
        element = self.getElementAt(position)
        if element.size: return element.size
        
        startingPosition = self.findOrigin(element, position)
        
        pos = list(startingPosition)
        
        while pos[0] < self.size[0]-1 and self.elements[pos[0]+1][pos[1]][pos[2]] == element:
            pos[0] += 1
            
        while pos[1] < self.size[1]-1 and self.elements[pos[0]][pos[1]+1][pos[2]] == element:
            pos[1] += 1
            
        while pos[2] < self.size[2]-1 and self.elements[pos[0]][pos[1]][pos[2]+1] == element:
            pos[2] += 1
        
        return (pos[i] - startingPosition[i] for i in range(3))
    
    def getNextDialogueLine(self):
        self.dialogueIndex += 1
        return self.dialogue[self.dialogueIndex]
    
    def increaseDialogueCounter(self, i=1):
        self.dialogueIndex += i
    
    def decreaseDialogueCounter(self, i=1):
        self.dialogueIndex -= i
    
    def fadeOut(self):
        del self