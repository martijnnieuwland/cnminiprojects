import characters as c

opponent = c.cinderella


def intro():
    print(f"""Good luck {c.hero.name}!
Your relative strength is {c.hero.strength}.
We'll start you off easy against {opponent.name}.
She has a relative strength of {opponent.strength}!
Now what will you do?""")


def play():
    print(f"You're fighting {opponent.name}!")
    choice = input("[a] Attack\n"
                   "[r] Run away\n"
                   ":  ")
    if choice == 'a':
        hero_strike = c.hero.fight()
        opponent_strike = opponent.fight()
        print(f"{c.hero.name} attacks... strikes with a power of {hero_strike}")
        print(f"{opponent.name} strikes back with {opponent_strike} force!")
        if hero_strike > opponent_strike:
            c.hero.strength += 1
            print(f"{c.hero.name} wins!  Your strength is now {c.hero.strength}")
        else:
            c.hero.strength -= 1
            print(f"{opponent.name} wins!  Your strength is now {c.hero.strength}")
            if c.hero.strength == 0:
                print("You die!")
    else:
        c.hero.strength -= 1
        print(f"{c.hero.name} retreats and loses the fight!!  Your strength is now {c.hero.strength}")
        if c.hero.strength == 0:
            print("You die!")


intro()
while c.hero.strength > 0:
    play()
    while c.hero.strength > 0:
        opponent = c.hero.pick_opponent()
        break
