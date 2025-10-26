def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n): # Here using for loop finding fabonacci.
        sequence.append(a)
        a, b = b, a + b
    return sequence
    
