num_of_sent_mess = int(input())
result = ""
for i in range(1, num_of_sent_mess + 1):
    new = int(input())
    if new == 88:
        result = "Hello"
        print(result)
    elif new == 86:
        result = "How are you?"
        print(result)
    elif new != 86 and new < 88:
        result = "GREAT!"
        print(result)
    elif new > 88:
        result = "Bye."
        print(result)