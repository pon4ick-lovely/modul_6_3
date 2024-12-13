import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    x = 0
    y = 0
    z = 0
    _cards = [x, y, z]

    def __init__(self, speed):

        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            Animal.x = dx * self.speed
            Animal.y = dy * self.speed
            Animal.z = dz * self.speed

    def get_cords(self):
        print(f'X: {Animal.x} Y: {Animal.y} Z: {Animal.z}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_number = random.randint(1, 4)
        print(f'Here are(is) {random_number} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        Animal.z = (Animal.z / 2) - abs(dz)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()