import time
import random
from tkinter import *
print('Programming Project Classes Imported')
# players and gui
class player:
 def __init__(self,name,passw):
     self.name= name
     self.passw= passw
     self.temp=None
     self.wincards=[]
     
class GUI:
    def __init__(self, master): 
        self.master=master
    def create_win(self,player,card): # allows the player to draw a card
        self.player=player
        self.card=card[0]
        self.setcol=card[3]
        self.master.title('Draw Card')
        button = Button(self.master, text = 'Press to Draw Player:{}'.format(self.player.name), width = 25, command = self.card_win)
        button.pack()
        self.master.mainloop()
        print(f'{self.player.name}, your card is {self.card}!')
        return self.card
    
    def card_win(self): # reveals to the player their card
        self.cardwin=Tk()
        self.cardwin.configure(bg=self.setcol)
        self.cardwin.title('{},your Card is:'.format(self.player.name))
        label=Label(self.cardwin,text=f'Your card is: {self.card}',bg=self.setcol,font=("Helvetica", "18")).pack() 
        quitbutton=Button(self.cardwin,text='quit',command=self.destroywin,bg='light grey').pack()
    def destroywin(self,win=1):# destroys current window
     try:
      self.cardwin.destroy()
      self.master.destroy()
     except:
      pass
    def displaywin(self,winner): # displays the winner of the round
        self.master.title(f'Well done {winner.name}!')
        Label(self.master,text=f'Well done {winner.name}, you have won this round!').pack()
    def displaytop5(self,phraser): # displays the top 5 results
        self.master.title(f'Top 5 Scores')
        for sen in phraser:
           Label(text=sen).pack() 
    

        
