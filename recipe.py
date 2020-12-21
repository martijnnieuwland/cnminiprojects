class Ingredient:
    """Models an ingredient."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def expire(self):
        if self.name == 'salt':
            print(f"{self.name} never expires! Ask the sea!")
        else:
            print(f"eh... sorry but that {self.name} actually went bad!")
            self.name = "expired " + self.name


class Vegetable(Ingredient):
    def chop(self):
        print(f"Your {self.amount} {self.name} are now chopped!")


class Soup:

    def __init__(self, recipe):
        self.recipe = recipe

    def cook(self):
        name = ''
        for i in self.recipe:
            name += i.name
        return name

    def serves(self):
        people = 0
        for i in self.recipe:
            people += i.amount
        return int(people / 2)

    def __str__(self):
        return f"Yummy {self.cook()} soup for {self.serves()} people!"


carrot = Ingredient('Carrot', 3)
pumpkin = Ingredient('Pumkin', 1)
soup = Soup([pumpkin, carrot])
soup.cook()
print(soup)
