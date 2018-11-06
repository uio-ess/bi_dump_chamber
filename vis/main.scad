// written by grey@christoforo.net
// movies generated like this;
// ffmpeg -framerate 30 -pattern_type glob -i '*.png' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -pix_fmt yuv420p out2.mp4
include <../screen_holder_assembly/assembly.scad>
include <../simple_mockup/chamber_mockup.scad>

vessel_cross_center_to_actuator_bottom_flange = 682.45;

act_flange_D = 114;

// switch positions
LT_pos=860.00;
SA_pos=850.00;
SB_pos=607.55;
SC_pos=372.55;
LB_pos=352.55;


// draws the stuff that will move as a funciton of actuator flange spacing
module things_that_move(mover_position){
    translate([0,0,vessel_cross_center_to_actuator_bottom_flange+mover_position]) circle(d=act_flange_D);
    rotate([0,0,135]) translate([0,0,-long_rod_length+vessel_cross_center_to_actuator_bottom_flange+mover_position]) assembly();
}


// animation
min_actuator_position = LB_pos;
max_actuator_position = LT_pos;
actuator_position = LB_pos + $t*(LT_pos-LB_pos);
things_that_move (actuator_position);

// at top limit switch (should never be here, but this should be safe)
//things_that_move (LT_pos);

// at screen withdrawn position switch
//things_that_move (SA_pos);

// at bottom screen position switch
//things_that_move (SB_pos);

// at top screen position switch
//things_that_move (SC_pos);

// at bottom limit switch (should never be here, but this should be safe)
//things_that_move (LB_pos);

// draw chamber mockup
%drawChamber();

// mouning actuator flange (stationary)
translate([0,0,vessel_cross_center_to_actuator_bottom_flange]) circle(d=act_flange_D);