class Animal:

    def __init__(self, age, color) -> None:
        self.age = age
        self.color = color

    def born(self):
        print('This animal has been born')
    
    def talk(self):
        print('this animal makes a sound')

class Bird(Animal):

    def __init__(self, age, color, altitude) -> None:
        super().__init__(age, color)
        self.altitude = altitude

    def talk(self):
        print('chirp')
    
    def fly(self, feet):
        print(f'this bird flies {feet} feet')


tweetie = Bird(2, 'yellow', 196)
print(tweetie.color)
tweetie.born()
tweetie.fly(328)