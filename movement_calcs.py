#!/usr/bin/env python3

# assuming UHV actuator part# HLSML64-600-H
# all units in mm

# if True, the crossbar will be a 5mm thick plate
use_thinner_crossbar = False

actuator_travel = 600  # maximum possible travel of actuator
actuator_flange_spacing_min = 260  # minimum possible distance from top of moving flange to bottom of stationary one
acutator_flange_spacing_max = actuator_flange_spacing_min + actuator_travel

# we'll install the lower physical travel hard stop this far away from the most contracted position
bottom_end_stop_padding = 50


# the distance between the center of the chamber and the bottom of the non-moving flange of the actuator 
vessel_cross_center_to_actuator_bottom_flange = 685.05

# distance between the center of the chamber and the bottom flange surface
vessel_cross_center_to_vessel_bottom_flange = 464.42

# the minimum distance between the bottom edge of the stationary acutator flange and the top of the sample holder crossbar
# such that the cross bar can't crash into the top of the chamber when the moving flange is at its highest point
# and so the beam does not roll off the rollers
required_top_clearance = 61.83

beam_pipe_diameter = 250
view_diameter = 220

# vertical dimension of the top horizontal screen holder bar (aka the bar's cross-sectional, width=height)
if use_thinner_crossbar:
  crossbar_height = 5
else:
  crossbar_height = 25
square_crosssection = 25

# vertical spacing between the bottom edge of the top screen and the top edge of the bottom screen
screen_screen_spacing = 0

# vertical distance between the top edge of the screen and the bottom surface of the long vertical shaft
#top_screen_long_shaft_spacing = crossbar_height + top_screen_holder_spacing

# dimension of the screen
screen_dim_y = 230
screen_dim_x = 290

# offset of left edge of switch bracket
#switch_bracket_offset = 179.75

# when we're at SB (bottom screen in beam) the beam center will be this many mm above the center of the screen (going to be positive)
# must be on [-5,5] so that the screen stays in the viewing area
bottom_screen_beam_center_vertical_offset = 0
#bottom_screen_beam_center_vertical_offset = 5

# when we're at SC (top screen in beam) the beam center will be this many mm above the center of the screen (going to be negative)
top_screen_beam_center_vertical_offset = -5

# amount of buffer we'll move the top stopper down from its absolute maximum value
top_stopper_buffer = 1

if use_thinner_crossbar:
  minimum_switch_switch_spacing = 11.36  # smallest possible spacing between limit/position switches
else:
  minimum_switch_switch_spacing = 1
minimum_switch_stopper_spacing = 1 # smallest possible spacing between limit switches and end stops

# vertical spacing between the bottom face of the horizontal screen holder bar and the top edge of the top screen
#top_screen_holder_spacing = 17.36
top_screen_holder_spacing = top_screen_beam_center_vertical_offset + (beam_pipe_diameter-screen_dim_y)/2 + minimum_switch_stopper_spacing + minimum_switch_switch_spacing

# this is the most travel we'll ever posibly be able to get because anything more will mean cross bar crash into top flange or cross bar enters beam pipe
maximum_stopper_spacing = vessel_cross_center_to_actuator_bottom_flange - beam_pipe_diameter/2 - required_top_clearance - crossbar_height

# anything higher than this would fail the maximum_stopper_spacing requirement
absolute_highest_position_for_top_stopper = actuator_flange_spacing_min + maximum_stopper_spacing + bottom_end_stop_padding

# length of the long vertical shaft in the screen holder frame
long_shaft_length = vessel_cross_center_to_actuator_bottom_flange - crossbar_height - screen_dim_y/2 + actuator_flange_spacing_min + bottom_end_stop_padding - top_screen_holder_spacing + minimum_switch_switch_spacing + minimum_switch_stopper_spacing + top_screen_beam_center_vertical_offset

crossbar_shaft_length = beam_pipe_diameter+2*square_crosssection
side_shaft_lengths = 2 * screen_dim_y + screen_screen_spacing + top_screen_holder_spacing

# total frame holder assembly vertical dimension
assembly_dim = long_shaft_length + side_shaft_lengths + crossbar_height

# long shaft length reduction for L-Bracket swinger
l_bracket_length_reduction = 10

no_crossbar_total_length = 2*side_shaft_lengths + long_shaft_length - l_bracket_length_reduction
crossbar_total_length = 2*side_shaft_lengths + long_shaft_length + crossbar_shaft_length - l_bracket_length_reduction

