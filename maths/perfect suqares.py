#different ways to find perfect squares
def fromOdds(value):
    counter=2
    Odds=[1]
    temp2=[1]
    for x in range(value-1):
        temp=Odds[x]+counter
        Odds.append(temp)
        temp3=sum(Odds)
        temp2.append(temp3)

    return temp2

def oddNumbers(value):
    counter=2
    listOdds=[1]
    for x in range(value-1):
        temp=listOdds[x]+counter
        listOdds.append(temp)
    return listOdds

value=int(input('enter the number of perfect squares you want to see: '))
perfectSquare = []
perfectAddition = []
temp =0


oddNumbers=oddNumbers(value)
calcOdds=fromOdds(value)

for x in range(value):
	perfectSquare.append((x+1)*(x+1))

for	x in range(value):
	counter=oddNumbers[x]
	perfectAddition.append(counter+temp)
	temp=counter+temp
	
	

print(perfectSquare)
print(perfectAddition)
print(calcOdds)
