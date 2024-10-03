#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
import argparse
import fibonacci
from math import sqrt
def is_prime(n):
    for i in range(2,int(sqrt(n))+2):
        if n % i ==0:
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',"--count",type = int, default= 50000, help = 'limit of a fibonacci sequence')
    args = parser.parse_args()
    fib_list = fibonacci.fib_gen(args.count)
    first_prime = 0
    for i in range(1,len(fib_list)-1):
        if is_prime(fib_list[-i]):
            first_prime = fib_list[-i]
            break
    print(first_prime)


