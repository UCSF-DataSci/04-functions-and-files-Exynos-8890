#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse
def fib_gen(an_argument):
    fib = [0,1]
    max = 1
    while(max < an_argument):
        fib.append(max)
        max = fib[-1]+fib[-2]
    return fib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('count',type = int,default = 100,help = 'limit of a Fibonacci Sequence')
    args = parser.parse_args()
    output = str(fib_gen(args.count))
    with open("fibonacci_100.txt",'w') as files:
        files.write(output)