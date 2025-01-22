# Create a Python function to simulate the game of Pig with the following specifications:

# Inputs:
    # player_score: int . Accept the current player score player
    # target_score: int . Score player needs to reach or exceed to win


# Logic:
    # Simulate a dice roll and add result to player_score
    # If player rolls 1, all points lost and game ends.
    # If player 'banks', dice is added to their player_score and ends turn
    # If the player doesn't bank, 
    # If the score (after banking) reaches or exceeds the target, the function should declare the player as the winner.

    # dice: int           Allow input of the results of dice rolls.
    # bank: bool           the points.

# Outputs:
    # The updated overall score of the player.
    # The status of the game (e.g., whether the turn is ongoing, the player has banked, or the player has won).
    # Any relevant messages about the result of the dice roll or the consequences of their decision.

def play_pig(player_score:int, target_score:int):
    pass


print(play_pig(0, 10))
