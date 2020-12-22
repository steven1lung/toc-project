from transitions.extensions import GraphMachine

from utils import send_text_message

import random

answer = []
MAX_GUESS = 10
guess = []

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)


    def is_going_to_playgame(self, event):
        text = event.message.text
        return text.lower() == "play"

    def on_exit_user(self,event):
        print("hey here")
        global answer
        answer= list(str(random.randint(100,999)))

    def on_enter_playgame(self,event):
        reply_token=event.reply_token
        text='Enter a 3-digit number to guess'
        send_text_message(reply_token,text)
        print("in playgame")
        self.advance(event)
        




    def on_enter_answeruser(self, event):
        win=False
        reply_token=event.reply_token
        print(answer)


#        for i in range(1,MAX_GUESS):
 #           send_text_message(reply_token,"Round %2d"%(i))
  #          guess = list(event.message.text)
   #         while len(guess) != 3 :
    #            send_text_message(reply_token,"Guess Again !")
#                guess = list(event.message.text)
 #           correct = decide(guess,answer,len(answer))
  #          if correct == len(answer):
   #             machine.go_to_win(event)
    #            break

        self.go_to_win(event)




    def decide(guess,answer,length):
        a=b=0
        for i in range(length):
            if answer[i]==guess[i]:
                a+=1
            elif answer[i] in guess:
                b+=1

        send_text_message(event.reply_token,"%dA%dB"%(a,b))
        return a

        
