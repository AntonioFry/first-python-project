print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
  print("You are old enough!")

  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Let's play!")

    left_or_right = input("First choice... (left/righ)? ")

    if left_or_right == 'left':
      ans = input("You find a bridge. Do you cross it? (yes/no)? ")

      if ans == 'yes':
        print("The bridge breaks and you die...")

      else:
        print("You turn around and head back the way you came... good job.")

    else:
      print("You fell to your death...")
  
  else:
    print("Bye.")

else:
  print("You are not old enough to play.")

