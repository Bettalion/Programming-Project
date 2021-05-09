import time
import random
from tkinter import *
from PlayersGUI import *


## must add all players
#initial players
amogh=player('Amogh','1')
simha=player('Simha','2')
tester=player('Tester','3')
#players
Players = {
    amogh.name:amogh,
    simha.name:simha,
    tester.name:tester
    }


def verify(Players): # user input verification
    user1 = input('What is your name? (p1)').capitalize()
    user2 = input('What is your name? (p2)').capitalize()
    try:
        p1 = Players[user1]
        p2 = Players[user2]
    except:
        print('Unouthorised Name(s)')
        time.sleep(2)
        if input('Do you want to try again?(Y/N)').upper() in ['Y','YES']:
         verify(Players)
        else:
            quit()
    user1 = input('What is your pasword ({})?'.format(p1.name).capitalize())
    if user1 != p1.passw:
        print('Incorrect Pasword')
        time.sleep(2)
        if input('Do you want to try again?(Y/N)').upper() in ['Y','YES']:
         verify(Players)
        else:
            quit()
    user2 = input('What is your pasword ({})?'.format(p2.name).capitalize())
    if user2 != p2.passw:
        print('Incorrect Pasword')
        time.sleep(2)
        if input('Do you want to try again?(Y/N)').upper() in ['Y','YES']:
         verify(Players)
        else:
            quit()
    return [p1,p2]

def setdeck(): # creates a deck of cards
    adeck=[]
    for x in range(1,10): #####10
     adeck.append('0'+str(x)+"R")
     adeck.append('0'+str(x)+"Y")
     adeck.append('0'+str(x)+"B")
    adeck.append("10R")
    adeck.append("10Y")
    adeck.append("10B")
    return adeck
def randomise(deck): # randomises the deck of cards
    #print(deck)
    while len(deck)!=0:
        index = random.randint(0,len(deck)-1)
        yield deck[index]
        deck.remove(deck[index])

def interpretC(cardID): ## gives the details of a specified card
    col=(cardID[2:])
    if col == 'B':
        setcol='light blue' # the colour for GUI colouring
    if col == 'Y':
        setcol='yellow'
    if col == 'R':
        setcol='red'
    num = cardID[:2]
    return [cardID,num,col,setcol]

def instructions(): # displays the instructions if required
    print('''When it is your turn, press any key to draw a card.
When your turn is over,it immediately goes to the next player.
The winner of the round will then be displayed.
Repeat this untill the final scores have been released.
Have fun playing The Card Game\n''')
def play(p1,p2,inou):
     if input('Would you like the instructions?(Y/N)').lower() in ['y','yes']:
         instructions()
     # v counter for number of rounds won v 
     p1w=0
     p2w=0
    #  p1cards=[]
    #  p2cards=[]
     while len(p1.deck)!=0 or len(p2.deck)!=0:
##      print(len(p1.deck),len(p2.deck)
      if inou == 1: # for GUI
            app=GUI(Tk())
            p1card = p1.deck[0] # retrieve card
            p1.deck.remove(p1.deck[0]) # remove card from deck
            interpreted=interpretC(p1card) # get the details of the card
            app.create_win(p1,interpreted) # GUI
            app.destroywin()  # remove GUI window
            
            app=GUI(Tk())
            p2card = p2.deck[0] # retrieve card
            p2.deck.remove(p2.deck[0]) # remove card from deck
            interpreted=interpretC(p2card) # get the details of the card
            app.create_win(p2,interpreted) # GUI
            app.destroywin() # remove GUI window

      else:   # for console
            p1card = p1.deck[0] # retrieve card
            p1.deck.remove(p1.deck[0]) # remove card from deck
            cardID,num,_,setcol=interpretC(p1card) # get the details of the card
            # v Display the card info v
            print('{}, your Card is:\n number:{} and colour:{}\n ({})'.format(p1.name,num,setcol.capitalize(),cardID))
            time.sleep(1.5) # delay

            p2card = p2.deck[0] # retrieve card
            p2.deck.remove(p2.deck[0]) # remove card from deck
            cardID,num,_,setcol=interpretC(p2card) # get the details of the card
            # v Display the card info v
            print('{}, your Card is:\n number:{} and colour:{}\n ({})'.format(p2.name,num,setcol.capitalize(),cardID))
            time.sleep(1.5) # delay

      p1.temp,p2.temp=(p1card,p2card) # assign to each player
      winner,winn=mechanics(p1,p2)    # work out the winner of the round and their cards
      if winn == 1:
          p1w+=1 
          # assign the cards of the round to the winner
          p1.wincards.append(p1.temp)
          p1.wincards.append(p2.temp)
      else:
          p2w+=1
          # assign the cards of the round to the winner
          p2.wincards.append(p1.temp)
          p2.wincards.append(p2.temp)
      if inou == 2:time.sleep(1.75)

      
     return [p1w,p2w] # returns the total round wins

