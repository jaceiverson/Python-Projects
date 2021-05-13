'''
https://adventofcode.com/
'''

import pandas as pd
import numpy as np
import math
import re
#daily specific functions
from daily_answers.five import row,seat
#for day 6 internet answer
from functools import reduce

def one_a():
    #read file in
    #with open('./files/one_a.txt') as f:
    df=pd.read_csv('./files/one_a.txt',sep=' ',header=None)
    for x in df[0]:
        for y in df[0]:
            if x != y:
                if x+y==2020:
                    return x*y,(x,y)
def one_b():
    df = pd.read_csv('./files/one_a.txt', sep=' ', header=None)
    for x in df[0]:
        for y in df[0]:
            for z in df[0]:
                if x != y and x!= z:
                    if x+y+z==2020:
                        return x*y*z,(x,y,z)

def two_a():
    '''
    Probably a better way to do this one.
    :return:
    '''
    df=pd.read_csv('./files/two_a.txt',sep=' ',header=None)
    df[['min', 'max']] = df[0].str.split('-', expand=True)
    df['letter']=df[1].str.split(':',expand=True)[0]
    #df['letter_c']=df[2],df['letter'].apply(lambda x,y : x.str.count(y))
    df['letter_c']=None
    for index,rows in df.iterrows():
        df['letter_c'][index]=rows[2].count(rows['letter'])
    cond=[(df['letter_c']>=df['min']) & (df['letter_c']<=df['max'])]

    values=['Pass']
    df['good']=np.select(cond,values)

    return df['good'].value_counts()['Pass']
def two_b():
    '''
    Again, I think there is a better way to do it, but it is done.
    :return:
    '''
    df = pd.read_csv('./files/two_a.txt', sep=' ', header=None)
    df['first']=df[0].str.split('-',expand=True)[0].astype(int)
    df['second'] = df[0].str.split('-',expand=True)[1].astype(int)
    df['char'] = df[1].str.split(':',expand=True)[0]
    #df['char_pos']=[pos for pos, char in enumerate(df[2]) if char == df['char']]
    df['first_match']=None
    df['second_match']=None

    for index,rows in df.iterrows():
        df['first_match'][index]=rows[2][rows['first']-1]==rows['char']
        df['second_match'][index]= rows[2][rows['second'] - 1] == rows['char']

    cond= [(df['first_match'] != df['second_match'])]
    value=['Pass']
    df['good']=np.select(cond,value)

    return df['good'].value_counts()['Pass']

def three_a(right_steps=3,down_steps=1):
    with open('./files/three_a.txt', 'r') as f:
        route = f.read()
    route=route.split('\n')
    tree_count=0
    altitude=0
    right_count=0

    for y in range(0,len(route),down_steps):
        if route[y]=='':
            break
        else:
            #we need to go 3 times as far right as we do down
            slope=route[y]*(math.ceil(len(route)/len(route[y])))*right_steps

            if slope[right_count] == '#':
                tree_count+=1

            right_count+=right_steps

    print("Right: ", right_steps, " Down: ", down_steps)
    print(tree_count)
    return tree_count
def three_b():
    one=(1,1)
    two=(3,1)
    three=(5,1)
    four=(7,1)
    five=(1,2)

    tests=[one,two,three,four,five]
    results=[]
    for x in tests:
        results.append(three_a(x[0],x[1]))

    return np.product(np.array(results))

def four_a():
    with open('./files/four_a.txt', 'r') as f:
        passports = f.read()

    passports=passports.replace('\n',' ').split('  ')
    df=pd.DataFrame(columns=['iyr', 'hgt', 'byr', 'cid', 'pid', 'eyr', 'hcl', 'ecl'])
    req=['iyr', 'hgt', 'byr', 'pid', 'eyr', 'hcl', 'ecl']
    #clean indivdual
    for x in passports:
        temp=pd.DataFrame(x.split(' '))
        temp=temp[0].str.split(':',expand=True).T
        temp.columns=temp.iloc[0]
        temp=temp.drop(0)

        df=df.append(temp)

    #want to know all non NA values for the req columns
    return df[req].dropna()
def four_b():
    #requirements
    byr_min=1920
    byr_max=2002
    iyr_min=2010
    iyr_max=2020
    eyr_min=2020
    eyr_max=2030
    h_cm_max=193
    h_cm_min=150
    h_in_max=76
    h_in_min=59
    #color have '#' followed by 6 valid digits
    #re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)
    e_color_list=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    #p_num=re.search(r'\d{0,9}',str)

    df=four_a()
    df[['byr','iyr','eyr']]=df[['byr','iyr','eyr']].astype(int)

    df=df.loc[(df['byr']>=byr_min) & (df['byr']<=byr_max)]
    df=df.loc[(df['iyr']>=iyr_min) & (df['iyr']<=iyr_max)]
    df=df.loc[(df['eyr']>=eyr_min) & (df['eyr']<=eyr_max)]
    cm=df.loc[df['hgt'].str.contains('cm')]
    inch=df.loc[df['hgt'].str.contains('in')]
    cm=cm.loc[(cm['hgt'].str.split('c',expand=True)[0].astype(int)>=h_cm_min)&
              (cm['hgt'].str.split('c',expand=True)[0].astype(int)<=h_cm_max)]
    inch = inch.loc[(inch['hgt'].str.split('i', expand=True)[0].astype(int) >= h_in_min) &
                (inch['hgt'].str.split('i', expand=True)[0].astype(int) <= h_in_max)]
    df=cm.append(inch)
    df['color_valid']=df['hcl'].apply(lambda x: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x))
    df=df.dropna(subset=['color_valid'])

    df=df.loc[df['ecl'].isin(e_color_list)]

    #pid
    df=df.loc[df['pid'].str.len()==9]
    df['pid_valid']=df['pid'].apply(lambda x: re.search(r'^\d{0,9}$',x))
    df=df.dropna(subset=['pid_valid'])

    return df

