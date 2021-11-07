
# Project elements:
1) Map generation
2) Minimax AI
3) Frontend

# Map generation
The map is a randomly generated board with some "magic numbers" for the probability of squares being obstacles, field, or special squares. We then verify the validity of the map by running a BFS between each pair of points to ensure that no squares are "Locked off". And to ensure the fairness of the map, we make sure that no player is at a significant disadvantage.

# Mini
