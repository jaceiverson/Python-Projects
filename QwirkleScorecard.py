import pandas as pd
import datetime as dt

def gatherPlayers():
    players=int(input("How many players?"))

    scorecard=pd.DataFrame()

    for x in range(players):
        tempPlay=input("Player "+str(x+1)+":")
        scorecard[tempPlay]=''
        scorecard[tempPlay+'_Qwirkles']=''

    return scorecard

def updateDF(turn,row,df):
    df.loc[turn]=row
    return df

def playGame(scorecard):
    firstPlayer=scorecard.columns[0]
    print('Looks like ',firstPlayer,' is going first. 6 bonus points.\nDon\'t worry, I\'ll add those in for you')
    winner=False
    turn = 0
    
    while winner==False:
        turnRow=[]
        #initiate the turn
        for x in scorecard.columns:
            if 'Quarkle' in x:
                badRow=True
            else:
                badRow=False
                qScore=0
                
                roundScore=int(input(x+'\'s Score for Round '+str(turn+1)+':'))
                #
                if roundScore>=12:
                    quarkle=input('Did they score a QWIRKLE?')
                else:
                    quarkle='n'
                
                #give the bonus points for going first
                if turn==0 and x==scorecard.columns[0]:
                    roundScore+=6
                    
                if quarkle.lower() in ('1','y','yes','yeah','fo sho'):
                    qScore=1
                elif quarkle=='be done':
                    break
                #update the master turn row with the players score
                turnRow+=[roundScore,qScore]

                #check to see if they won only after 10 turns
                if turn>=10:
                    didWin=input('Did you win on this turn? ')
                    if didWin.lower() in ('1','y','yes','yeah','fo sho'):
                        #if they won, give them 6 bonus points, update the scorecard for the last time, and lets get out of here
                        roundScore+=6
                        scorecard=updateDF(turn,turnRow,scorecard)
                        winner=True

        scorecard=updateDF(turn,turnRow,scorecard)
        
        printScore(scorecard,turn)
        turn+=1

    return scorecard

def printScore(df,turn):
    
    print(df[df.columns[::2]].sum())
    
if __name__=='__main__':
    startTime=dt.datetime.today()
    print('Welcome to Jace\'s Qwirkle scorecard!')
    df=gatherPlayers()
    print('Starting the game at '+ startTime.strftime("%b %d %Y %H:%M:%S"))
    playGame(df)
    endTime=dt.datetime.today()
    gameLen=endTime-startTime
    print('Game is over after ' + str(gameLen))
    print('Saving the scorecard in the normal location')
    path='/Users/jaceiverson/Documents/Tech Stuff/GameNight/Qwirkle Scores/'
    fileName=str(int(len(df.columns)/2))+' player game started at ' + startTime.strftime("%b %d %Y %H:%M:%S")+'.csv'
    df.to_csv(path+fileName,index=True)
    
