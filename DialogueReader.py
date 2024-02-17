def numeric(value):
    return float(value) if value.isnumeric() else value

def cutAttributes(dialogues, name, attributes):
    attributes = attributes.split('-')
    dialogues[name][-1]["values"] = [numeric(value) for value in attributes]
    print("\ncutattributes(result) =  ", dialogues[name])

def cutPart(dialogues, part):
    raw_data = part.split('\n')[1:]
    name = raw_data[0]
    dialogues[name] = []
    for line in raw_data[1:]:
        print("\ncutpart(input) = \"" + line + "\"", bool(line))
        if line and line[0] == "$":
            dialogues[name].append({"character": line[1], "line": line[2:]})
        elif line:
            cutAttributes(dialogues, name, line)
        print("\ncutpart(result) = ", dialogues[name])

def readDialogues(file="dialogues_2.txt"):    
    dialogues = {}
    file = open(file, "r").read()
    for part in file.split('&'):
        cutPart(dialogues, part)

    return dialogues

print(readDialogues())
