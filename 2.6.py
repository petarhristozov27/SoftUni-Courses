num_string = int(input())

for _ in range(num_string):
    j = input()

    if ("," in j) or ("_" in j) or ("." in j):
        print(f"{j} is not pure!")
    else:
        print(f"{j} is pure.")