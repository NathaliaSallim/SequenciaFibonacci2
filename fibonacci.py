def fibonacci_sequence(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

def is_in_fibonacci_sequence(n):
    fib = fibonacci_sequence(n)
    if n in fib:
        return True
    else:
        return False

n = int(input("Digite um número: "))
if is_in_fibonacci_sequence(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
