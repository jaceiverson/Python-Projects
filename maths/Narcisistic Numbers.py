#narsisistic numbers
#153 1^3+5^3+3^3=153
#https://www.youtube.com/watch?v=4aMtJ-V26Z4

import matplotlib.pyplot as plt

narNumbers=[]

def success(x):
    print(x, ' this is a narcisistic number')
    if x in narNumbers:
        value=x
    else:
        narNumbers.append(x)
        narNumbers.sort()

def showNarNums():
    print(narNumbers, ' list of found narNumbers')
    maxNum=max(narNumbers)
    plt.axis([0,5,0,maxNum+100])
    plt.plot(narNumbers,'ro')
    plt.ylabel('Naricistic')
    plt.xlabel('Count of NarNum')
    plt.show()
    print('Search again')
    narNums()

def clearList():
    narNumbers=[]
    print('List is now cleared')
    print('search again')
    narNums()

def plotNum(list,list2):
    plt.plot(list)
    plt.plot(list2)
    plt.show()
    print('Return to search')
    narNums()

def fail(x):
    #do nothing
    y=x
def narNums():

    startNum=int(input('starting number'))
    maxNum = int(input('ending number'))
    listNum=[]
    newList=[]

    for x in range(maxNum-startNum+1):
        listNum.append(startNum+x)

    print(listNum, '  Your range')

    for x in range(len(listNum)):

        temp=len(str(listNum[x]))
        number=0

        if temp==1:
            number=listNum[x]
        else:
            value=str(listNum[x])
            for y in range(len(value)):
                number=number+(int(value[y])**temp)

        newList.append(number)

        if listNum[x] == newList[x] and temp>1:
            success(number)

        else:
            fail(number)

    print(listNum, '  Number list')
    print(newList, '  Associated Trial list')

    print('To see found numbers press ''3')
    print('to see a plot of number press 5')
    comeBack=input('Search another range?\n yes=1 no=0')


    if comeBack == 1 or comeBack == '1' or comeBack == 'y' or comeBack == 'Y' or comeBack =='yes':
        narNums()
    elif comeBack==3 or comeBack == '3':
        showNarNums()
    elif comeBack =='9':
        clearList()
    elif comeBack == '5':
        plotNum(listNum,newList)
    else:
        print('Thanks for playing')

narNums()
