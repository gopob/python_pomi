symbol = chr(9608)
text = '''
What do you choose?
    1. Draw a square
    2. Draw a tower upside down
    3. Stop
'''
while True:
    try:
        print(text)
        choice = int(input(''))
        if choice < 1 and choice > 3:
            print('Enter a valid choice: 1, 2 or 3!')
            continue
        if choice == 1:
            try:
                dimension = int(input('Give a dimension for your construction: '))
                if dimension < 1:
                    print('Enter a integer number')
                    continue
                else:
                    for i in range(dimension):
                        for j in range(dimension):
                            print(symbol, end='')
                        print()
            except:
                print('Entered a wrong value')

        if choice == 2:
            try:
                dimension = int(input('Give a dimension for your construction: '))
                divider = dimension
                if dimension < 1:
                    print('Enter a integer number')
                    continue
                else:
                    for i in range(dimension):
                        for h in range(dimension):
                            for j in range(i + 1):
                                print(' ', end='')
                            for j in range(dimension):
                                print(symbol, end='')
                            print()
                        dimension -=2
            except:
                print('Entered a wrong value')
        if choice == 3:
            print('Thanks for playing with us!')
            break
    except:
        print('Entered a wrong value')
        continue

