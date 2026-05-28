budget = int(input())
all_price = 0
while True:
    new = input()
    if new == "End":
        print('You bought everything needed.')
        break
    else:
        prices = int(new)
        all_price += prices
        if all_price > budget:
            print("You went in overdraft!")
            break