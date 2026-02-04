import random      
numbers=correct
answer={"correct": ["1", "2", "3", "4", "5"]}
resposta=random.choice(answer[numbers])
print("guess the number (1 to 5)")
while True:
  player=input("your answer: ").lower
if player == resposta
  print("congratulations, you guessed it!")
  break
else:
  print("no, try again.")
  
