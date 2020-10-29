#https://www.youtube.com/watch?v=XKu_SEDAykw

import random

def winnerFunc(low, li, high, hi, sn):
    print("Sum was: ", sn, ". We got there by adding: ", low, " + ", high, " at positions: ", li, " & ", hi, " respectively.")

goalNum=random.randrange(100,200)

rr=[]
for i in range (20):
    rr.append(random.randrange(1,101,1))

rr.sort()
print ("Find 2 numbers with sum: ", goalNum, "\n", rr)

low=0
high=len(rr)-1
count=0

while rr[low]<rr[high]:
    if rr[low]>rr[high]:
        print(rr[low], ">", rr[high], " unsuccessfull")
        break
    sumNum=rr[low]+rr[high]
    print(rr[low]," and ", rr[high], " = ", sumNum)
    if sumNum==goalNum:
        print("winner winner")
        winnerFunc(rr[low],low,rr[high], high, sumNum)
        break
    elif sumNum<goalNum:
        low=low+1
    elif sumNum>goalNum:
        high=high-1
    else:
        print("broke")
    
    print("end of while")
                   
print(low, " ", high)
