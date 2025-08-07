"""1041. Robot Bounded In Circle
Medium

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.


Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.


Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""


def test_rover():
    """pytest rover.py"""
    assert is_valid("G") == False
    assert is_valid("L") == True
    assert is_valid("GGLLGG") == True
    assert is_valid("GG") == False
    assert is_valid("GL") == True
    assert is_valid("GLGLGGLGL") == False


def is_valid(instructions: str) -> bool:
    """
    Determines if a robot executing the given instructions will be bounded in a circle.

    The key insight: After executing the instructions once, the robot will be bounded if:
    1. It returns to the starting position (0,0), OR
    2. It's facing a different direction than it started (not facing North)

    If condition 2 is true, executing the instructions multiple times will eventually
    create a cycle because the robot will change direction with each iteration.
    """

    # Direction vectors: North=(0,1), East=(1,0), South=(0,-1), West=(-1,0)
    # Start facing North (positive Y direction)
    face = (0, 1)

    # Start at origin (0, 0)
    coor = [0, 0]

    # Execute each instruction once
    for c in list(instructions):
        print(c)

        if c == "G":
            # Move forward one unit in current facing direction
            # Add the direction vector to current position
            coor[0] += face[0]  # Update x coordinate
            coor[1] += face[1]  # Update y coordinate

        elif c == "L":
            # Turn 90 degrees left (counter-clockwise)
            # Rotation matrix for 90 degrees CCW: (x,y) -> (-y,x)
            face = (-face[1], face[0])

        elif c == "R":
            # Turn 90 degrees right (clockwise)
            # Rotation matrix for 90 degrees CW: (x,y) -> (y,-x)
            face = (face[1], -face[0])

    # Robot is bounded if:
    # 1. Back at starting position (will repeat exact same path), OR
    # 2. Facing different direction (will eventually form a cycle)
    #    - If facing East/West/South, it will take 2-4 iterations to return to start
    if coor == [0, 0] or face != (0, 1):
        return True

    # If at different position AND still facing North, robot will move infinitely
    return False
