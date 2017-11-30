
Zero = ['*****',
        '*   *',
        '*   *',
        '*   *',
        '*   *',
        '*****']
One = ['  *',
       ' **',
       '* *',
       '  *',
       '  *',
       '  *']
Two = [' *****',
       ' *   *',
       '    * ',
       '   *  ',
       '  *   ',
       ' *****']
Three = ['*****',
         '   * ',
         '  *  ',
         '  *  ',
         '    *',
         '*****']
Four = ['*   *',
        '*   *',
        '*   *',
        '* * *',
        '    *',
        '    *']
Five = ['*****',
        '*    ',
        '* ** ',
        '    *',
        '    *',
        '**** ']
Six = ['* * *',
       '*    ',
       '* * *',
       '*   *',
       '*   *',
       '* * *']
Seven = ['* * *',
         '    *',
         '    *',
         '   * ',
         '  *  ',
         ' *   ']
Eight = ['*****',
         '*   *',
         ' *** ',
         ' *** ',
         '*   *',
         '*****']
Nine = ['* * *',
        '*   *',
        '* * *',
        '    *',
        '    *',
        '* * *']

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = input('Input your number: ')
    row = 0
    while row < 7:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for el in digit[row]:
                if el == '*':
                    el = str(number)
                line += el
            line += '   '
            column += 1
        print(line)
        row += 1
except IndexError:
    print('IndexError happened!')
except ValueError as err:
    print(err)
