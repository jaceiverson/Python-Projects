#https://www.codewars.com/kata/57b06f90e298a7b53d000a86

import pprint
import json

def queue_time(customers, n):
    queues=[]
    cashierCustCount={}
    customerCounter=0
    customerInfo={}
    #makes my queue list the length of how many cashiers (n) i have avalible
    for x in range(n):
        queues.append(0)
        cashierCustCount[x+1]=0

    for i in range(len(customers)):
        index = queues.index(min(queues))
        customerCounter+=1

        customerInfo=feedCustAPI(i,customerInfo,customers,queues,index)
        queues[index]+=customers[i]
        cashierCustCount[index+1]+=1

    cashierInfo=cashierFile(cashierCustCount,queues, customerInfo)
    final=combineFiles(cashierInfo,customerInfo)
    pprintAPI(final)
    printToText(final)
    return max(queues)

def combineFiles(f1, f2):
    file={"Cashier Info": f1, "Customer Info": f2}
    return file

def cashierFile(custCount, time, custInfo):
    cashierFile={}

    for z in custCount:
        cashierFile[z]={"Cashier": z, "helped":{"Count":custCount.get(z), "Customers":[]}, "total work time": time[z - 1]}


        for y in custInfo:
            if custInfo[y]['queue visited']==cashierFile[z]["Cashier"]:
                cashierFile[z]['helped']['Customers'].append(y)

    return cashierFile

def pprintAPI(file):
    pprint.pprint(file)

def printToText(file):
    fileName=input("What do you want to name your file? ")
    file=json.dumps(file)
    with open(f'{fileName}.json','a') as f:
        f.write(file)

def feedCustAPI(x,customerInfo,customers,queues, index):
    customerInfo[x + 1] = {'length of checkout': customers[x], 'wait time': queues[index], 'queue visited': index+1}
    return customerInfo

if __name__=="__main__":
    #fill with any information that you have
    cust=[1,2,3,1,7,5,6,7,8,4,1,2,3,4,5,6,5,4,7,6,5,4,3,2,1,3,4,6]
    n=8
    print(f'{queue_time(cust, n)} is the time it would take {len(cust)} customers with {n} cashiers')
