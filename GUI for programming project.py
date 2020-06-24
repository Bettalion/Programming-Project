#gui Uses python 2, else uses python 3 
import Tkinter as tk
import time
class Player:
 def __init__(self,name,password,score,deck,cards):
  self.name=name
  self.password=password
  self.score=score
  self.deck=deck
  self.cards=cards

class GUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
    def create_win(self,player,card):
        self.player=player
        self.card=card
        self.button = tk.Button(self.frame, text = 'Press to Draw P{}'.format(self.player.name), width = 25, command = self.new_window)
        self.button.pack()
        self.frame.pack()
        return 1234
    def new_window(self):
        self.cardwin=tk.Tk()
        label=tk.Label(self.cardwin,text='Your card is:').pack()
        label2=tk.Label(self.cardwin,text=self.card).pack()
        quitbutton=tk.Button(self.cardwin,text='quit',command=self.destroywin).pack()
    def destroywin(self,win=1):
     try:
      self.cardwin.destroy()
      self.master.destroy()
     except:
      pass
     return 1234  # return an arbitray value so the code runs in sequence not simulaneous
class display:
 def __init__(self, master,text2disp):
  self.master = master
  self.dlabel=tk.Label(self.master,text=text2disp).pack()
def main(): 
    arr=[1,2,3,4,5,6,7,8]
    p1=Player('a','2',4,arr[:len(arr)//2],arr[:4])
    p2=Player('b','2',5,arr[len(arr)//2:],arr[4:])
    root = tk.Tk()
    app = GUI(root)
    z=app.create_win(p1,arr[1])
    root.mainloop()

    root2=tk.Tk()
    dwinner=display(root2,'I love you Matilda')
    root.mainloop()
    
    

if __name__ == '__main__':
    main()