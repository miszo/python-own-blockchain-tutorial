# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_tansaction(transaction_amount, last_transaction=[1]):
    """ Append a new transaction to the blockchain with last blockchain value

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default[1]).
    """
    if last_transaction == None:
        blockchain.append([transaction_amount])
    else:
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


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_tansaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) > 0:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list.')
    if not verify_chain():
        print('Invalid blockchain!')
        break


print('Done!')
