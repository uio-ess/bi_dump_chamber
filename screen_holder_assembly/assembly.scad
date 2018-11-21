// written by grey@christoforo.net
include <al_strut.scad>
include <threads.scad>

// all dims in mm

screenX = 320;
screenY = 230;
screenT = 1;

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

module mount_piece(){
    c_height = 50;
    difference(){
        union(){
            metric_thread (diameter=5, pitch=0.8, length=30);
            translate([0,0,-c_height]) cylinder(d=5,h=c_height);
        }
        translate([0,0,-20]) rotate_extrude() translate([5,0,0]) circle(3);
        cylinder(h=120,d=2,center=true);
    }
}

// draws the whole assembly
module assembly(){
    extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=long_rod_length);
    
    translate([-crossbar_width/2,0,-strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);
    
    translate([screenX/2-strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);
    translate([-screenX/2+strut_square/2,0,-sidebar_length]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=sidebar_length);
    
    //%translate([-crossbar_width/2,0,-sidebar_length+strut_square/2]) rotate([0,90,0]) extrusion_profile_20x20_v_slot_smooth(size=strut_square, height=crossbar_width);
    
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
    translate([0,0,long_rod_length]) mount_piece();
}


//mount_piece();