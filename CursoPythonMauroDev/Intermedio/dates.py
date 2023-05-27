### dates ###
from datetime import datetime

now = datetime.now()

print(now.timestamp())


def fibonacci(n):
    fib_seq = [0, 1]  # Iniciamos la secuencia con los primeros dos números: 0 y 1

    while fib_seq[-1] < n:
        next_num = fib_seq[-1] + fib_seq[-2]  # Calculamos el siguiente número sumando los dos últimos
        fib_seq.append(next_num)

    return fib_seq

fibonacci_seq = fibonacci(50)

print(fibonacci_seq)