import random
import time

#account / password 
autorise={
	'amogh':1,
	'b':2,
	'c':3
}

#verifys person
def verify(p,autorise,name):					   
 print('\nWelcome, "'+name+'" you are player',p)
 if name in autorise:
  if int(input('Enter your password:'))==autorise[name]:
   print("Autorised entry")
   return True 
  else:
   print("Incorrect password")
 else:
  print('Unouthorised name')
 return False
 
def as_deck():		# creates full deck
 adeck=[]
 deck=[]
 for x in range(1,11):
  
  adeck.append(str(x)+"R")
  adeck.append(str(x)+"Y")
  adeck.append(str(x)+"B")
 
 
 for a in adeck:	#.   ensures all ellements are same. lleenth (so can access colour)
  #print(len(a))
  if len(a)==2:
   deck.append('0'+a)
  elif len(a)==3:
   deck.append(a)
  else:
   print('error')
  
 #print(len(deck))
# print(deck)
 return deck
  
def gen():			#shuffles deck
	deck=as_deck()
	position=[]
	for x in range(30):
	 position.append(x)
	 
	for i in range(1,31):
		pos=random.choice(position)
		yield deck[pos]
		position.remove(pos)
		
def mechanics(p1T,p2T):
 p1Num=p1T[:2]	  #player 1 number
 p1Col=p1T[2]	   #player 1 col
 # print(p1T,p1Num,p1Col)
 p2Num=p2T[:2]	  #player 1 number
 p2Col=p2T[2]	   #player 1 col
 # print(p2T,p2Num,p2Col)
 
 #number theory
 if p1Col == p2Col:
  if p1Num > p2Num:
   print('\nplayer 1 wins both cards')
   return 1 #.			returns winner of round
  if p1Num < p2Num:
   print('\nplayer 2 wins both cards')
   return 2
   
   #colour theory
 else:
  if p1Col=='R' and p2Col=='B':
   print('\nplayer 1 wins both cards\n')
   return 1
  elif p1Col=='Y' and p2Col=='R':
   print('\nplayer 1 wins both cards\n')
   return 1
  elif p1Col=='B' and p2Col=='Y':
   print('\nplayer 1 wins both cards\n')
   return 1
  else:
   print('\nplayer 2 wins both cards\n')
   return 2
 
def dots(ending=0,timer=0.12,count=2):
 for x in range(count):
  time.sleep(timer)
  print('.',end='')
  time.sleep(timer)
  timer/=2
 if ending==1:
  print('\n')
 else:
  print(' ')

def instructions(known=True):
 if known==False:
  instructions='''
  When it is your turn, press any key to draw a card.
  When your turn is over,it immediately goes to the next player.
  The winner of the round will then be displayed.
  Repeat this untill the final scores have been released.
  Have fun playing The Card Game\n'''
  print(instructions)

def play(p1,p2):	   # game start
 # input('Would you like the instructions?(Y/N)').lower() == 'y':
 #  instructions(False)
 print('\nLoading  deck',end=".")
 dots()
 print('Shufling deck',end=".")
 dots()
 print('Starting game',end=".")
 dots(1)
 print('')
 deck=list(gen())	  #shuffled deck
 #print(deck) #test deck
 p1w=0
 p2w=0
 p1cards=[]
 p2cards=[]
 while len(deck)!=0:
  tempcards=[]
  # input('It is player 1\'s go:')
  print("player 1's card is",deck[0]) #########
  tempcards.append(deck[0])
  p1T=deck[0]
  deck.pop(0)
  # input('It is player 2\'s go:')
  print(f"player 2's card is {deck[0]}")###########
  tempcards.append(deck[0])
  p2T=deck[0]
  deck.pop(0)
  rwinner=mechanics(p1T,p2T)
  if rwinner==1:
   p1w+=2
   p1cards.append(tempcards[0])
   p1cards.append(tempcards[1])
  elif rwinner==2:
   p2w+=2
   p2cards.append(tempcards[0])
   p2cards.append(tempcards[1])
 # print(p1w,p2w)
 print('The Game has finnished')
 games={
	  p1:p1w,
	  p2:p2w
 }
 # print(games,games[p1]) #
 # print(p1cards,p2cards)
 returnvalue=[games,[p1cards,p2cards]]
 # return games #.   returns name and score
 return returnvalue

def top5(result_type=1):
  if result_type==1:
    file='Winning Results.txt'
  else:
    file='Overall Results.txt'
  try:
    results=open(file,'r')
    content=(results.read())
    content=content.split(';\n')
    content=content[:len(content)-1]
    # print(content)
    #bubblesort
    n = len(content) 
    sortedlist=content #to sort
    for result in range(n-1): 
     for j in range(0, n-result-1): 
      # print(sortedlist[j][len(sortedlist[j])-2:])
      if sortedlist[j][len(sortedlist[j])-2:] > sortedlist[j+1][len(sortedlist[j+1])-2:] : 
          sortedlist[j], sortedlist[j+1] = sortedlist[j+1], sortedlist[j]
    # print(sortedlist)
    if len(sortedlist) >= 5:
      returnvalue=[sortedlist[len(sortedlist)-5:],sortedlist]
      return returnvalue
    else:
      returnvalue=[_,sortedlist]
      return returnvalue
  except:
    raise SyntaxError#sorting didnt work



def storage(games,winner,other):
 # print(games)
 #contains the winners results
 try:
  results=open('Winning Results.txt','a')
 except:
  results=open('Winning Results.txt','w')
 results.write(winner)
 results.write(' ')
 results.write(str(games[winner]))
 results.write('\n')
 results.close()
 #contains the results of the winner and other players
 try:
  results=open('Overall Results.txt','a')
 except:
  results=open('Overall Results.txt','w')
 results.write(winner)
 results.write(' ')
 if len(str(games[winner]))==2:
   gameswon=str(games[winner])
 elif len(str(games[winner]))==1:
   gameswon='0'+str(games[winner])
 results.write(gameswon)
 results.write(';')
 results.write('\n')
 if len(str(games[other]))==2:
   gameswon=str(games[other])
 elif len(str(games[other]))==1:
   gameswon='0'+str(games[other])
 results.write(other)
 results.write(' ')
 results.write(gameswon)
 results.write(';')
 results.write('\n')
 results.close()

 
def main(autorise):	#main start
  p1='Amogh'
  p2='Simha'
 # print('welcome to the card game')
 # p1=input('Enter your name player 1')
 # p2=input('\nEnter your name player 2')
 # if verify(1,autorise,p1)==True and verify(2,autorise,p2)==True:
  games,cards=play(p1,p2)
  if games[p1]>games[p2]:
   print('\n	player 1 "{}" has won this game with {} cards!\n\nTheir cards include:'.format(p1,games[p1]))
   time.sleep(5)
   [print(card) for card in cards[0]]
   storage(games,p1,p2)
  if games[p1]<games[p2]:
   print(f'\n	player 2 "{p2}" has won this game with {games[p2]} cards!\n\nTheir cards include:')
   time.sleep(2)
   [print(card) for card in cards[1]]
   storage(games,p2,p1)
  print('The top 5 results for The Card Game are:')
  time.sleep(1)
  [print(f' -{result}') for result in top5()[0]]
  if input('Do you want to see the rest of the leader board? (y/n)\n').lower() =='y': 
   # results=open('Overall Results.txt','r')
   # print(results.read())
   # results.close()
   print('Leader Board:')
   [print(f' +{result}') for result in top5(0)[1]]
   pass
  print('Well Done!\nThanks for playing The Card Game')
  
#play(1,2) # testing game
main(autorise)
# top5()