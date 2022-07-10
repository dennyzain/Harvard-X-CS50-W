import sys

try:
    x=int(input('x: '))
    y=int(input('y: '))
except ValueError:
    print('input value is invalid')
    sys.exit(1)

try :
    result=x/y
    print(f'{x} / {y} = {result}')
except ZeroDivisionError:
    print('zero divide is invalid result')
    sys.exit(1)
