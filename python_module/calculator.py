import module

print('  Menu')
print(' ---------')
print('  1 : add')
print('  2 : sub')
print('  3 : multiply')
print('  4 : divide')
print('  5 : stop')
while True:
    number = int(input(' : '))
    if number == 5:
        print('The Calculator is ended.')
        break
    if number > 5:
        print('Enter Right Number!')
        number = int(input(' : '))
    num1 = int(input('num1 : '))
    num2 = int(input('num2 : '))
    calNum = module.fourCal(num1,num2)
    if number == 1:
        print(calNum.add())
    elif number == 2:
        print(calNum.subtract())
    elif number == 3:
        print(calNum.multiply())
    elif number == 4:
        print(calNum.division())
