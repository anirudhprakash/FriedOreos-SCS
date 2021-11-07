# Description
MapQuest 112 is a single-player, turn based strategy game that simulates a war between the imperialist Taylor Faction and the Rebel Kosbie Function (read more about the lore in game). Players will take turns creating earning troops, conquering structures, and attempting to achieve the ultimate goal of capturing the opponents base. To start the game, run the MapQuest112.py file.

# Project elements:
1) Map generation
2) Minimax AI
3) Frontend

# Map generation
The map is a randomly generated board with some "magic numbers" for the probability of squares being obstacles, field, or special squares. We then verify the validity of the map by running a BFS between each pair of points to ensure that no squares are "Locked off". And to ensure the fairness of the map, we make sure that no player is at a significant disadvantage.

# Minimax AI
The Artificial Intelligence that runs the opponent is written in the file "Ai.py" and it is based on a MiniMax algorithm with a simple heuristic.

# Running the program
To play the game, simply open the file "MapQuest 112.py" in your chosen compiler and hit run! We do not rely on any externally sourced libraries other than cmu_112_graphics.py. But our code was built using some other Python modules like random, collections, and copy which are typically available with normally downloaded python modules.

# The files in the program:
1) pieces.py: Some dataclasses that we use to represent the gameState
2) MapQuest 112.py: The main driver program that runs all of the animations and the AI.
3) Ai.py: The minimax artificial intelligence.
4) Images: The folder of the sprites that we used to represent the characters.
5) AI.py: A scrap file that we used for testing, rough work etc.
