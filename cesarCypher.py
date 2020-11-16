alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


for l in secret:
    if not l.isalpha():
        print(l, end="")
    elif alphabet.index(l) + cipher > 52:
        print(alphabet[alphabet.index(l) + cipher - 52], end="")
    else:
        print(alphabet[alphabet.index(l) + cipher], end="")
