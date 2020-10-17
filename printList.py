people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

to_print = ""
while people:
    while len(people[0]) > 1:
        to_print += (people[0][0] + " " + people[0][1] + "\n")
        people.remove(people[0])
    to_print += (people[0][0] + "\n")
    people.remove(people[0])

print(to_print)
