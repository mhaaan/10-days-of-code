def perfurme():
    for p in range(1,10000):
        yield f'P-{p + 1}'

def cosmetics():
    for c in range(1,10000):
        yield f'C-{c + 1}'

def medicine():
    for m in range(1,10000):
        yield f'M-{m + 1}'

p = perfurme()
c = cosmetics()
m = medicine ()

def decorate_tickets(product):

    print('Your Number is:')
    if product == 'p':
        print(next(p))
    elif product == 'c':
        print(next(c))
    else:
        print(next(m))
    print('Please wait and we will be right with you')