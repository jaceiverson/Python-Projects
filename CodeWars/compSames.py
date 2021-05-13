import numpy as np

def comp(a1, a2):
    import math as m


    for x in a2:
        if m.sqrt(x) not in a1:
            print(f'a2 false because {m.sqrt(x)} isn\'t in a1')
            return False
    for x in a1:
        if x * x not in a2:
            print(f'false because {x}*{x} not in a2')
            return False

    return True

a1=np.array([1,2,3,4,5,6])
b=a1+3

print(comp(a1,b))