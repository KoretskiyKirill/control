#сложный уровень C


try:
    num_1 = int(input())
    print(num_1, 'кб')
    num_1 = 1024 * num_1
    print(num_1, 'мб')
    num_1 = 1024 * num_1
    print(num_1, 'бит')
    print(num_1 * 8, 'байт')
except(ValueError):
    print('сюда нужна цифра')
