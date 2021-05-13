#https://www.codewars.com/kata/primes-in-numbers/train/python

def printAnswer(factors):
    #creates a unique set of values used later
    uniqueNums = set(factors)

    #sorts that set smallest to largest
    uniqueNums=sorted(uniqueNums)
    factorList = []

    #makes the string
    for y in uniqueNums:
        count = factors.count(y)
        if count == 1:
            temp = ['(', y, ')']
        else:
            temp = ['(', y, '**', count, ')']
        factorList.append(temp)
    factorString=''
    for x in factorList:
        factorString+="".join(str(x)).replace('[','').replace(']','').replace(',','').replace('\'','').replace(' ','')
    return factorString

def primeFactors(n):
    factors = []
    allNums = 2
    #this makes all the prime factors and stores them in a factors list
    while n != 1:
        while n % allNums == 0:
            factors.append(allNums)
            n = n // allNums
        allNums += 1
    #this sends the list to a function to make it into the formated string
    answer = (printAnswer(factors))
    return answer


print(primeFactors(86240))