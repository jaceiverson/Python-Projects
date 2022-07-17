from decimal import *
import math


def continuedFractions():
    print("Calculate Continued Fractions")
    print("What continued fraction would you like to calculate?: \n")
    print("1:Rational Fractions")
    print("2:Irrational Numbers")
    print("3: Decimal Numbers")
    print("4:Solar Year") 
    print("anything else will draw an error")
    answer=int(input("Pick your category: "))
   
    if answer==1:
        rationalFrac()
    elif answer==2:
        irrationalFrac()
    elif answer==3:
        decimalValue()
    elif answer ==4:
        solarYear()
    else:
        print("Wrong Choice")
        exit()
               
def truncate(x):
    num1 = int(x*10000000)/10000000
    return num1

def rationalFrac():
    num=int(input("Numerator: "))
    den=int(input("Denominator: "))
    calC(num,den)

def irrationalFrac():
    print("what would you like?")
    print("(please select the number)")
    print("1: pi")
    print("2: square root of _ ")
    print("3: e")
    print("4: Golden Ratio")
    print("thats all we have;")
    answer=input("Selection: ")

    if type(answer)==str and answer!='e':
        answer=int(answer)

    if answer==1:
        num=math.pi
        den=1
        
    elif answer==2:
        sqroot=decimal.Decimal(input("square root of what number?: "))
        num=math.sqrt(sqroot)
        den=1
        print(num)
        
    elif answer==3 or answer=='e':
        num=math.e
        den=1
        
    elif answer == 4:
        num=(1 + 5 ** 0.5) / 2
        den=1
    else:
        print("wrong")
        exit()

    calC(num,den)
    
def decimalValue():
    num=float(input("Value: "))
    den=1

    calC(num,den)
    
def solarYear():
    num=365.2425
    print("there are ", num, " days in a Gregorian Calandar year!")
    den=1
    calC(num,den)

def printConFrac(confrac):
    print("Size of continued fraction: ",len(confrac))

    answer = input("Do you want to print? (put in Y or N)")

    if answer =='Y' or answer =='y':
        print(confrac)
    else:
        print("End")
        
    for x in confrac:
        if confrac.index(x)<len(confrac)-1 or len(confrac)>35:
            print(x, ' + 1 divide by')
        else:
            print(x, '\nend')
        
def calC(num,den):
    lefts=[]
    count=0
    num=Decimal(num)
    den=Decimal(den)
    
    while True:

        count=count+1
        if count>35:
            print('fraction has reached 35+ partial quotients: you probably have an irrational number')
            break
             
        if num>den:
            leftNum=num//den
            lefts.append(int(leftNum))
            num=num%den
            if num==0:
                break
            
        elif num>1:
            leftNum=int(1/(num/den))
            lefts.append(int(leftNum))
            num=(1/(num/den))-leftNum
            
        else:     
            if (truncate(1/num)).is_integer():
                num=1/num
                lefts.append(int(num))
                break
            else:
                leftNum=int(1/num)
                lefts.append(int(leftNum))
                num=1/num-(leftNum)
                if num==0:
                    print('num0break')
                    break

    printConFrac(lefts)

    retry=input("would you like to try again?: ")
    if retry=='y' or retry=='Y':
        continuedFractions()
    else:
        exit()

                
continuedFractions()

    
