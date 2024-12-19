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

step 1. random angle between 30 and 60 to avoid extremes
step 2.
  C side = 16
  A side (x) = 16*cos (prev rand angle)
  B side (y) = 16*sin (prev rand angle)

step 3. multiply x and y by either -1 or 1 at random to determine quadrant direction