def five_a():
    with open('./files/five_a.txt') as f:
        tickets=f.read()
    tickets=tickets.split('\n')
    row_num=[]
    seat_num=[]
    for x in tickets:
        if x != '':
            row_list=x[:7]
            seat_list=x[7:]

            row_num.append(row(row_list,127,0))
            seat_num.append(seat(seat_list,7,0))

    df=pd.DataFrame([tickets,row_num,seat_num])
    df=df.T
    df=df.dropna()
    df.columns=['Ticket','row_num','seat_num']
    df['id']=(df['row_num']*8)+df['seat_num']
    #to solve the problem
    #return df['id'].max()
    #for help on five_b
    return df
def five_b():
    df=five_a()
    range_ids=np.arange(df['id'].min(), df['id'].max(), 1)
    for x in range_ids:
        if x not in df['id'].values:
            return x

def six_a():
    with open('./files/six_a.txt') as f:
        answers=f.read()
    #separates groups
    answers=answers.split('\n\n')

    unique_answers=0
    for x in answers:
        temp=[]

        for y in x.replace('\n',''):
            temp.append(y)

        temp=pd.Series(temp)
        unique_answers += len(temp.unique())

    return unique_answers
#TODO
def six_b():
    #NOT 3461, to low
    with open('./files/six_a.txt') as f:
        answers = f.read()
    # separates groups
    answers = answers.split('\n\n')

    answer_count=0
    for x in answers:

        common_answer=True
        new_list=x.split('\n')

        y=new_list[0]
        for z in y:
            for i in new_list:

                if z in i:
                    common_answer=True
                else:
                    common_answer=False
                    break

            if common_answer:
                answer_count+=1

    return answer_count
#TODO
def seven_a():
    with open('./files/seven_a.txt') as f:
        rules = f.read()

    bag='shiny gold'
    r=rules.split(' bags contain ')

    df = pd.read_csv('./files/seven_a.txt', sep=' bags contain ',header=None)
    new_cols=df[1].str.split(', ',expand=True)
    new_cols.columns=new_cols.columns+1
    new_cols['main']=df[0]
    df=[['main',1,2,3,4]]

    for x in new_cols.columns[[1,2,3,4]]:
        temp=df[df[x].str.contains(bag)]['main'].values


    r.index()
#TODO
def seven_b():
    pass

def eight_a():
    df=pd.read_csv('./files/eight_a.txt',sep=' ',header=None)
    df['order']=None
    return eight_loop(df=df)

def eight_b():
    df=pd.read_csv('./files/eight_a.txt',sep=' ',header=None)
    df['order']=None
    return eight_loop(df,day2=True)

def eight_loop(df,current_rule=0,step=0,acc=0,day2=False):
    last_step=len(df)-1
    running=True
    while running:
        step += 1
        if current_rule == last_step:
            return "WE OUT"

        line = df.iloc[current_rule]
        if not day2:
            if line['order']:
                running = False
                break
        df.loc[current_rule, 'order'] = step
        action = line[0]
        if action == 'acc':
            acc += df.iloc[current_rule][1]
            # increment
            current_rule += 1
        elif action == 'nop':
            # increment
            current_rule += 1
        elif action == 'jmp':
            #check if change will end loop
            if day2:
                if eight_loop(df.copy(),current_rule+1,step=step,acc=acc) == "WE OUT":
                    return current_rule
            current_rule += (df.iloc[current_rule][1])

    return df,acc

if __name__ =='__main__':
    print(eight_b())
    df=pd.read_csv('./files/eight_a.txt',sep=' ',header=None)
    df['order']=None
    df.loc[265,0]='nop'
    test=eight_loop(df)
    print(test)
    '''
    online 2 this one worked
    # create an array of arrays splitting up the groups and answers per group
    groups = [line.split("\n") for line in [group.strip() for group in open("./files/six_a.txt").read().split("\n\n")]]
    # PART 2
    # output: tally of questions answered by everyone in the group
    sumCompleteAnswers = 0
    # check if an answer appears same # of times as people in group
    for group in groups:
        joined = ''.join(group)  # flat string, unsplit by person
        people = len(group)  # number of people in group
        answers = set(joined)  # the questions this group answered, no duplicates
        for c in answers:
            if len(re.findall(c, joined)) == people:
                sumCompleteAnswers += 1

    print(sumCompleteAnswers)
    '''
