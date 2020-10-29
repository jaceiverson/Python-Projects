#25 horses
import numpy as np
horses=np.random.uniform(size=25)
raceCount=0
fastest=[]

#find the fastest 3 running 5 distinct heats with each of the 25 horses in one heat
for x in range(0,len(horses)-1,5):
    print(np.sort(horses[x:x+5])[::-1][:3])
'''
9 races:
+5 5 races for all 25 to race once
+1 3rd place race (all 3rd place from first heats) you only keep winner (because it is only possible to have 1 thrid place be fastest 3)
+1 2nd place race (all 2nd place from first heats) you only keep winner (dito for second place)
+1 1st place race
+1 1st place winners race the 2nd and 3rd place winners

9 total? 
'''

'''
+1 5 keep top 2 note 3rd


'''
