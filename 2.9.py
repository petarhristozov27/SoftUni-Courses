house = ""
letter_count = 0
while True:
    name = str(input())
    letter_count = 0
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for i in name:
        letter_count += 1
        if letter_count < 5:
            house = "Gryffindor"
        elif letter_count == 5:
            house = "Slytherin"
        elif letter_count == 6:
            house = "Ravenclaw"
        else:
            house = "Hufflepuff"
    print(f"{name} goes to {house}.")
