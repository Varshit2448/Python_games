import random as rand
rock = '''
    _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
 '''

paper = '''
     _______
 ---'   ____)____
           ______)
           _______)
          _______)
 ---. __________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
start_game = int(input("Welcome I am goats Do you wanna play with me Click 1 : "))
while(start_game==1):
    user_move=int(input("Enter Your choice gammer {0 for rock}\n{1 for paper}\n{2 for scissors}  "))
    if(user_move<=2 and user_move>=0):  
      game=[rock,paper,scissors]
      ran_move=rand.randint(0,len(game)-1)
      comp_move=game[ran_move]
      print(game[user_move])   
      if(ran_move==user_move):
        print("Its a draw.")
        print(comp_move)
      elif((ran_move==0 and user_move==2) or (ran_move==1 and user_move==0) and (ran_move==2 and user_move==1)):
        print("You lose but try to win again.")
        print(comp_move)
      else:
        print("YAY,You win party leda pushpa")
        print(comp_move)
    else:
      print("Please! use instructed numbers only")

    start_game = int(input("Don't you wanna play with me if yes click 1 else click any number : "))
     


 
