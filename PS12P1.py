lastnames = ['Campo', 'Pfister', 'Williams', 'Espinosa', 'Jurek', 'Jones', 'Gates', 'Musk', 'Jordan', 'Patton']

#funtion
def displaynames(names):
    for name in names:
        print(name)

#function in reverse order
def displayreverse(names):
    for name in reversed(names):
        print(name)

#call funtion
displaynames(lastnames)

#call function
displayreverse(lastnames)