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

# Function to present and solve riddles
def solve_riddle(riddle, solution):
    user_answer = input("Your answer: ").lower()
    return user_answer == solution

def start_page(request):
    global game_state

    # Set initial state when the user clicks "Start"
    if not game_state:
        game_state = {
            'current_room': "Realm of Shadows",
            'inventory': [],
            'msg': "",
            'nearby_artifact': "",
        }

    context = {
        'msg': game_state['msg'],
        'current_room': game_state['current_room'],
        'inventory': game_state['inventory'],
        'nearby_artifact': game_state['nearby_artifact'],
    }

    return render(request, 'adventure/start_page.html', context)

def dungeon_adventure(request):
    # Retrieve game state from the global variable
    global game_state
    # Set initial state when the user clicks "Start"
    if not game_state:
        game_state = {
            'current_room': "Realm of Shadows",
            'inventory': [],
            'msg': "",
            'nearby_artifact': "",
        }
    
    current_room = game_state['current_room']
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

        # Process the user's move and update the game state
        try:
            current_room = dungeon_rooms[current_room][direction]
            msg = f"You explore {direction}"

            # Check for artifact in the room
            if "Artifact" in dungeon_rooms[current_room].keys():
                nearby_artifact = dungeon_rooms[current_room]["Artifact"]

                if nearby_artifact not in inventory:
                    msg += f"\nYou see {nearby_artifact}. Type 'Grab {nearby_artifact}' to collect it."

        except KeyError:
            msg = "You can't go that way."

    elif action == "Grab":
        try:
            if "Artifact" in dungeon_rooms[current_room].keys():
                artifact_name = dungeon_rooms[current_room]["Artifact"]

                if artifact_name == artifact:
                    # Check if a riddle is associated with the artifact
                    riddle_key = f'Riddle {inventory.count(artifact_name) + 1}'

                    if riddle_key in riddles:
                        msg = f"You found an artifact: {artifact_name}. Type 'Solve' to solve the riddle."
                        # Save the artifact and associated riddle details in the game state
                        game_state['current_artifact'] = artifact_name
                        game_state['current_riddle_key'] = riddle_key
                    else:
                        # No riddle for this artifact
                        if artifact_name not in inventory:
                            inventory.append(artifact_name)
                            msg = f"{artifact_name} acquired!"
                        else:
                            msg = f"You already possess the {artifact_name}"
                else:
                    msg = f"Can't find {artifact}"
            else:
                msg = f"There's no artifact to grab in this room."

        except KeyError:
            msg = f"Can't find {artifact}"

    elif action == "Solve":
        # Check if the user has a current artifact and riddle to solve
        if 'current_artifact' in game_state and 'current_riddle_key' in game_state:
            artifact_name = game_state['current_artifact']
            riddle_key = game_state['current_riddle_key']

            if riddle_key in riddles:
                riddle_solution = dungeon_rooms[current_room].get("RiddleSolution", '')
                if solve_riddle(riddles[riddle_key], riddle_solution):
                    msg = f"Congratulations! You solved the riddle and acquired {artifact_name}."
                    inventory.append(artifact_name)
                else:
                    msg = "Incorrect answer. Try again or type 'Explore' to move in a direction."
            else:
                msg = f"No riddle associated with {artifact_name}."

            # Clear the current artifact and riddle details after solving
            game_state.pop('current_artifact', None)
            game_state.pop('current_riddle_key', None)
        else:
            msg = "You don't have any artifacts to solve a riddle. Explore and collect artifacts first."

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
        'dungeon_master': dungeon_rooms[current_room]['DungeonMaster'] if 'DungeonMaster' in dungeon_rooms[current_room].keys() else None,
        'user_input': user_input,
        'action': action,
        'direction': direction,
        'artifact': artifact,
        'riddles': riddles,
        'current_riddle_key': game_state.get('current_riddle_key', ''),  # Add the current riddle key to pass to the template
    }

    # If not a POST request, redirect to start_page
    return render(request, 'adventure/dungeon_adventure.html', context)
