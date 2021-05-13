#https://www.codewars.com/kata/51b62bf6a9c58071c600001b

"""
try 1
def solution(n):
    # TODO convert int to roman string
    returnString = ""
    returnList=[]
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    while n > 0:
        for x in values:
            counter=0
            while n >= values.get(x):
                returnList.append(x)
                n -= values.get(x)
                counter+=1
                if counter>3:
                    pass

    # for x in range(100):
    # print(f'The number is {x} the value is {solution(x)}.'
    return returnString
"""
"""
try 2
def getKey(dictionary, value):
     for x in dictionary:
         if dictionary.get(x)==value:
             return x

def solution(n):
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    returnList=[]
    while n>0:

        for x in values:

                tester=n//values.get(x)

                if tester >0 and tester<4:

                    for y in range(tester):
                        returnList.append(x)
                        n-=values.get(x)

                subtester=values.get(x)-n

                if subtester in values.values():

                    returnList.append(getKey(values,subtester))
                    returnList.append(x)
                    n=0
                    break

    returnString="".join(returnList)
    return returnString
"""
"""
try 3

def inThreshold(value, t, n):
    if n>value-t:
        return True
    else:
        return False

def solution(n):
    roman=""
    returnList=[]
    symbols=["M", "D", "C", "L", "X", "V", "I"]
    values=[1000,500,100,50,10,5,1]


    for x in values:
        if '5' in str(x):
            threshold=x/5
        else:
            threshold=x/10

    for x in values:
        if inThreshold(x,threshold,n):
        tester = n//x

        if tester > 0 and tester < 4:

        for y in range(tester):
            returnList.append(x)
            n -= values.get(x)

    return roman

"""

"""
online answer 1:
Like i was trying to do it (doesn't quite make sense to me)

def solution(n):
    ROMAN_SYMBOLS = ["M", "D", "C", "L", "X", "V", "I"]
    ROMAN_VALUES = [1000, 500, 100, 50, 10, 5, 1]
    idx = 0
    roman = []
    while n > 0:
        if n < ROMAN_VALUES[idx]:
            idx += 1
            continue
        n -= ROMAN_VALUES[idx]
        roman.append(ROMAN_SYMBOLS[idx])
        if roman[-4:].count(roman[-1]) == 4:
            roman = roman[:-3] + [ROMAN_SYMBOLS[idx-1]]
            if roman[-3:-2] == roman[-1:]:
                roman = roman[:-3] + [ROMAN_SYMBOLS[idx]] + [ROMAN_SYMBOLS[idx-2]]
    return "".join(roman)

"""


"""
online answer 2:
another way (sort of cheating the system)

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

"""



def test(value, solution):
    if value==solution:
        return True
    else:
        return False


if __name__=="__main__":
    groupings=[
    [solution(1), 'I']
    ,[solution(4), 'IV']
    ,[solution(6), 'VI']
    ,[solution(14), 'XIV']
    ,[solution(21), 'XXI']
    ,[solution(89), 'LXXXIX']
    ,[solution(91), 'XCI']
    ,[solution(984), 'CMLXXXIV']
    ,[solution(1000), 'M']
    ,[solution(1889), 'MDCCCLXXXIX']
    ,[solution(1989), 'MCMLXXXIX']
    ]


    for x in groupings:
        if x:
            print(f'Test {x} passed')
        else:
            print(f'Test {x} failed')
