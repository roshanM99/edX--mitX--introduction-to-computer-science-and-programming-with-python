# Lecture 12.5, slide 3

def genFib():
    """
    Generates the fibonacci sequence.
    """
    fibn_1 = 1 # fib(n - 1)
    fibn_2 = 0 # fib(n - 2)
    while True:
        # fib(n) = fib(n - 1) + fib(n - 2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next