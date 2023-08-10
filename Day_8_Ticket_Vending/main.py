import ticket_vending

def ask():
    while True:
        try:
            my_product = input('Choose your product: ').upper()
            ['P', 'M', 'C'].index(my_product)
        except ValueError:
            print('That is not a valid option')
        else:
            break
    
    ticket_vending.decorate_tickets(my_product)

def start():
    while True:
        ask()
        try:
            another_ticket = input('Do you want another ticket? Y or N').upper()
            ['Y', 'N'].index(another_ticket)
        except ValueError:
            print('Not a valid option')
        else:
            break

start()