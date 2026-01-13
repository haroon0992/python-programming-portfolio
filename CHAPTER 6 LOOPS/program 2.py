#program 2
total = 0
integer_number =  int (input('enter a integer number: '))

while integer_number != 0:
    total += integer_number

    integer_number = int(input('enter a number: '))
print('total =', total)