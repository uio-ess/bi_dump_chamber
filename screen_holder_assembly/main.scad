//include <threads.scad>
//include <everynut/everynut.scad>
include <al_strut.scad>

screenX = 230;
screenY = 230;
screenT = 1;

// all dims in mm
spacing_between_screens = 10;

top_bar_spacing = 10;

strut_square = 20;

mover_flange_to_top_of_frame = 920;

crossbar_width = screenX-2*strut_square;
echo(crossbar_width);

sidebar_length = spacing_between_screens+2*screenY + strut_square + top_bar_spacing;
echo(sidebar_length);

screen_mount_hole_diameter = 5;

screen_mount_hole_offset = strut_square/2;

extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=mover_flange_to_top_of_frame);

translate([-crossbar_width/2,0,-strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);

translate([screenX/2-strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);
translate([-screenX/2+strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);

%translate([-crossbar_width/2,0,-sidebar_length+strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);

#translate([-screenX/2,strut_square/2,-screenY-strut_square-top_bar_spacing]) difference(){
    cube([screenX, screenT,screenY], center=false);
    rotate([90,0,0]) translate ([screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
}

#translate([-screenX/2,strut_square/2,-2*screenY-strut_square-spacing_between_screens-top_bar_spacing]) difference(){
    cube([screenX, screenT,screenY], center=false);
    rotate([90,0,0]) translate ([screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
    rotate([90,0,0]) translate ([screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
}
