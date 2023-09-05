# William Fishburn

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom', 'Exit': 'Exit Room'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'Exit': 'Exit Room'},
    'Cellar': {'West': 'Bedroom', 'Exit': 'Exit Room'},
    'Exit Room': {}
}

# Set default location and current room to "Great Hall"
location = 'Great Hall'
current_room = "Great Hall"

# Create empty variable for directional moves
direction = " "

# Game Loop
while direction != 'exit' or 'Exit':
    print("\nYou are in the", location)

    # Print the Child key of the Parent Key
    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    # Print the values of the Child key
    possible_exits = rooms[current_room]
    print("Possible exits: ", possible_exits)

    # Take user input for direction
    direction = input("Which way to go? ")

    # Decision branch
    if direction in possible_moves:
        current_room = possible_exits[direction]
        print(f"You are now in the {current_room}")

        # Re-assign location variable to the next current room
        location = current_room

        # Nested IF statement to leave the game if Exit Room is selected
        if current_room in ['Indestructible Room']:
            if len(carrying) == 6:
                print('You collected all of the items, and defeated the minotaur!')
            else:
                print('It looks like you have not found everything, you have been defeated!')
            break

    # Alternative exit command to exit the game
    elif direction == 'exit' or direction == 'Exit':
        print("Entering exit room. Thank you for playing! Goodbye.")
        exit(0)

    # Invalid input validation
    else:
        print(f"{direction} is not a valid exit from {current_room}")
