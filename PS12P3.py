with open('data3.txt', 'r') as f:
    data = f.readlines()


lastnames = []
scores = []
for line in data:
    fields = line.strip().split()
    lastnames.append(fields[0])
    scores.append(int(fields[1]))

def displayextremes(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0
    
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    
    print("Highest score: " + names[high_index] + " - " + str(high_var))
    print("Lowest score: " + names[low_index] + " - " + str(low_var))

displayextremes(lastnames, scores)