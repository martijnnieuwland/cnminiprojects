from random import randint


class Fighter:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def fight(self):
        attack = randint(0, 10)
        strike = attack + self.strength / 10
        return strike


class Opponent(Fighter):
    def __init__(self, name, strength):
        super().__init__(name, strength)


class Hero(Fighter):
    def __init__(self, name, strength=2):
        super().__init__(name, strength)

    @staticmethod
    def pick_opponent():
        global opponent
        print(f"Who will you fight now?")
        choice = input(f"[c] {cinderella.name} is {cinderella.strength} strong\n"
                       f"[y] {yogi.name} is {yogi.strength} strong\n"
                       f"[m] {martijn.name} is {martijn.strength} strong\n"
                       f": ")
        if choice == "c":
            opponent = cinderella
        elif choice == "y":
            opponent = yogi
        elif choice == "m":
            opponent = martijn
        return opponent


def get_hero():
    print("Welcome contestant to virtual MMA!")
    player = Hero(input("What is your name? "))
    return player


hero = get_hero()
cinderella = Opponent("Cinderella", 1)
yogi = Opponent("Yogi Bear", 3)
martijn = Opponent("Martijn", 5)
opponent = cinderella
