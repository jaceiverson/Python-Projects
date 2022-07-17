#https://www.youtube.com/watch?v=uQdy914JRKQ
import random

def googleToo(list=[]):
    if len(list)==0:
        array=[]
        for i in range (4):
            array.append(random.randrange(1,10,1))
    else:
        array=list

    print("original ", array)

    value=len(array)
    if value==1:
        if array[0]==9:
            array=[1,0]
            
        else:
            array[0]=array[0]+1
    else:       
        for i in range(value):
            j=i+1
            if array[value-j]>=9:
                array[value-j]=0
                array[value-j-1]=array[value-j-1]+1
            

            else:
                array[value-j]=array[value-j]+1
                break
            
            
            if array[0]==10:
                newArray=[1]
                for k in range(value):
                    newArray.append(0)
                array=newArray
                break

    print("new ", array)
