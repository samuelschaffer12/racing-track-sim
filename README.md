# Final Project
BCOG 200


1. This project is a user interactive racing simulator where you draw a custom track in a pygame window, and my code returns which car that I created would win the race. There are 4 different cars, each with different stats and strengths, such as speed, turning left, and turning right. The code chooses a winner depending on the track designed by the user. Each does better in different stats and the program times the hypothetical time each car would take to run through the track, and prints the fastest time in the terminal.

## Requirments
Python 3 and Pygame must be installed

pip3 install pygame

runs with "python3 project.py"

A white window will appear where you can click your mouse down and draw your track.

2. A. I would have a create track function that lets the user draw and make the track to the way of their liking.
B. My second function would be calculating how long each individual car would take around the track depending on how it looks.
C. Following that, I would have a function that takes the times of all the cars and chooses the winner with the shortest time.