if use_thinner_crossbar:
  print(f'Total strut length = {no_crossbar_total_length}mm:')
  print(f'That is 2x {side_shaft_lengths}mm')
  print(f'And 1x {long_shaft_length-l_bracket_length_reduction}mm')
else:
  print(f'Total strut length = {crossbar_total_length}mm:')
  print(f'That is 2x {side_shaft_lengths}mm')
  print(f'And 1x {long_shaft_length-l_bracket_length_reduction}mm')
  print(f'And 1x {crossbar_shaft_length}mm')


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


BOTTOM_STOP_POS = actuator_flange_spacing_min + bottom_end_stop_padding # location to install the bottom movement stopper
LB_pos = BOTTOM_STOP_POS + minimum_switch_stopper_spacing  # prevents hitting the bottom stopper

TOP_STOP_POS = absolute_highest_position_for_top_stopper - top_stopper_buffer # location to install the top movement stopper 
LT_pos = TOP_STOP_POS - minimum_switch_stopper_spacing  # prevents hitting the top stopper

# valid screens removed position
SA_pos = LT_pos - minimum_switch_switch_spacing

# valid bottom screen in beam position
SB_pos = assembly_dim - vessel_cross_center_to_actuator_bottom_flange - screen_dim_y/2 - bottom_screen_beam_center_vertical_offset

# valid top screen in beam position
SC_pos = LB_pos + minimum_switch_switch_spacing
#SC_pos = assembly_dim - vessel_cross_center_to_actuator_bottom_flange - screen_dim_y - screen_screen_spacing - screen_dim_y/2 - top_screen_beam_center_vertical_offset

#SB_pos = 1.5 * screen_dim_y + screen_screen_spacing + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange  
#SC_pos = 0.5 * screen_dim_y + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange # top screen centered in beam
#LB_pos = BOTTOM_STOP_POS + minimum_switch_switch_spacing  # no reason to allow for pushing the screens in further than a few mm past SC
#BOTTOM_STOP_POS = actuator_flange_spacing_min + end_stop_padding # location to install the bottom movement stopper

# check that everything is within the travel limits of the actuator
# highest_thing = max([TOP_STOP_pos, LT_pos, SA_pos, SB_pos, SC_pos, LB_pos, BOTTOM_STOP_POS])
# lowest_thing = min([TOP_STOP_pos, LT_pos, SA_pos, SB_pos, SC_pos, LB_pos, BOTTOM_STOP_POS])
# if ( ((highest_thing<=acutator_flange_spacing_max)and(highest_thing>=actuator_flange_spacing_min)) and ((lowest_thing<=acutator_flange_spacing_max)and(lowest_thing>=actuator_flange_spacing_min)) ):
# 	print("Looks good, everything is within the mover's travel limits")
# else:
# 	print("ERROR: Something is not within the mover's travel limits")

# check that BOTTOM_STOP_POS prevents bottom crashing
bottom_padding = vessel_cross_center_to_vessel_bottom_flange - ((vessel_cross_center_to_actuator_bottom_flange + BOTTOM_STOP_POS) - assembly_dim )
if bottom_padding <= 0:
	print("ERROR: Assembly can crash into the bottom of the vessel")
else:
	print("Looks good, the assembly can't crash into the bottom of the vessel.")

# check that the stoppers are the right distance apart
requested_stopper_spacing = TOP_STOP_POS - BOTTOM_STOP_POS
if requested_stopper_spacing > maximum_stopper_spacing:
	print("ERROR: We can't possibly be allowed to travel this far!")
else:
	print("Looks good, we're not asking for too much travel.")

# check that at SA (screens removed) position, the screen is out of the beam pipe
# distance between the bottom edge of the bottom screen and the top edge of the beam pipe of the chamber and the bottom of the frame assembly when at SA (should be at least 125 to clear beam pipe)
SA_removal_padding = vessel_cross_center_to_actuator_bottom_flange - (assembly_dim - SA_pos) - beam_pipe_diameter/2
if (SA_removal_padding <= 0):
	print("ERROR: the top screen position doesn't fully remove the screen assembly from the beam pipe")
else:
	print("Looks good, we can remove the assembly from the pipe")

# check that if we hit the bottom stop, the crossbar is out of the beam pipe
cross_bar_beam_pipe_padding = (vessel_cross_center_to_actuator_bottom_flange + BOTTOM_STOP_POS - (long_shaft_length+crossbar_height)) - (beam_pipe_diameter/2)
if (cross_bar_beam_pipe_padding < 0):
	print("ERROR: The top bar could enter the beam pipe")
