"""
There are 25 mechanical horses and a single racetrack. 
Each horse completes the track in a pre-programmed time, 
and the horses all have different finishing times, unknown to you. 
You can race 5 horses at a time. After a race is over, you get 
a printout with the order the horses finished, but not the 
finishing times of the horses. 

What is the minimum number of races you need to identify the fastest 3 horses?

The solution is included on line 100 here, don't read further if you'd like to figure it out on your own.

If you want a good description, MindYourDecisions on YouTube has a good video
https://www.youtube.com/watch?v=i-xqRDwpilM

"""

import random

class Horse():
  def __init__(self, num:int, t:float):
    self.number = num
    self.time = t
    self.heat_num = None
    self.heat_pos = None
    self.overall_pos = None

  def set_heat(self, heat:int):
    self.heat_num = heat

  def show_stats(self, hide_time:bool = True) -> None :
    if hide_time:
      print(f"Number: {self.number} | Heat: {self.heat_num} | Heat Pos: {self.heat_pos} | Overall Position: {self.overall_pos}")
    else:
      print(f"Number: {self.number} | Heat: {self.heat_num} | Heat Pos: {self.heat_pos} | Overall Position: {self.overall_pos} | Time: {self.time}")

def race_horses(horse_list:list, heat:str = None) -> List:
  if heat is not None:
    # assign heat number
    [x.set_heat(heat) for x in horse_list]
  # "race" the horses
  horse_list.sort(key=lambda x: x.time, reverse=False)

  return horse_list

def heat_one(horse_list:list) -> List:
  place = 0
  for horse in horse_list:
    place+=1
    horse.heat_pos = place

  return horse_list

# get 25 random times between 20 and 22
horse_times = [random.uniform(20,22) for x in range(25)]
# create Horse objects and assign those times
horses = [Horse(x,horse_times[x]) for x in range(25)]

# race all 25 in groups of 5 (5 races)
for race in range(0,len(horses)-1,5):
  horses[race:race+5] = heat_one(race_horses(horses[race:race+5],heat=(race//5)+1))

# here are the 1st place finishers
heat1_first_place_horses = [x for x in horses if x.heat_pos ==1]

# 6th race - the first place horses
first_place_race_results = race_horses(heat1_first_place_horses)

# we have our champion
first_place_race_results[0].overall_pos = 1

# winning horse needs 2nd and 3rd from their heat
group1 = [horse for horse in horses if horse.heat_num == winning_horse.heat_num and horse.heat_pos in (2,3)]
# 2nd place needs 2nd from their heat as well themselves
group2 = [horse for horse in horses if horse.heat_num == first_place_race_results[1].heat_num and horse.heat_pos in (1,2)]
# 3rd place races again
group3 = [first_place_race_results[2]]

# 7th and final race
final_race_results = race_horses(group1+group2+group3)

# assign the final positions
final_race_results[0].overall_pos = 2
final_race_results[1].overall_pos = 3 

# top 3
top3 = [x for x in horses if x.overall_pos is not None]
top3.sort(key=lambda x: x.overall_pos, reverse=False)
# output results
print("--TOP 3--")
[x.show_stats(hide_time=False) for x in top3]

# how easy it is if we can use the time 
horses.sort(key=lambda x: x.time, reverse=False)
# print all values
print("--ALL HORSES--")
print([x.show_stats(hide_time=False) for x in horses])
 
'''
SOLUTION Description

7 races

HEATs 1-5
+5 -> 5 races for all 25 to race once

CHAMPIONSHIP HEAT = CH
+1 -> All First Place Horses Race

Horses that race in this heat are now titled CH then their respective position
Example: CH-1 is the first place horse from this heat

__Results__
CH-1 = Fastest of the 25
Ch-2
 - still in contention, but must race again
 - Horses 3-5 from CH-2's first heat are eliminated
CH-3 
 - still in contention, but must race again
 - Horses 2-5 from CH-3's first heat are eliminated
CH-4 & CH-5
 - out of contention 
 - All horses from CH-4 and CH-5's first heats are eliminated
 
We now have eliminated 19 Horses and identified the fastest one
This gives us 5 horses to still race

CONFIRMATION/FINAL HEAT
+1 -> CH-2, CH-3, CH-2's Heat 1 2nd, CH-2's Heat 1 3rd, CH-3's Heat 1 2nd

__Results__
1st place = 2nd fastest horse
2nd place = 3rd fastest horse

'''
