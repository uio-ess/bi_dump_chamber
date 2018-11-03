#!/usr/bin/env python3

# assuming UHV actuator part# HLSML64-600-H
# all units in mm

actuator_travel = 600 # maximum possible travel of actuator
actuator_flange_spacing_min = 260 # minimum possible distance from top of moving flange to bottom of stationary one
acutator_flange_spacing_max = actuator_flange_spacing_min + actuator_travel

# the distance between the center of the chamber and the bottom of the non-moving flange of the actuator 
vessel_cross_center_to_actuator_bottom_flange = 682.45

# the minimum distance between the bottom edge of the stationary acutator flange and the top of the sample holder crossbar
# such that the cross bar can't crash into the top of the chamber when the moving flange is at its highest point
required_top_clearance = 55

# length of the long vertical shaft in the screen holder frame
long_shaft_length = acutator_flange_spacing_max + required_top_clearance

# vertical dimension of the top horizontal screen holder bar
screen_holder_bar_width = 20

# vertical spacing between the horizontal screen holder bar and the top edge of the top screen
top_screen_holder_spacing = 5

# vertical spacing between the bottom edge of the top screen and the top edge of the bottom screen
screen_screen_spacing = 5

# vertical distance between the top edge of the screen and the bottom surface of the long vertical shaft
top_screen_long_shaft_spacing = screen_holder_bar_width + top_screen_holder_spacing

# dimension of the screen (both x and y)
screen_dim = 230

crossbar_shaft_width = screen_dim-2*screen_holder_bar_width
side_shaft_lengths = top_screen_long_shaft_spacing + 2 * screen_dim + screen_screen_spacing

# total frame holder assembly vertical dimension
assembly_dim = long_shaft_length + side_shaft_lengths

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
# defined as switch instillation position such that the distance between the midpoint of the switch
# hysteresis occurs when the the bottom of the stationary flange is this many mm away from the top of the moving flange
# must be on the interval [fully withdrawn, fully inserted] = [860,260]

minimum_switch_switch_spacing = 5  # smallest possible spacing between limit/position switches

LT_pos = 855  # just some number to prevent the actuator from crashing into its self at the end of travel
SA_pos = LT_pos - minimum_switch_switch_spacing  # the screens are now very close to as far away from the beam as we can possibly get them
SB_pos = 1.5 * screen_dim + screen_screen_spacing + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange  # bottom screen centered in beam
SC_pos = 0.5 * screen_dim + top_screen_long_shaft_spacing + long_shaft_length - vessel_cross_center_to_actuator_bottom_flange # top screen centered in beam
LB_pos = SC_pos - 20  # no reason to allow for pushing the screens in further than a few mm past SC

# distance between the center of the chamber and the bottom flange surface
vessel_cross_center_to_vessel_bottom_flange = 463.25

# distance between the bottom of the frame assembly and bottom flange surface when at LB (must be > 0 to avoid crash into bottom of chamber)
LB_crash_padding = vessel_cross_center_to_vessel_bottom_flange + vessel_cross_center_to_actuator_bottom_flange - assembly_dim + LB_pos

# distance between center of the chamber and the bottom of the frame assembly when at SA (should be at least 125 to clear beam pipe)
SA_removal_padding = vessel_cross_center_to_actuator_bottom_flange - (assembly_dim - SA_pos)

def printvars():
  tmp = globals().copy()
  [print(k,'  :  ', '{:.2f} [mm]'.format(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]
  with open("geom_calc_results.txt", "w") as results:
    [print(k,'  :  ', '{:0.2f} [mm]'.format(v), file=results) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

printvars()
print('Done!')