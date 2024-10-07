#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0, 1]
    if length == 0:
        print([]) 
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        for i in range(length - 2):
            fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i+1])
        print(fibonacci_list)
            
print_fibonacci(100)
            
        
        
        
        
        
        
        