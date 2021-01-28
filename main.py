from random import randint 
# from art import logo  

easy_level_turns=10 
hard_level_turns=5

def check_answer(guess,answer,turns):
  if guess>answer:
    print("Too High.") 
    return turns-1
  elif guess<answer:
    print("Too Low. ") 
    return turns-1
  else:
    print(f"You got it! The answer was {answer}.")







def set_difficulty():
  level=input("Choose a difficulty : 'easy' or 'hard': ") 
  if level=="easy": 
    return easy_level_turns 
  else:
    return hard_level_turns   






 

    

def game():
  # print(logo)
# Choosing a random number between 1 & 100 : 
  print("Welcome to the number Guessing Game ! ") 
  print("I am thinking of a number between 1 and 100 ") 

  answer=randint(1,100)
  print(f"The answer is {answer}")
  turns= set_difficulty() 
  
  guess=0 
  while guess!=answer:
    print(f"You have {turns} turns remaining. ")  
    guess=int(input("make a guess. "))  
    turns=check_answer(guess,answer,turns)  
    if turns==0:
      print("You have run out of guesse's. ") 
      return 
    elif guess!=answer:
      print("Guess again!. ") 





game() 
# Make a function for difficulty: 