def mechanics(p1,p2):  # works out the winner of the round
    #print(p1.temp,p2.temp)
    # get the players colours
    p1Col = p1.temp[2:]
    p2Col = p2.temp[2:]
    p1Num = p1.temp[:2]
    p2Num = p2.temp[:2]

    #Num theory
    if p1Col == p2Col:
      if p1Num > p2Num:
       print(f'\nPlayer 1 ({p1.name}) wins both cards\n')
       rwinner =  p1			
      if p1Num < p2Num:
       print(f'\nPlayer 2 ({p2.name}) wins both cards\n')
       rwinner = p2
       
    #Color theory
    else:
        if p1Col=='R' and p2Col=='B':
           print(f'\nPlayer 1 ({p1.name}) wins both cards\n')
           rwinner = p1
        elif p1Col=='Y' and p2Col=='R':
           print(f'\nPlayer 1 ({p1.name}) wins both cards\n')
           rwinner = p1
        elif p1Col=='B' and p2Col=='Y':
           print(f'\nPlayer 1 ({p1.name}) wins both cards\n')
           rwinner = p1
        else:
          print(f'\nPlayer 2 ({p2.name}) wins both cards\n')
          rwinner = p2
    if rwinner == p1:
        rwinner = [rwinner,1]
    else:
        rwinner = [rwinner,2]
    return rwinner # winner object, player no.

def top5(): # display top 5 scores
    print(f'\nTop 5 Results:\n')
    f = open('WINNERS.txt','r')
    content = f.read()
    # sort all of the scores - cannot just use the sort function as the entry is not just a number 
    # must improve efficency
    SCOREs = []
    scores = content.split(';')
    scna={}
    for thing in scores:
        try:
            na,sc = thing.split(':')
            SCOREs.append(int(sc))
        except:
            pass
        scna[sc]=na
    SCOREs.sort(reverse=True)
    t5 =[]
    c=0
    for goal in SCOREs:
        if c>4:
            break
        else:
            c+=1
        try:
            sen= f'{scna[str(goal)]} got a score of: {goal}'
            print(sen)
            t5.append(sen)
        except:
            pass
    GUI(Tk()).displaytop5(t5)

    
    
def main(Players):
    print('\n\nWelcome to The Card Game!')
    # verify Players
    p1,p2= verify(Players)
    # p1= Players['Amogh']
    # p2= Players['Tester']
    inou=1 # method of input/output 
    if int(input('Would you like to:\n1) Use the GUI\n2) Use the console\n')) == 2:
     inou=2
    # make deck + set to players
    deck = list(randomise(setdeck()))
    time.sleep(1)
    print('Making deck')
    setattr(p1,'deck',deck[:len(deck)//2])
    setattr(p2,'deck',deck[len(deck)//2:])
    time.sleep(1)
    print('Assign deck')
    #print(p2.deck)
    time.sleep(1)
    print('Play\n') # start Game
    result = p1w,p2w = play(p1,p2,inou) # results
    
    #print(p1w,p2w, p1.wincards,p2.wincards)
    if len(p1.wincards)> len(p2.wincards): #work out the winner
        winner = p1
    else:
        winner = p2
    #     Add the results to the winner file
    try:
        f = open('WINNERS.txt','a')        
    except:
        f = open('WINNERS.txt','w')
    f.write(f'{winner.name}:{len(winner.wincards)};')   # name, total card number
    f.close()

    # display the results
    r= 2
    if inou==1:  # GUI
        win = Tk()
        win.title(f'Well done {winner.name}')
        Label(win,text = (f'Well done {winner.name}, you won The Card Game!')).grid(row=0,column=0)
        Label(win,text= f'\nYour score is {len(winner.wincards)}\n Your cards include:').grid(row=1,column=0)
        
        for card in winner.wincards:
            Label(win,text=card).grid(row=r,column=0)
            r+=1
        win.mainloop()
    else: # console
        print(f'Well done {winner.name}, you won The Card Game!\nYour score is {len(winner.wincards)} and you cards include:')
        for card in winner.wincards:
            print(card)
            time.sleep(0.25)
            r+=1
    top5()
    input()
    

main(Players)
