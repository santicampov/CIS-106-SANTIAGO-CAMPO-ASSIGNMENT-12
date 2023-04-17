lastnames = ['Campo', 'Pfister', 'Williams', 'Espinosa', 'Jurek', 'Jones', 'Gates', 'Musk', 'Jordan', 'Patton']
escores = [77, 56, 70, 85, 72, 97, 99, 74, 88, 87]

#functions
def display(names, scores):
    for i in range(len(names)):
        print(names[i] + ": " + str(scores[i]))


def displayreverse(names, scores):
    for i in range(len(names)-1, -1, -1):
        print(names[i] + ": " + str(scores[i]))

#call functions
display(lastnames, escores)

displayreverse(lastnames, escores)