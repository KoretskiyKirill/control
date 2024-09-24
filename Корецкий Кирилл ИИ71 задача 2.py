#сложный уровень C
try:
    lin = int(input())
    let = int(input())
except(ValueError):
    print('пиши цифру')
sim = lin * let * 2
print(sim * 5,'байт',sep='-')
