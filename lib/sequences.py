#!/usr/bin/env python3



def print_fibonacci(length):
    a=0
    b=1
    result=[]
    for i in range(length):
        result.append(a)
        c=a+b
        a=b
        b=c
    print(result)
        
    
print_fibonacci(9)