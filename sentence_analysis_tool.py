# Take a sentence from the user
sentence = input("Say something: ")

# Count and store the characters
lowercase = 0
uppercase = 0
punctuation = 0

for i in sentence:
    if i.isspace():
        pass
    elif i.islower():
        lowercase += 1
    elif i.isupper():
        uppercase += 1
    elif i.isascii():
        punctuation += 1

total = (lowercase + uppercase + punctuation)

# Output the re
print("So get this, here's what you said:")
print("Uppercase:", uppercase)
print("Lower case:", lowercase)
print("Punctuation:", punctuation)
print("Total chars:", total)
