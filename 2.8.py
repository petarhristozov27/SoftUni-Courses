points = 0
bol = True
while True:
    type_act = str(input())
    if type_act == "END":
        break
    if type_act == "dog" or type_act == "cat" or type_act == "movie" or type_act == "coding":
        points += 1
    elif type_act == "DOG" or type_act == "CAT" or type_act == "MOVIE" or type_act == "CODING":
        points += 2
    else:
        continue
    points += 0
    if points > 5:
        print("You need extra sleep")
        bol = False
        break
if bol == True:
    print(points)
