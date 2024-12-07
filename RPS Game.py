print("WELCOM TO ROCK, PAPER, SCISSORS GAME")
print("************************************")


import random

moves_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """,
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

user_move = input("Enter your move (rock, paper, scissors): ")

if user_move not in ["rock","paper","scissors"]:
    print("Invalid input; Please select only in (rock, paper, scissors)")
else:
    move_num = random.randint(1,3)
    if move_num == 1:
        computer_move = "rock"
    elif move_num == 2:
        computer_move = "paper"
    else:
        computer_move = "scissors"

print(f"\nYour Move: {user_move}{moves_art[user_move]}")
print(f"Computer Move: {computer_move}{moves_art[computer_move]}")

if user_move == computer_move:
    print("Tie!!! Try Again!")
elif user_move == "rock":
    if computer_move == "scissors":
        print("Congratulations!!! You win!")
    else:
        print("You Lose! Better luck next time")
elif user_move == "paper":
    if computer_move == "rock":
        print("Congratulations!!! You win!")
    else:
        print("You Lose! Better luck next time")
elif user_move == "scissors":
    if computer_move == "paper":
        print("Congratulations!!! You win!")
    else:
        print("You Lose! Better luck next time")