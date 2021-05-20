a = int(input())
b = int(input())
soma = int(0)
if (a > b):
    b = b + 1
    while (b < a):
        if (b%2 != 0):
            soma = soma + b
        b = b + 1
else:
    a = a + 1
    while (a < b):
        if (a%2 != 0):
            soma = soma + b
print(soma)