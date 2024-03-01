# функции

# простая функция
def hello_world():
    print('Hello, World!')

hello_world()

def return_none() -> None:
    pass

aaa = return_none()  # вернет None

# функция с параметром
def square(x: int):
    return x ** 2

print('результат квадрата =', square(2))

# функция с несколькими параметрами
def add(a: int, b: int):
    return a + b

print('результат сложения =', add(2, 3))

def power(a: int, b: int):
    return a ** b

# задание параметров функции по позиции
print(f'результат возведения в степень (где a = 2, b = 3) =', power(2, 3))
print(f'результат возведения в степень (где a = 3, b = 2) =', power(3, 2))

# задание параметров функции по имени
print(f'результат возведения в степень (где a = 2, b = 3) =', power(a=2, b=3))
print(f'результат возведения в степень (где a = 3, b = 2) =', power(b=2, a=3))

# функция с параметром по умолчанию
def power_default(a: int, b: int = 2):
    return a ** b

print(f'результат возведения в степень (где a = 2, b = 3) =', power_default(2, 3))  # тут он видит что задано 2 параметра и берет оба
print(f'результат возведения в степень (где a = 3, а b - не задается, оно берется по умолчанию) =', power_default(3))  # а тут он видит, что задан только 1 параметр и берет второй по умолчанию

# функция с неопределенным количеством параметров
def sum_all(*args):
    print('args =', args)
    for arg in args:
        print('arg =', arg)
    return sum(args)

print(f'результат суммы всех параметров (где a = 1, b = 2, c = 3) =', sum_all(1, 2, 3))
print(f'результат суммы всех параметров (где a = 1, b = 2, c = 3, d = 4) =', sum_all(1, 2, 3, 4))

# функция с неопределенным количеством именованных параметров
def print_all_kwargs(**kwargs):
    print('kwargs =', kwargs)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    print('new_variable =', kwargs.get('new_variable'))
    print('unexpected_variable_1 =', kwargs['unexpected_variable']
    print('unexpected_variable_2 =', kwargs.get('unexpected_variable'))


print('print_all_kwargs')
print_all_kwargs(a=1, b=2, c=3, new_variable=4)