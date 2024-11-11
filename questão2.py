def is_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0


numero = 34


if is_fibonacci(numero):
    print(f'{numero} pertence a sequência de Fibonacci')

else:
    print(f'{numero} não pertence a sequência de Finonacci')
