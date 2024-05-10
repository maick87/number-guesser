# Importing necessary modules
import random  # For generating random numbers
import os      # For interacting with the operating system

# Generating a random number between 1 and 100
numb_gen = random.randint(1, 100)

# Initializing variables to keep track of player's attempts and maximum allowed attempts
player_tries = 0
max_tries = 5

# Starting an infinite loop to keep the game running until the player wins or exceeds the maximum attempts
while True or player_tries < max_tries:

    # Getting player's input
    player_number = input('Type a number: ' if player_tries < max_tries - 1 else 'Last chance!' )

    # Checking if the input is a valid integer
    try:
        player_number = int(player_number)
    except ValueError:
        # Informing the player to input only integers if the input is not a valid integer
        print('Error. Type only integrers')
        continue  # Skipping the rest of the loop and asking for input again
    
    # Checking if player's guess is correct
    if player_number == numb_gen:
        print('You won!!')
        # Asking the player if they want to play again
        player_input = input('Play again YES/NO = ').upper()
        if player_input == 'YES':
            # Resetting the game if the player wants to play again
            os.system('cls')  # Clearing the screen
            player_tries = 0
            numb_gen = random.randint(1, 100)
            continue
        elif player_input == 'NO':
            # Exiting the game if the player doesn't want to play again
            os.system('cls')
            print('thanks for using my code')
            break
    
    # Informing the player to guess a higher number if their guess is lower than the generated number
    elif player_number < numb_gen:
        if player_tries < max_tries - 1:
            print('Try a high number.')
        player_tries += 1
    
    # Informing the player to guess a lower number if their guess is higher than the generated number
    else:
        if player_tries < max_tries - 1:
            print'Try a low number.')
        player_tries += 1 

    # Checking if the player has used all their attempts
    if player_tries == max_tries:
        os.system('cls')  # Clearing the screen
        print('You lose!! The right number is = ', numb_gen)
        # Asking the player if they want to play again
        player_input2 = input('Play again YES/NO = ').upper()
        if player_input2 == 'YES':
            # Resetting the game if the player wants to play again
            os.system('cls')
            player_tries = 0
            numb_gen = random.randint(1, 100)
            continue
        elif player_input2 == 'NO':
            # Exiting the game if the player doesn't want to play again
            os.system('cls')
            print('thanks for using my code')
            break
