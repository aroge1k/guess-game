import random

name = input("lets play a game... whats your name? ")
print("welcome " + name + " Im thinking of a number between 1 and 100, if you get it right your chains will be released, if you dont get it in 5 guesses, well...")

my_number = random.randint(1, 100)
guesses = []
for guess_number in range(1, 11):
  valid_guess = False
  while not valid_guess:
    try:
      user_guess = int(input("take a guess...\n"))
      valid_guess = True
    except ValueError:
      print("please provide a valid number.")
      
  difference = abs(my_number - user_guess)
  guesses.append(user_guess)
  
  if user_guess < my_number and difference > 10:
    print("Your guess is very low. Try again.")
  elif user_guess < my_number and difference < 10:
    print("your guess is a little low. Try again.")
  elif user_guess > my_number and difference > 10:
    print("your guess is very high. try again")
  elif user_guess > my_number and difference < 10:
    print("your guess is a little too high")
  else:
      break
  
if user_guess == my_number:
  print("you won" + name + "! you guessed my number in " +       str(guess_number) + " guesses.")
  print("Your guesses were: " + " ".join(str(x) for x in guesses))
else:
  print("sorry you didnt guess my number. the number I am thinking of is " + str(my_number))

#test commit
