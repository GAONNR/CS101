##########################################################################
# Title :
# Author :
# The number of hours taken for finishing the homework :
##########################################################################
from cs1robots import *

# Define functions for turning right and around
def Hubo_turn_right():
    for i in range(3):
        Hubo.turn_left()

def Hubo_turn_around():
    for i in range(2):
        Hubo.turn_left()

def Ami_turn_right():
    for i in range(3):
        Ami.turn_left()

def Ami_turn_around():
    for i in range(2):
        Ami.turn_left()

load_world("Mazes/Maze5.wld")

Hubo = Robot(avenue=1, street=2, color = "gray", beepers = 1000)
Ami = Robot(avenue=7, street=2, color = "purple", orientation = "S", beepers = 1)
# The positions of Hubo and Ami are fixed.
# Modify the number of beepers if you need.

Hubo.set_trace("blue")
Ami.set_trace("purple")

Hubo.drop_beeper()          # Indicate the exit of the maze
Hubo.move()
Ami.drop_beeper()           # Indicate the position of Ami

while not Hubo.on_beeper() or Hubo.front_is_clear() or Hubo.right_is_clear() or Hubo.left_is_clear():
    num_of_drop = 0

    if Hubo.front_is_clear():
        num_of_drop = num_of_drop + 1
    if Hubo.right_is_clear():
        num_of_drop = num_of_drop + 1
    if Hubo.left_is_clear():
        num_of_drop = num_of_drop + 1
    # num_of_drop means the number of beepers that Hubo needs to drop
    # this equals to the number of directins that Hubo can go to

    if not Hubo.on_beeper():
        for i in range(num_of_drop):
            Hubo.drop_beeper()

    else:
        Hubo.pick_beeper()
    # if there are beepers under Hubo, (it means Hubo was going back the way)
    # Hubo picks up beeper, and if there are no beeper, Hubo drops the beeper to make trace

    if num_of_drop == 0:
        Hubo_turn_around()
    # num_of_drop == 0 means that there are no way that Hubo can go to, o Hubo should turn around

    # Follow Right Wall
    if Hubo.right_is_clear():
        Hubo_turn_right()
    while not Hubo.front_is_clear():
        Hubo.turn_left()
    Hubo.move()
    # /Follow Right Wall

# Ami is here. Let's go back to the exit.
while not Hubo.front_is_clear():
    Hubo.turn_left()
while not Ami.front_is_clear():
    Ami.turn_left()

while Hubo.on_beeper():     # please modify this condition to 'not Hubo.on_beeper()' when you do not use the the indicated route.
    Hubo_turn_count = 0
    num_of_dir = 0
    chk = 0

    if Hubo.front_is_clear():
        num_of_dir = num_of_dir + 1
    if Hubo.right_is_clear():
        num_of_dir = num_of_dir + 1
    if Hubo.left_is_clear():
        num_of_dir = num_of_dir + 1

    # num_of_dir means as same as the num_of_drop.

    if num_of_dir == 0:
        Hubo.pick_beeper()
        Hubo_turn_count = 4
    #If there is nowhere to go for Hubo, it means Hubo arrived to the end.
    #So he just picks up the beeper

    elif num_of_dir == 1:
        if Hubo.right_is_clear():
            Hubo_turn_right()
            Hubo_turn_count = 3
        elif Hubo.left_is_clear():
            Hubo.turn_left()
            Hubo_turn_count = 1
        Hubo.move()
    #If there were only one way to go, Hubo go to the way he can only go to

    else:
        if Hubo.right_is_clear() and chk == 0:
            Hubo_turn_right()
            Hubo_turn_count = 3
            Hubo.move()
            chk = 1
            if not Hubo.on_beeper():
                Hubo_turn_around()
                Hubo.move()
                Hubo_turn_right()
                chk = 0

        if Hubo.front_is_clear() and chk == 0:
            Hubo_turn_count = 0
            Hubo.move()
            chk = 1
            if not Hubo.on_beeper():
                Hubo_turn_around()
                Hubo.move()
                Hubo_turn_around()
                chk = 0

        if Hubo.left_is_clear() and chk == 0:
            Hubo.turn_left()
            Hubo_turn_count = 1
            Hubo.move()
            chk = 1
            if not Hubo.on_beeper():
                Hubo_turn_around()
                Hubo.move()
                Hubo.turn_left()
                chk = 0
    #if there are several ways those hubo can go to, Hubo will search all the direction.
    #if there were no beeper in one direction, Hubo will go back and search another direction.

    while Ami.on_beeper():
        Ami.pick_beeper()
    #Ami will pick up the beepers while following Hubo.

    if Hubo_turn_count == 1:
        Ami.turn_left()
    elif Hubo_turn_count == 3:
        Ami_turn_right()
    if not Hubo_turn_count == 4:
        Ami.move()
    #Ami is guided by Hubo. Ami's direction is decided by the variable Hubo_turn_count.
