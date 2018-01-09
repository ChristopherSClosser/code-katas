"""Kata: Grasshopper - Terminal game move function.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

- **URL**: [challenge url](https://www.codewars.com/kata/grasshopper-terminal-game-move-function)

#1 Best Practices Solution by GNX & others

def findSmallestInt(arr):
    return min(arr)
"""


def move(position, roll):
    """Simple math."""
    new_position = position + (roll * 2)
    return new_position
