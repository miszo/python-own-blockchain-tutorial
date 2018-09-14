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


def get_user_input():
    """ Asks user for transaction amount and returns it as a float """
    return float(input('Your transaction amount please: '))


""" Get the first transaction input and add value to the blockchain """
add_value(get_user_input())

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    """ Output blockain into console """
    for block in blockchain:
        print('Outputting block')
        print(block)
        print('-'*10)

print('Done!')
