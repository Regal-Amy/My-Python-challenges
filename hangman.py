import random
import os, time

print ("HANGMAN!!")
time.sleep(3)
print("Generating Words...")
time.sleep(2)
print("Please Wait...")
time.sleep(2)
print()

listOFword = []


word = random.choice(listOFword)
allLetters = []
correct_letters = []
lives = 6

while lives > 0: 
  letter = input("choose a letter: ".lower())

  if letter in allLetters:
    print("letter has been chosen before, try again!")
  else:
    if letter in word:
      print("correct!")
      correct_letters.append(letter)
      for i in word:
        if i in correct_letters:
          print(i, end="")
        else:
          print("_", end="")
      print()  
    else:
      lives -= 1
      print(f"not in word\n{lives} lives left")
  c_word = "".join(correct_letters)
  if set(c_word) == set(word):
    print("You Win \nGame Over")
    break
    
  allLetters.append(letter)
  time.sleep(1)
  #os.system("clear")
else:
  print("You Lose! \nGame Over!!!!!!!")