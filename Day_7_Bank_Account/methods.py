class Bird:

    wings= True

    def __init__(self, color, species):
        self.color = color
        self.species = species

    def chirp(self):
        print('tweet, I am {}'.format(self.color))

    def fly(self, feet):
        print(f'the bird flies {feet} feet')

    def paint_black(self):
        self.color = 'black'
        print(f'Now the bird is {self.color}')

    @classmethod
    def lay_eggs(cls, number):
        print(f'it laid {number} eggs')

    @staticmethod
    def look():
        print('look at me')

# tweetie = Bird('yellow', 'canary')
# tweetie.chirp()
# tweetie.fly(164)
# tweetie.paint_black()
# tweetie.wings = False
# print(tweetie.wings)

# Bird.lay_eggs(3)
Bird.look()