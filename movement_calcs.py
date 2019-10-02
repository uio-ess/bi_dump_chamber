#!/usr/bin/env python3

# assuming UHV actuator part# HLSML64-600-H
# all units in mm

actuator_travel = 600 # maximum possible travel of actuator
actuator_flange_spacing_min = 260 # minimum possible distance from top of moving flange to bottom of stationary one
acutator_flange_spacing_max = actuator_flange_spacing_min + actuator_travel

# the distance between the center of the chamber and the bottom of the non-moving flange of the actuator 
vessel_cross_center_to_actuator_bottom_flange = 682.45

# distance between the center of the chamber and the bottom flange surface
vessel_cross_center_to_vessel_bottom_flange = 464.42

# the minimum distance between the bottom edge of the stationary acutator flange and the top of the sample holder crossbar
# such that the cross bar can't crash into the top of the chamber when the moving flange is at its highest point
required_top_clearance = 63.80 + 1.2

# length of the long vertical shaft in the screen holder frame
long_shaft_length = acutator_flange_spacing_max + required_top_clearance

# vertical dimension of the top horizontal screen holder bar (aka the bar's cross-sectional, width=height)
screen_holder_bar_width = 25

# vertical spacing between the bottom face of the horizontal screen holder bar and the top edge of the top screen
top_screen_holder_spacing = 0

# vertical spacing between the bottom edge of the top screen and the top edge of the bottom screen
screen_screen_spacing = 1

# vertical distance between the top edge of the screen and the bottom surface of the long vertical shaft
top_screen_long_shaft_spacing = screen_holder_bar_width + top_screen_holder_spacing

# dimension of the screen
screen_dim_y = 230
screen_dim_x = 290

beam_pipe_diameter = 250

crossbar_shaft_width = beam_pipe_diameter+2*screen_holder_bar_width
side_shaft_lengths = 2 * screen_dim_y + screen_screen_spacing + top_screen_holder_spacing

# total frame holder assembly vertical dimension
assembly_dim = long_shaft_length + side_shaft_lengths + screen_holder_bar_width

#  possible screen positions
#  A = no screen in beam
#  B = lower screen installed
#  C = upper screen installed

# the actuator will have 5 location sensing switches:
# LT = the top limit switch, prevents the screens from being pulled out too far
# SA = the position switch for when the screen is in position A
# SB = the position switch for when the screen is in position B
# SC = the position switch for when the screen is in position C
# LB = the bottom limit switch, prevents the screens from being moved too far into the chamber

# position switch locations:
# defined as switch installation position such that the distance between the midpoint of the switch
# hysteresis occurs when the the bottom of the stationary flange is this many mm away from the top of the moving flange
# must be on the interval [fully withdrawn, fully inserted] = [860,260]

minimum_switch_switch_spacing = 5  # smallest possible spacing between limit/position switches

TOP_STOP_pos = acutator_flange_spacing_max # location to install the top movement stopper this 
LT_pos = TOP_STOP_pos - minimum_switch_switch_spacing  # just some number to prevent the actuator from crashing into its self at the end of travel
SA_pos = LT_pos - minimum_switch_switch_spacing - 5  # the screens are now very close to as far away from the beam as we can possibly get them
SB_pos = 1.5 * screen_dim_y + screen_screen_spacing + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange  # bottom screen centered in beam
SC_pos = 0.5 * screen_dim_y + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange # top screen centered in beam
LB_pos = SC_pos - 20  # no reason to allow for pushing the screens in further than a few mm past SC
BOTTOM_STOP_POS = LB_pos - minimum_switch_switch_spacing # location to install the bottom movement stopper

# check that everything is within the travel limits of the actuator
highest_thing = max([TOP_STOP_pos, LT_pos, SA_pos, SB_pos, SC_pos, LB_pos, BOTTOM_STOP_POS])
lowest_thing = min([TOP_STOP_pos, LT_pos, SA_pos, SB_pos, SC_pos, LB_pos, BOTTOM_STOP_POS])
if ( ((highest_thing<=acutator_flange_spacing_max)and(highest_thing>=actuator_flange_spacing_min)) and ((lowest_thing<=acutator_flange_spacing_max)and(lowest_thing>=actuator_flange_spacing_min)) ):
	print("Looks good, everything is within the mover's travel limits")
else:
	print("ERROR: Something is not within the mover's travel limits")

# check that BOTTOM_STOP_POS prevents bottom crashing
bottom_padding = vessel_cross_center_to_vessel_bottom_flange - ((vessel_cross_center_to_actuator_bottom_flange + BOTTOM_STOP_POS) - assembly_dim )
if bottom_padding <= 0:
	print("ERROR: Assembly can crash into the bottom of the vessel")
else:
	print("Looks good, the assembly can't crash into the bottom of the vessel.")

# distance between the bottom of the frame assembly and bottom flange surface when at LB (must be > 0 to avoid crash into bottom of chamber)
#LB_crash_padding = vessel_cross_center_to_vessel_bottom_flange + vessel_cross_center_to_actuator_bottom_flange - assembly_dim + LB_pos

# check that we can remove the assembly from the beam pipe
# distance between center of the chamber and the bottom of the frame assembly when at SA (should be at least 125 to clear beam pipe)
SA_removal_padding = vessel_cross_center_to_actuator_bottom_flange - (assembly_dim - SA_pos)
if (SA_removal_padding < (beam_pipe_diameter/2)):
	print("ERROR: the top screen position doesn't fully remove the screen assembly from the beam pipe")
else:
	print("Looks good, we can remove the assembly from the pipe")

# check that the bottom stopper prevents the top bar from entering the beam pipe
top_bar_safety_padding = (vessel_cross_center_to_actuator_bottom_flange+BOTTOM_STOP_POS - (long_shaft_length+screen_holder_bar_width)) - (beam_pipe_diameter/2)
if (top_bar_safety_padding <= 0):
	print("ERROR: The top bar could enter the beam pipe")
else:
	print("Looks good, the top bar can never enter the pipe")

def printvars():
  tmp = globals().copy()
  [print(k,'  :  ', '{:.2f} [mm]'.format(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]
  with open("geom_calc_results.txt", "w") as results:
    [print(k,'  :  ', '{:0.2f} [mm]'.format(v), file=results) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

printvars()
print('Done!')
