# Pong

- player tile
- computer tile
- score (player and opponent?)
- divider line
- ball

- get window up
- get player tile controllable
- get enemy tile moving
- get ball to move and make contact
- keep score


1. Create the screen
2. Create and move a paddle
3. Create second enemy paddle (would be cool to make two player getting wasd and arrow keys)
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

for ball direction:

0-east | 90 - north | 180 - west | 270 - south

step 1. random angle between 0 and 90. (really angle between 30 and 60?)
step 2. random 0-3. add result * 90 (for quadrant)
step 3. a^2 + b^2 = c^2. trig algo
  C side = 16
  A side (x) = 16*cos (prev rand angle)
  B side (y) = 16*sin (prev rand angle)