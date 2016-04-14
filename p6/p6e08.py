class Animal:
    def speak(self): print('*animalic sound*')
    def reply(self): self.speak()

class Mammal(Animal):
    def speak(self): print('nugh nugh')

class Cat(Mammal):
    def speak(self): print('meaow')

class Dog(Mammal):
    def speak(self): print('woof')

class Primate(Mammal):
    def speak(self): print('ugh ugh')

class Hacker(Primate):
    pass # def speak(self): print('Hello World!')

if __name__ == '__main__':
    jacky = Dog()
    jacky.reply()

    ahi = Hacker()
    ahi.reply()


