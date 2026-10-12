"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

current_room = "Great Hall"

while current_room != "exit":
    print("You are in the ", current_room)

    command = input("Enter a direction (North, South, East, West) or exit: ").lower()

    if command == "exit":
        current_room = "exit"
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    else:
        print("Invalid command. You cannot go that way.")

print("Thanks for playing!")
