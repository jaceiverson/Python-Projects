#am+bm+cm=num
#the famous nugget problem, find the max number of nuggets you cannot buy

def isNugNum(num):
    for x in range(num):
        for y in range(num):
            for z in range(num):
                if num==(a*x)+(b*y)+(c*z):
                    return True
                else:
                    pass
    return False

def getNums():
    a = int(input("first value: "))
    b = int(input("second value: "))
    c = int(input("third value: "))
    return a,b,c

def printOut(high,list):
    #print your output with the highest number
    print(f'The highest number of nuggets that you can\'t buy is {high}.\n'
          f'Now go ask the worker at McDonald\'s for {high} nuggets and see what they do')

    #print your output as a list
    print(f'Here is a list of nuggets you cannot buy {list}.')
if __name__=='__main__':

    consecutive = 0
    num = 1
    max = 0
    a,b,c=getNums()
    noBuy=[]

    while consecutive < 6:
        #now you need to check if you can get that many nugs
        if isNugNum(num):
            #if it is a nugNum(a number you can order with parameters a,b,c) it will add a point to consecutive
            #because when you hit 6 in a row, you can order everything else after that
            consecutive += 1
        else:
            #resets the consecutive to 0 because we found a number we can't order
            consecutive = 0

            #you can either store the numbers in a list
            noBuy.append(num)
            #or just store the highest number
            max = num
        #you will then need to increment your counter
        num += 1

    printOut(max,noBuy)
