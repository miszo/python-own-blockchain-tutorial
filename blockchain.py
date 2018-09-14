# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new transaction to the blockchain with last blockchain value

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default[1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Asks user for transaction amount and returns it as a float """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    """ Output blockain into console """
    for block in blockchain:
        print('Outputting block')
        print(block)
        print('-'*10)

""" Get the first transaction input and add value to the blockchain """
add_value(get_transaction_value())

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()

print('Done!')
