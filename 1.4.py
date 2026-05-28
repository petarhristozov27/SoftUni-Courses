n = int(input())
tries = 0
for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f'{number} is odd!')
        break
    if tries == n - 1:
        print(f"All numbers are even.")
        break
    else:
        tries += 1
        continue
