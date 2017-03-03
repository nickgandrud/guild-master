# Author: Michael
# this is the where we're going to start simulating and calculating things
# so now we can pass individual points (plural is the important part) to
# inverseKinematicSolver, which will solve for the control angles, and then pass
# them to roboticArmSim to draw the arm in the new position 

groundLink = sqrt(4000)
L1 = 160
L5 = 200 
L6 = 40 # start of the 3rd box, 
angle6 =45; # set the 3rd box's angle
L8 = 50  # length of the bottom part of the end effector 
b = # L5-groundLink; 

y = 50;

# finally, add in one more line to rArmSimulator.m at the very end: 
# GcodeSpitter([0 0 0],1);
