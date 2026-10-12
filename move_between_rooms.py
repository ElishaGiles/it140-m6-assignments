Prompt
For this milestone, you will be submitting a working draft of code for a simplified version of the text-based game that you are developing for Project Two. You will use the Milestone Simplified Dragon Text Game resources and sample code to make a working room dictionary using the “move” commands. This will include the if, else, and elif statements that move the adventurer from one room to another. It’s important that you use the starter code from the examples to get started, but expand on that code to reach the ideas you submitted in your Project One submission.

Before beginning this milestone, it is important to understand the required functionality for this simplified version of the game. The game should prompt the player to enter commands to either move between rooms or exit the game. Review the Milestone Simplified Dragon Text Game Video and the Milestone Simplified Text Game Flowchart to see an example of the simplified version of the game. A video transcript is available: Transcript for Milestone Simplified Dragon Text Game Video.

IMPORTANT: The “Move Between Rooms” process in the Milestone Simplified Text Game Flowchart is intentionally vague. You designed a more detailed flowchart or pseudocode for this process as a part of your work on Project One. Think about how your design will fit into this larger flowchart.
In your IDE, create a new code file titled “move_between_rooms.py.” As you develop your code, you must use industry standard best practices, including comments, whitespace, and appropriate naming conventions, to enhance the readability and maintainability of the code.
Next, copy the following dictionary into your PY file. This dictionary links rooms to one another and will be used to store all possible moves per room, in order to properly validate player commands (input). This will allow the player to move only between rooms that are linked.

Note: For this milestone, you are being given a dictionary and map for a simplified version of the dragon-themed game. Make sure to read the code carefully so that you understand how it works. In Project Two, you will create your own dictionary based on your designs.
# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'south': 'Bedroom'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
        'Cellar': {'west': 'Bedroom'}
    }
A portion of the map for the Dragon Text Game showing the Great Hall, Bedroom, and Cellar, with arrows indicating the directions the player can move between them. The Cellar is to the East of the Bedroom, which is to the South of the Great Hall.

Next, you will develop code to meet the required functionality by prompting the player to enter commands to move between the rooms or exit the game. To achieve this, you must develop the following:
A gameplay loop that includes:
Output that displays the room the player is currently in
Decision branching that tells the game how to handle the different commands. The commands can be to either move between rooms (such as go north, south, east, or west) or exit.
If the player enters a valid “move” command, the game should use the dictionary to move them into the new room.
If the player enters “exit,” the game should set their room to a room called “exit.”
If the player enters an invalid command, the game should output an error message to the player (input validation).
A way to end the gameplay loop once the player is in the “exit” room
TIP: Use the pseudocode that you designed in Step 4 of Project One to help you develop your code.
As you develop, you should debug your code to minimize errors and enhance functionality. After you have developed all of your code, be sure to run the code to test and make sure it is working correctly.
What happens if the player enters a valid direction? Does the game move them to the correct room?
What happens if the player enters an invalid direction? Does the game provide the correct output?
Can the player exit the game?
