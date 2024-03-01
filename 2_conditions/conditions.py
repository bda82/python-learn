# условия

a = -10

# обычное условие (>, <, >=, <=, ==, !=)
if a > 0:
    print('positive')
else:
    print('negative or zero')

# множественное условие (>, <, >=, <=, ==, !=)
if a >= 0:
    print('positive')
elif a == 0:
    print('zero')
else:
    print('negative')

# сравнение строк
month: int = 4

if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
else:
    print('Unknown month')

# pattern matching (Python 3.10+)
month: int = 1

match month:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case _:
        print('Unknown month')
