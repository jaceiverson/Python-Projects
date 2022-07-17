#fibanaci numbers with a speed check to see if arrays or lists are faster
#I wanted to find a breakeven point for the speed

import numpy as np
import time

def usingArray(x,y,num):
    fib = np.zeros(num,dtype=np.float64)
    for i in range(len(fib)):
        fib[i]=x
        if i==0:
            y=0
            x=1
        else:
            x+=y
            y=fib[i]

    return fib

def usingList(x,y,num):

    fib = []
    for i in range(num):
        fib.append(x)
        if i==0:
            y=0
            x=1
        else:
            x+=y
            y=fib[i]

    return fib

def oneValue():
    #if you wanted the user to input one value
    num = int(input('How many numbers do you want? '))
    num += 1
    x = 0
    y = 1
    t0a = time.time()
    usingArray(x, y, num)
    t1a = time.time()
    x = 0
    y = 1
    t0l = time.time()
    usingList(x, y, num)
    t1l = time.time()

    speedArray= t1a - t0a
    speedList= t1l - t0l

    #for testing one value only, couple this with
    print(f'Speed for an array is: {speedArray: .10f}. Speed for a list is: {speedList: .10f}')
    if speedList>speedArray:
        print(f'The array is faster by: {speedList-speedArray: .10f}')
    else:
        print(f'The list is faster by: {speedArray-speedList: .10f}')

def breakevenPoint():

    speedArray = [0]
    speedList = [0]
    num = 0
    while speedList[-1] <= speedArray[-1]:
        num += 1
        x = 0
        y = 1
        t0a = time.time()
        usingArray(x, y, num)
        t1a = time.time()
        x = 0
        y = 1
        t0l = time.time()
        usingList(x, y, num)
        t1l = time.time()


        speedList.append(t1l - t0l)
        speedArray.append(t1a - t0a)

    print(f'Finally at {num}, was the array faster than the list.\n'
          f'The speeds were: List: {speedList[-1]: .10f}. Array: {speedArray[-1]:.10f}\n'
          f'Array is faster by {speedList[-1]-speedArray[-1]:.10f}')

if __name__=='__main__':
    #this will get user input and print the number of fibanaci numbers that you want
    oneValue()

    #this will find the breakeven point where a array becomes faster than the list
    #breakevenPoint()
