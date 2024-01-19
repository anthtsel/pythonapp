from django.shortcuts import render, redirect

# Define riddles globally within the function
riddles = {
    'Riddle 1': "What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?",
    'Riddle 2': "Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters.",
    'Riddle 3': "It cannot be seen, cannot be felt,\nCannot be heard, cannot be smelt.\nIt lies behind stars and under hills,\nAnd empty holes it fills.\nIt comes out first and follows after,\nEnds life, kills laughter.",
    'Riddle 4': "Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.",
    'Riddle 5': "This thing all things devours;\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel;\nGrinds hard stones to meal;\nSlays king, ruins town,\nAnd beats mountain down."
}

# Global variable to store game state
game_state = {
    'current_room': "Realm of Shadows",
    'inventory': [],
    'msg': "",
    'nearby_artifact': "",
}

def start_page(request):
    return render(request, 'adventure/start_page.html')

# Function to present and solve riddles
def solve_riddle(riddle, solution):
    user_answer = input("Your answer: ").lower()
    return user_answer == solution

def explore_room(request, current_room=None):
    global game_state

    # Initialize action, user_input, direction, and artifact variables here
    action = ""
    user_input = ""
    direction = ""
    artifact = ""

    inventory = game_state['inventory']
    msg = game_state['msg']
    nearby_artifact = game_state['nearby_artifact']

    dungeon_rooms = {
        'Realm of Shadows': {'North': 'Cursed Catacombs', 'South': 'Bat Roost', 'East': 'Ethereal Bazaar'},
        'Cursed Catacombs': {'South': 'Realm of Shadows', 'Artifact': 'Obsidian Shard', 'RiddleSolution': 'mountain'},
        'Bat Roost': {'North': 'Realm of Shadows', 'East': 'Infernal Abyss', 'Artifact': 'Sorcerer Staff', 'RiddleSolution': 'wind'},
        'Ethereal Bazaar': {'West': 'Realm of Shadows', 'North': 'Frostbite Forge', 'East': 'Training Grounds', 'Artifact': 'Phantom Elixirs', 'RiddleSolution': 'dark'},
        'Frostbite Forge': {'South': 'Ethereal Bazaar', 'East': 'Quicksand Pit', 'Artifact': 'Frostbound Blade', 'RiddleSolution': 'fish'},
        'Quicksand Pit': {'West': 'Frostbite Forge', 'Artifact': 'Venomous Cloak', 'RiddleSolution': 'time'},
        'Infernal Abyss': {'West': 'Bat Roost', 'Artifact': 'Hellfire Elixir', 'RiddleSolution': 'fish'},
        'Training Grounds': {'West': 'Ethereal Bazaar', 'DungeonMaster': 'Gollum'}
    }
    
    # Check if current_room is None (for example, if the view is called without a room specified)
    if current_room is None:
        # Redirect to the start_page or any other appropriate page
        return render(request, 'adventure/start_page.html')

    if request.method == 'POST':
        # Retrieve user's move from the form data
        user_input = request.POST.get('user_input', '')
        
        # Set initial values for the game state
        action = ""
        direction = ""
        artifact = ""

        # Parse the user input
        user_input_split = user_input.split(' ')
        action = user_input_split[0].title()

        if len(user_input_split) > 1:
            direction = user_input_split[1].title()
            artifact = " ".join(user_input_split[1:]).title()
            
        if action == "Explore":
            if direction in dungeon_rooms[current_room]:
                # Process the user's move and update the game state
                current_room = dungeon_rooms[current_room][direction]
                msg = f"You explore {direction}"

                # Check for artifact in the room
                if "Artifact" in dungeon_rooms[current_room].keys():
                    nearby_artifact = dungeon_rooms[current_room]["Artifact"]

                    if nearby_artifact not in inventory:
                        msg += f"\nYou see {nearby_artifact}. Type 'Grab {nearby_artifact}' to collect it."
            else:
                msg = "You can't go that way."

        elif action == "Grab":
            try:
                # Get the artifact name in the room (case-insensitive)
                artifact_name_in_room = dungeon_rooms[current_room].get("Artifact", "").lower()

                # Check if the lowercase user's input contains the lowercase artifact name in the room
                if artifact_name_in_room in artifact.lower():
                    # Check if a riddle is associated with the artifact
                    riddle_key = f'Riddle {inventory.count(artifact_name_in_room) + 1}'

                    if riddle_key in riddles:
                        msg = f"You found an artifact: {artifact_name_in_room}. Type 'Solve' to solve the riddle."
                        # Save the artifact and associated riddle details in the game state
                        game_state['current_artifact'] = artifact_name_in_room
                        game_state['current_riddle_key'] = riddle_key
                    else:
                        # No riddle for this artifact
                        if artifact_name_in_room not in inventory:
                            inventory.append(artifact_name_in_room)
                            msg = f"{artifact_name_in_room} acquired!"
                        else:
                            msg = f"You already possess the {artifact_name_in_room}"

                    # Update current_room after the "Grab" action
                    exit_directions = dungeon_rooms[current_room].keys()
                    if 'South' in exit_directions:  # Check if there is a South exit
                        current_room = dungeon_rooms[current_room]['South']
                        msg += f"\nYou explore South"
                    else:
                        msg += "\nThere's no exit to the South."

                    # Check for artifact in the new room
                    if "Artifact" in dungeon_rooms[current_room].keys():
                        nearby_artifact = dungeon_rooms[current_room]["Artifact"]
                        if nearby_artifact not in inventory:
                            msg += f"\nYou see {nearby_artifact}. Type 'Grab {nearby_artifact}' to collect it."

                else:
                    msg = f"Can't find {artifact}"

            except KeyError:
                msg = f"Can't find {artifact}"
            
        if action == "Solve":
            # Check if the user has a riddle to solve
            if 'current_riddle_key' in game_state:
                user_answer = user_input.lower()
                correct_answer = riddles[game_state['current_riddle_key']].lower()

                if user_answer == correct_answer:
                    # Correct answer
                    artifact_name = game_state['current_artifact']
                    inventory.append(artifact_name)
                    msg = f"Correct! You acquired {artifact_name}."
                    del game_state['current_artifact']
                    del game_state['current_riddle_key']
                else:
                    # Incorrect answer
                    msg = "Incorrect answer. Try again or explore."

    # Update the global game state
    game_state['current_room'] = current_room
    game_state['inventory'] = inventory
    game_state['msg'] = msg
    game_state['nearby_artifact'] = nearby_artifact

    context = {
        'current_room': current_room,
        'inventory': inventory,
        'msg': msg,
        'nearby_artifact': nearby_artifact,
        'dungeon_master': dungeon_rooms[current_room].get('DungeonMaster', None),
        'user_input': user_input,
        'action': action,
        'direction': direction,
        'artifact': artifact,
    }

    # If not a POST request, redirect to start_page
    return render(request, 'adventure/dungeon_adventure.html', context)
