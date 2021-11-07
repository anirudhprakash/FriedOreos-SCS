# Description
MapQuest 112 is a single-player, turn based strategy game that simulates a war between the imperialist Taylor Faction and the Rebel Kosbie Function (read more about the lore in game). Players will take turns creating earning troops, conquering structures, and attempting to achieve the ultimate goal of capturing the opponents base. To start the game, run the MapQuest112.py file.

# Project elements:
1) Map generation
2) Minimax AI
3) Frontend

# Map generation
The map is a randomly generated board with some "magic numbers" for the probability of squares being obstacles, field, or special squares. We then verify the validity of the map by running a BFS between each pair of points to ensure that no squares are "Locked off". And to ensure the fairness of the map, we make sure that no player is at a significant disadvantage.

# Minimax AI
