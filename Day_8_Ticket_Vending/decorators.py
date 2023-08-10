def decorate_greeting(function):
    def another_function(word):
        print('Hello')
        function(word)
        print('Goodbye')
    return another_function



def uppercase(text):
    print(text.upper())


def lowercase(text):
    print(text.lower())

decorated_uppercase = decorate_greeting(uppercase)

decorated_uppercase('me')