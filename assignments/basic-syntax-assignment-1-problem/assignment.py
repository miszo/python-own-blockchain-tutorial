# 1 Create two variables – one with your name and one with your age
name = 'Miszo'
age = 31

# 2 Create a function which prints your data as one string
def greet():
    """ Prints your name and age (global variables). """
    print('Hi ' + name + '! You are ' + str(age) + ' years old.')

greet()
# 3 Create a function which prints ANY data (two arguments) as one string
def print_strings(str1, str2):
    """ Prints statement with two strings passed as arguments
    Arguments:
        :str1: String one.
        :str2: String two.
    """
    print('Statement with ' + str1 + ' and ' + str2 + '.')

print_strings('Starsky', 'Hutch')
# 4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def decades_lived(your_age):
    """ Calculates and returns the number of decades you already lived
    Arguments:
        :your_age: Your age (int).
    """
    return int(your_age // 10)

print(decades_lived(31))
