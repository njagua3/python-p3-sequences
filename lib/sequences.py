#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the desired length
    for i in range(2, length):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    
    # Print the Fibonacci sequence
    print(fib_sequence[:length])

# Example usage:
print_fibonacci(9)
