# Задание 1. Факториал

def fac(n):
    facl=1
    for i in range(2,n+1):
         facl*=i   
    return facl

# Задание 2. Наибольший общий делитель (НОД) для двух целых чисел

def gcd(a, b):   
    while(a!=0 and b!=0):
        if a>b:
            a=a%b
        else: b=b%a
    return (a+b)
      

# Задание 3. Генератор для ряда Фибоначчи

# def fib():
#     a,b=1,1
#     while True:
#        yield  a
#        a,b=b,a+b

    



# Задание 4. Напишите реализацию функции is_palindrome, которая проверяет, является ли последовательность палиндромом
#
# >>> is_palindrome('aba')
# True
# >>> is_palindrome('abc')
# False
# >>> is_palindrome([1, 2, 3, 2, 1])
# True

def is_palindrome(seq):
    pal=seq[::-1]
    if pal==seq:
        return True
    else: return False
    
     


# Задание 5. Напишите реализацию функции is_unique, которая проверяет, содержит ли последовательность только уникальные элементы.
# >>> is_unique([1, 2, 3, 2, 1])
# False
# >>> is_unique([1, 2, 3, 4, 5])
# True

def is_unique(seq):
    s=set(seq)
    if len(s)==len(seq):
        return True
    else:
        return False


# Задание 6. Напишите реализацию функции, которая вычисляет контрольную сумму последовательности чисел по модулю 10. Аргумент -- строку, содержащую только цифры, -- необходимо преобразовать в последовательность чисел, вычислить их сумму, и вернуть остаток от деления на 10.
# Пример: '12345' -> [1, 2, 3, 4, 5] -> 15 -> 5
#
# >>> checksum('123')
# 6
# >>> checksum('1234')
# 0
# >>> checksum('12345')
# 5

def checksum(code):
    # code=int(code)
    code_l=list(code)
    code_ld=[int(_) for _ in code_l]
    print (code_ld)
    code_sum=sum(code_ld)
    return code_sum%10


# Задание 7*. Преобразование вложенных последовательностей
#
# >>> flatten([])
# []
# >>> flatten([1, 2])
# [1, 2]
# >>> flatten([1, [2, [3]]])
# [1, 2, 3]
# >>> flatten([(1, 2), (3, 4)])
# [1, 2, 3, 4]

def flatten(seq):
    res = []
    for i in seq:
        print(type(i))
        # приводим к списку
        if type(i)== set or type(i)==tuple:
            i=list(i)
        # Добавляем к списку элемент
        if type(i) != list:
            res.append(i)
        # иначе вызываем рекурсию
        else:
            res += flatten(i) 
    return res
