// written by grey@christoforo.net
include <al_strut.scad>
include <threads.scad>

// all dims in mm

screenX = 320;
screenY = 230;
screenT = 1.5;

view_ellipse_Z = 220;
view_ellipse_XY = 306;

spacing_between_screens = 5;

top_bar_spacing = 5;

strut_square = 20;

long_rod_length = 915;

crossbar_width = screenX-2*strut_square;
//echo(crossbar_width);

sidebar_length = spacing_between_screens+2*screenY + strut_square + top_bar_spacing;
//echo(sidebar_length);

screen_mount_hole_diameter = 5;

screen_mount_hole_offset = strut_square/2;

//3cm of m5 threads
//5cm of smooth
// 6cm piece with vent hole at 2cm
module mount_piece(){
    length = 60;
    offset = 30;
    difference(){
        translate([0,0,-offset]) metric_thread (diameter=5, pitch=0.8, length=length);
        cylinder(h=offset,d=2);
        rotate([90,0,0]) cylinder(h=offset,d=2);

    }
}


module view_ellipse(){
        color([0,1,0]) translate([screenX/2, screenT, screenY/2]) rotate([90, 0 ,0]) scale([view_ellipse_XY, view_ellipse_Z]) circle(d=1);
}

// draws the whole assembly
module assembly(){
    extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=long_rod_length);
    
    translate([-crossbar_width/2,0,-strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);
    
    translate([screenX/2-strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);
    translate([-screenX/2+strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);
    
    //%translate([-crossbar_width/2,0,-sidebar_length+strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);
    
    translate([-screenX/2,strut_square/2,-screenY-strut_square-top_bar_spacing]){
        view_ellipse();
        #difference(){
            cube([screenX, screenT, screenY], center=false);
            rotate([90,0,0]) translate ([screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
        }
    }
    
    translate([-screenX/2,strut_square/2,-2*screenY-strut_square-spacing_between_screens-top_bar_spacing]){
        view_ellipse();
        #difference(){
            cube([screenX, screenT,screenY], center=false);
            rotate([90,0,0]) translate ([screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screenX-screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
            rotate([90,0,0]) translate ([screen_mount_hole_offset,screenY-screen_mount_hole_offset,0]) cylinder(h=screenT*2.2, d=screen_mount_hole_diameter, center=true);
        }
    }
    translate([0,0,long_rod_length]) mount_piece();
}


mount_piece();