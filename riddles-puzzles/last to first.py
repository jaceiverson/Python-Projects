#https://www.youtube.com/watch?v=1lHDCAIsyb8&

def flipNumber(num):
    if len(num)==1:
        return num
    else:
        value=num.pop()
        num.insert(0,value)
        return num


#answer is 105263157894736842
if __name__ == "__main__":
    """
    I made the logic using numbers 1-100, then after I found the solution
    I put in the numbers to run faster
    """
    for x in range(105263157894736000,105263157894737000):

        num=[int(i) for i in str(x)]

        value=flipNumber(num)

        value=int("".join(str(e) for e in value))

        if value==0:
            pass
        elif value==x*2:
            print(f'You have found the answer. {x} \nwhen flast becomes first is double: {value}')
            break


    print(f'end')
