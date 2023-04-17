def displayplayers(names, averages):
    print("Player Name\tBatting Average")
    for i in range(len(names)):
        print(names[i] + "\t\t" + str(averages[i]))

def searchplayer(names, averages):
    while True:
        searchname = input("Enter a player's name to search or press x to exit: ")
        if searchname == 'x':
            break
        found = False
        for i in range(len(names)):
            if names[i].lower() == searchname.lower():
                print(names[i] + "\t\t" + str(averages[i]))
                found = True
                break
        if not found:
            print("Not found, try again")

names = []
averages = []
with open("data4.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        names.append(data[0])
        averages.append(float(data[1]))

displayplayers(names, averages)

searchplayer(names, averages)