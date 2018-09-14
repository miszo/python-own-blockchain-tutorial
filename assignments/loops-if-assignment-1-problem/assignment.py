# 1) Create a list of names and use a for loop to output the length of each name (len()).
names_list = ['Emilka', 'Kinga', 'Miszo', 'Monika', 'Filip', 'Janusz', 'Maja', 'Ola']

for name in names_list:
    print(name + ', length: ' + str(len(name)))
else:
    print('-' * 20)


# 2) Add an if check inside the loop to only output names longer than 5 characters.
for name in names_list:
    if len(name) > 5:
        print(name + ', length: ' + str(len(name)))
else:
    print('-' * 20)


# 3) Add another if check to see whether a name includes a “n” or “N” character.
for name in names_list:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(name + ', length: ' + str(len(name)))
else:
    print('-' * 20)


# 4) Use a while loop to empty the list of names (via pop())
while len(names_list) > 0:
    names_list.pop()
else:
    print('Names list is now empty!')
