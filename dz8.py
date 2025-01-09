import random

class Animal: #класс описывающий животных
    live = True
    sound = None #звук
    _DEGREE_OF_DANGER = 0 #степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве.
        self.speed = speed #скорость передвижения существа

    def move(self, dx, dy, dz):  #меняет соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self): #выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self): #выводит "Sorry, i'm peaceful :)", если ст. опасности меньше 5 и "Be careful, i'm attacking you 0_0", если равно или больше
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self): #выводит строку со звуком sound
        print(self.sound)

class Bird(Animal):
    beak = True #наличие клюва

    def lay_eggs(self): # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        egg = random.randint(1, 4)
        print(f"Here is(are) {egg} egg(s) for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # dz изменение координаты z в _cords.
        new_z = self._cords[2] - abs(dz) * .5 * self.speed
        self._cords[2] = max(new_z, 0)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal): # класс, описывающий утконоса
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)
    def speak(self):
        print(self.sound)


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