else:
	print("Looks good, the top bar can never enter the pipe")

# check that if we hit the top stop, the bar doesn't roll off the rollers
roll_off_padding = (vessel_cross_center_to_actuator_bottom_flange + BOTTOM_STOP_POS - (long_shaft_length+crossbar_height)) - (beam_pipe_diameter/2)
if (roll_off_padding < 0):
	print("ERROR: The shaft might roll off the rollers")
else:
	print("Looks good, the shaft can't roll off the rollers")


# check that the order of the switches is proper and within limits
_must_be_increasing = [actuator_flange_spacing_min, BOTTOM_STOP_POS, LB_pos, SC_pos, SB_pos, SA_pos, LT_pos, TOP_STOP_POS, acutator_flange_spacing_max]
#_bracket_gap_check = [x- +  for x in _must_be_increasing ]
if (all(i <= j for i, j in zip(_must_be_increasing, _must_be_increasing[1:]))):
	print("Looks good: all switches in order and within limits")
else:
	print("ERROR: Something is out of order or beyond limits!")


def printvars():
  tmp = globals().copy()
  [print(k,'  :  ', '{:.2f} [mm]'.format(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]
  with open("geom_calc_results.txt", "w") as results:
    [print(k,'  :  ', '{:0.2f} [mm]'.format(v), file=results) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

printvars()
print(f'Must be increasing: {_must_be_increasing}')
#print(f'Switch bracket coordinates: {_bracket_gap_check}')
print('Done!')

# output for use_thinner_crossbar = False:
"""
Total strut length = 2069.05mm:
That is 2x 467.0mm
And 1x 835.05mm
And 1x 300mm
Looks good, the assembly can't crash into the bottom of the vessel.
Looks good, we're not asking for too much travel.
Looks good, we can remove the assembly from the pipe
Looks good, the top bar can never enter the pipe
Looks good, the shaft can't roll off the rollers
Looks good: all switches in order and within limits
use_thinner_crossbar   :   0.00 [mm]
actuator_travel   :   600.00 [mm]
actuator_flange_spacing_min   :   260.00 [mm]
acutator_flange_spacing_max   :   860.00 [mm]
bottom_end_stop_padding   :   50.00 [mm]
vessel_cross_center_to_actuator_bottom_flange   :   685.05 [mm]
vessel_cross_center_to_vessel_bottom_flange   :   464.42 [mm]
required_top_clearance   :   61.83 [mm]
beam_pipe_diameter   :   250.00 [mm]
view_diameter   :   220.00 [mm]
crossbar_height   :   25.00 [mm]
square_crosssection   :   25.00 [mm]
screen_screen_spacing   :   0.00 [mm]
screen_dim_y   :   230.00 [mm]
screen_dim_x   :   290.00 [mm]
bottom_screen_beam_center_vertical_offset   :   0.00 [mm]
top_screen_beam_center_vertical_offset   :   -5.00 [mm]
top_stopper_buffer   :   1.00 [mm]
minimum_switch_switch_spacing   :   1.00 [mm]
minimum_switch_stopper_spacing   :   1.00 [mm]
top_screen_holder_spacing   :   7.00 [mm]
maximum_stopper_spacing   :   473.22 [mm]
absolute_highest_position_for_top_stopper   :   783.22 [mm]
long_shaft_length   :   845.05 [mm]
crossbar_shaft_length   :   300.00 [mm]
side_shaft_lengths   :   467.00 [mm]
assembly_dim   :   1337.05 [mm]
l_bracket_length_reduction   :   10.00 [mm]
no_crossbar_total_length   :   1769.05 [mm]
crossbar_total_length   :   2069.05 [mm]
BOTTOM_STOP_POS   :   310.00 [mm]
LB_pos   :   311.00 [mm]
TOP_STOP_POS   :   782.22 [mm]
LT_pos   :   781.22 [mm]
SA_pos   :   780.22 [mm]
SB_pos   :   537.00 [mm]
SC_pos   :   312.00 [mm]
bottom_padding   :   806.42 [mm]
requested_stopper_spacing   :   472.22 [mm]
SA_removal_padding   :   3.22 [mm]
cross_bar_beam_pipe_padding   :   0.00 [mm]
roll_off_padding   :   0.00 [mm]
Must be increasing: [260, 310, 311, 312, 537.0, 780.22, 781.22, 782.22, 860]
Done!
"""