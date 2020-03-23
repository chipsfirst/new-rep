class Rider:
    def __init__(self, ridername):
        self.ridername = ridername


class Horse:
    def __init__(self, horsename, owner):
        self.horsename = horsename
        self.owner = owner


rider = Rider("Geralt")
horse = Horse("Plotva", rider)

print(horse.owner.ridername + " on the " + horse.horsename)

