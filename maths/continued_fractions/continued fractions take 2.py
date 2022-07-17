num=int(input("Numerator: "))
den=int(input("Denominator: "))
lefts=[]
while num%den != 0:
    
    if num>den:
        leftNum=num//den
        lefts.append(leftNum)
        num=num%den
    
    elif num>1:
        leftNum=int(1/(num/den))
        lefts.append(leftNum)
        num=(1/(num/den))-leftNum
        
    else:
        if (1/num).is_integer():
            break
        else:
            leftNum=int(1/num)
            lefts.append(leftNum)
            num=1/num-(leftNum)

print("Size of continued fraction: ",len(lefts))

answer = input("Do you want to print? (put in Y or N)")

if answer =='Y' or answer =='y':
    print(lefts)
else:
    print("End")

for x in lefts:
    if lefts.index(x)<len(lefts)-1:
        print(x, ' + 1 divide by')
    else:
        print(x, 'end')
    
print("This should be the end")
