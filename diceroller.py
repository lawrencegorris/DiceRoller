import random
import time
import os

def clear_console():
    os.system('cls')
    
dice_list = [4, 6, 8, 10, 12, 20, 100]

while True:

  # Get user input
  while True:
    dice_amount_input = input("\nHow many dice do you want to roll?\n")
    try:
      dice_amount = int(dice_amount_input)
    except:
      print("\nPlease add how many dice you want to roll")
    else:
      dice_amount = int(dice_amount_input)
      break

  while True:
    dice_type_input = input(f"\nWhat type of dice do you want to use? Choose from {dice_list} \nD")
    try:
      dice_type_input = int(dice_type_input)
    except:
      print("Please type what type of dice you want to roll")

    if dice_type_input not in dice_list:
      print(f"Please use one of these dice {dice_list}")
    else:
      dice_type = int(dice_type_input)
      break

  # Function to roll dice
  print(f"\nRolling {dice_amount} D{dice_type}...")
  roll_result = []

  def rollDice():
    min_value = 1
    max_value = dice_type

    for roll in range(dice_amount):
      roll_result.append(random.randint(min_value, max_value))
    print(f"\n{roll_result}")
      
  # Run function
  time.sleep(2)
  rollDice()

  #See if user wants to roll again
  responses = ["y", "n"]
  command = ""
  while command not in responses:
    command = input("\nDo want to roll some more dice?\nEnter 'y' to keep going. Type 'n' to stop rolling.\n").lower()
    if command == "":
      print("\nPlease provide an answer.")

  if command == "y":
    clear_console()
    continue
  elif command == "n":
    print("\nThanks for rolling with us. 'Till next time.")
    break