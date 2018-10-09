
$fn=32*1;

inch = 25.4*1;

NAME=0*1;
BORE=1*1;
WRENCH=2*1;
NUT_THICKNESS=3*1;
JAM_THICKNESS=4*1;
WASHER_ID=5*1;
WASHER_OD=6*1;
WASHER_THICKNESS=7*1;
INFO = [
    ["#0",  1.524, 3.969, 1.191, 0.595, 1.661, 4.430, 0.354], 
    ["#1",  1.854, 3.969, 1.191, 0.595, 2.021, 5.390, 0.431], 
    ["#2",  2.184, 4.763, 1.588, 0.794, 2.381, 6.350, 0.508], 
    ["#3",  2.515, 4.763, 1.588, 0.794, 2.741, 7.310, 0.585], 
    ["#4",  2.845, 6.350, 2.381, 1.191, 3.175, 7.938, 0.813], 
    ["#6",  3.505, 7.938, 2.778, 1.389, 3.969, 9.525, 1.245], 
    ["#8",  4.166, 8.731, 3.175, 1.588, 4.763, 11.113, 1.245], 
    ["#10",  4.826, 9.525, 3.175, 1.588, 5.556, 12.700, 1.245], 
    ["#12",  5.486, 11.113, 3.969, 1.984, 6.350, 14.288, 1.651], 
    ["1/4\"",  6.350, 11.113, 5.556, 3.969, 7.938, 18.644, 1.651], 
    ["5/16\"",  7.938, 12.700, 6.747, 4.763, 9.525, 22.225, 2.108], 
    ["3/8\"",  9.525, 14.288, 8.334, 5.556, 11.113, 25.400, 2.108], 
    ["7/16\"",  11.113, 17.463, 9.525, 6.350, 12.700, 31.750, 2.108], 
    ["1/2\"",  12.700, 19.050, 11.113, 7.938, 14.288, 34.925, 2.769], 
    ["9/16\"",  14.288, 22.225, 12.303, 7.938, 15.875, 37.306, 2.769], 
    ["5/8\"",  15.875, 23.813, 13.891, 9.525, 17.463, 44.450, 3.404], 
    ["3/4\"",  19.050, 28.575, 16.272, 10.716, 20.638, 50.800, 3.759], 
    ["7/8\"",  22.225, 33.338, 19.050, 12.303, 23.813, 57.150, 4.191], 
    ["1\"",  25.400, 38.100, 21.828, 13.891, 26.988, 63.500, 4.191], 
    ["2mm",  2.000, 4.000, 1.600, 1.200, 2.270, 4.850, 0.300], 
    ["2.5mm",  2.500, 5.000, 2.000, 1.600, 2.770, 5.850, 0.500], 
    ["3mm",  3.000, 5.500, 2.400, 1.800, 3.290, 6.820, 0.500], 
    ["4mm",  4.000, 7.000, 3.200, 2.200, 4.390, 8.820, 0.800], 
    ["5mm",  5.000, 8.000, 4.000, 2.700, 5.390, 9.820, 1.000], 
    ["6mm",  6.000, 10.000, 5.000, 3.200, 6.510, 11.785, 1.600], 
    ["7mm",  7.000, 11.000, 5.500, 3.500, 7.510, 13.785, 1.600], 
    ["8mm",  8.000, 13.000, 6.500, 4.000, 8.510, 15.785, 1.600], 
    ["10mm",  10.000, 17.000, 8.000, 5.000, 10.635, 19.740, 2.000], 
    ["12mm",  12.000, 19.000, 10.000, 6.000, 13.135, 23.740, 2.500], 
    ["14mm",  14.000, 22.000, 11.000, 7.000, 15.135, 27.740, 2.500], 
    ["16mm",  16.000, 24.000, 13.000, 8.000, 17.135, 29.740, 3.000], 
    ["18mm",  18.000, 27.000, 15.000, 9.000, 19.150, 33.215, 3.000], 
    ["20mm",  20.000, 30.000, 16.000, 10.000, 21.165, 36.690, 3.000], 
];

// ---------------------------------------------------
/* [Global] */

// Which part to show?
part="none"; // [ALL,Hex nut, Jam nut, Cap nut, Thumb nut, Square nut, Wing nut, Coupling nut, Lock washer, Small washer, Standard washer, Fender washer, Dowel pin]

// ---------------------------------------------------
/* [Size] */

// Select the nominal diameter of the bolt/pin
size = 26; // [0:#0, 1:#1, 2:#2, 3:#3, 4:#4, 5:#6, 6:#8, 7:#10, 8:#12, 9:1/4", 10:5/16", 11:3/8", 12:7/16", 13:1/2", 14:9/16", 15:5/8", 16:3/4", 17:7/8", 18:1", 19:2mm, 20:2.5mm, 21:3mm, 22:4mm, 23:5mm, 24:6mm, 25:7mm, 26:8mm, 27:10mm, 28:12mm, 29:14mm, 30:16mm, 31:18mm, 32:20mm]

echo("Name: ",INFO[size][NAME],"Maj dia: ",INFO[size][BORE], "Wrench:",INFO[size][WRENCH],"Part:",part);

// ---------------------------------------------------
/* [Tolerances] */

// Shrink the nut by this diameter to make it fit easily into a wrench. You may want to tune this to your printer. (mm)
nut_tolerance = 0.3;

// Grow the bore by this diameter. This can depend on the printer and plastic being used, so adjust it so that screws cut good threads into the nuts. If nut is too loose, reduce this, if nuts are too tight or break, increase. (mm)
bore_tolerance = -0.1;

// Shrink the dowel pin by this diameter so that it slots relatively easily into the hole. (mm)
pin_tolerance = 0.4;

// --------------------------------------------------
/* [Part details] */
// Length of the dowel pin (mm)
dowel_pin_length = 25;

// Percentage of the dowel pin's surface to bevel?
dowel_pin_bevel_percent = 10; // [0:100]
dowel_pin_bevel = dowel_pin_bevel_percent/100;

// Diameter of each individual nurl on the thumb nut? (mm)
nurl_dia = 1.5;

// Gap between individual nurls on the thumb nut? (mm)
nurl_gap = 0.5;

// Fraction of the thumb nut to apply nurling to
nurl_coverage_percent = 80; // [0:100]
nurl_coverage = nurl_coverage_percent/100;

// Adjust the wingnut wing length by this percentage
wing_span_adjust_percent = 50; //[0:100]
wing_span_adjust=1 + wing_span_adjust_percent/100;

// Number of teeth for the lock washer
lock_teeth = 10; // [5:16]

// Chooses how long each lock tooth is.
lock_tooth_fill_percent = 100; // [50:100]
lock_tooth_ratio = lock_tooth_fill_percent/100;

// ---------------------------------------------------
/* [Overrides] */

// Override the nominal diameter of the bolt/pin? (mm)
diameter_override = "";

// Override the wrench size for nuts? (mm)
wrench_size_override = "";

// Override the nut thickness? (mm)
nut_thickness_override = 0;

// Override the jam nut thickness? (mm)
jam_nut_thickness_override = 0;

// Override the washer inner diameter? (mm)
washer_inner_diameter_override = 0;

// Override the washer standard outer diameter? (mm)
washer_outer_diameter_override = 0;

// Override the washer thickness? (mm)
washer_thickness_override = 0;

// Override the length of the coupling nut? (mm)
coupling_nut_length_override = 0;

// Override the thickness of the lock washer teeth? (mm)
lock_tooth_thickness_override = 0;


// -------------- hidden settings --------------------
nut_edge_rounding = 0.97*1; // shave a little off the hex edges to make it easier to wrench, 1=no rounding, 0.92=almost fully round, 0.98=reasonable

min_wing_thickness = 1*1; // mm


// ------------- computed sizes -------------------

wrench_size = wrench_size_override ? wrench_size_override-nut_tolerance : INFO[size][WRENCH]-nut_tolerance;

wrench_od = hex_wrench_size_to_dia(wrench_size);

major_diameter = diameter_override ? diameter_override : INFO[size][BORE];

bore_diameter = major_diameter + bore_tolerance;

pin_diameter = major_diameter - pin_tolerance;

nut_thickness = nut_thickness_override ? nut_thickness_override : INFO[size][NUT_THICKNESS];

jam_nut_thickness = jam_nut_thickness_override ? jam_nut_thickness_override : INFO[size][JAM_THICKNESS];

washer_inner_diameter = washer_inner_diameter_override ? washer_inner_diameter_override : INFO[size][WASHER_ID];

washer_outer_diameter = washer_outer_diameter_override ? washer_outer_diameter_override : INFO[size][WASHER_OD];

washer_thickness = washer_thickness_override ? washer_thickness_override : INFO[size][WASHER_THICKNESS];

lock_tooth_thickness = lock_tooth_thickness_override ? lock_tooth_thickness_override : max(0.5,washer_thickness/2);

wing_thickness = max(min_wing_thickness,washer_thickness);

wing_round_radius = min(major_diameter, nut_thickness * 0.5);

coupling_nut_length = coupling_nut_length_override ? coupling_nut_length_override : major_diameter*3;

fender_washer_outer_diameter = wrench_od*2.5;

small_washer_outer_diameter = wrench_od*0.95;



// for hex forms, convert from flats-distance (wrench size) to points-distance (diameter)
function hex_wrench_size_to_dia(w) = w * (2/sqrt(3));
function hex_dia_to_wrench_size(w) = w / (2/sqrt(3));

dx = wrench_od*1.5;
dy = wrench_od*2;

module hex3d(wrench_size, diameter, thickness) {
    linear_extrude(thickness) hex2d(wrench_size,diameter);
}

module hex2d(wrench_size, diameter) {
    difference() {
        intersection() {
            circle(d=wrench_od, $fn=6, center=true);
            circle(d=wrench_od*nut_edge_rounding);
        }
        circle(d=diameter, center=true);
    }
}

module hex_nut() {
    hex3d(wrench_size, bore_diameter, nut_thickness);
}

module jam_nut() {
    hex3d(wrench_size, bore_diameter, jam_nut_thickness);
}

module square_nut() {
    linear_extrude(nut_thickness) difference() {
        intersection() {
            square(wrench_size, center=true);
            circle(d=2/sqrt(2)*wrench_size*nut_edge_rounding);
        }
        circle(d=bore_diameter, center=true);
    }
}

module washer(wrench_od) {
    linear_extrude(washer_thickness) difference() {
        circle(d=wrench_od, center=true);
        circle(d=washer_inner_diameter, center=true);
    }
}

module small_washer() { washer(small_washer_outer_diameter); }
module standard_washer() { washer(washer_outer_diameter); }
module fender_washer() { washer(fender_washer_outer_diameter); }

module coupling_nut() {
    hex3d(wrench_size, bore_diameter, coupling_nut_length);
}

module cap_nut() {
    translate([0,0,nut_thickness]) {
        difference() {
            sphere(d=wrench_size);
            sphere(d=bore_diameter);
            translate([-wrench_size/2,-wrench_size/2,-wrench_size/2])
                cube([wrench_size,wrench_size,wrench_size/2]);
        }
    }
    hex3d(wrench_size, bore_diameter, nut_thickness);
}

module dowel_pin() {
    beveled_cylinder(d=pin_diameter, h=dowel_pin_length, bevel=dowel_pin_bevel);
}

module wing_nut() {
    difference() {
        union() {
            cylinder(d=wrench_od,h=nut_thickness);
            for (m = [0,1]) {
                mirror([0,m,0]) 
                    translate([0,wrench_od/2,0]) 
                    rotate([0,-90,0]) 
                    translate([0,0,-wing_thickness/2])
                    linear_extrude(wing_thickness) 
                    offset(wing_round_radius)
                    offset(-wing_round_radius)
                    polygon([
                        [0,-(wrench_od-major_diameter)/2],
                        [0,wrench_od/2*0.6*wing_span_adjust],
                        [nut_thickness,wrench_od/2*0.9*wing_span_adjust],
                        [nut_thickness*1.5,wrench_od/4*wing_span_adjust],
                        [nut_thickness,-(wrench_od-major_diameter)/2*0.75],
                    ]);
            }
        }
        translate([0,0,-10]) cylinder(d=bore_diameter,h=nut_thickness+20);
    }
}

module beveled_cylinder(d=0,h,d1=false,d2=false, center=false, bevel=0.05) {
    d1 = d1 ? d1 : (d ? d : 0.01);
    d2 = d2 ? d2 : (d ? d : 0.01);
    bd1 = d1 * (1-bevel); // bevel cylinder 1 smaller dia
    bd2 = d2 * (1-bevel); // bevel cylinder 2 smaller dia
    bh1 = (d1-bd1)/2;  // bevel cylinder 1 height
    bh2 = (d2-bd2)/2;  // bevel cylinder 2 height
    translate([0,0,center?-h/2:0]) {
        cylinder(d1=bd1, d2=d1, h=bh1);
        translate([0,0,bh1])
            cylinder(d1=d1,d2=d2, h=h-bh1-bh2);
        translate([0,0,h-bh2])
            cylinder(d2=bd2, d1=d2, h=bh2);
    }
}

module rounded_cylinder(d=0,h,d1=false,d2=false) {
    d1 = d1 ? d1 : (d ? d : 0.01);
    d2 = d2 ? d2 : (d ? d : 0.01);
    hull() {
        translate([0,0,d1/2]) sphere(d=d1);
        translate([0,0,h-d2/2]) sphere(d=d2);
    }
}

module thumb_nut() {
    difference() {
        union() {
            //md = (wrench_size + wrench_size)/2;
            nurls = floor((PI*wrench_size)/(nurl_dia+nurl_gap));
            cylinder(d=wrench_size, h=nut_thickness);
            for (i = [0:nurls-1]) {
                theta = 360/nurls*i;
                translate([wrench_size/2*cos(theta),wrench_size/2*sin(theta),0])
                    beveled_cylinder(d1=nurl_dia, d2=nurl_dia, h=nut_thickness*nurl_coverage, $fn=$fn/2, bevel=0.15);
            }
        }
        translate([0,0,-1]) cylinder(d=bore_diameter, h=nut_thickness+2);
    }
}

module tooth_lock_washer() {
    md = (wrench_size+major_diameter)/2;
    lock_tooth_cadence = PI*wrench_size / lock_teeth;
    lock_tooth_size = lock_tooth_cadence * lock_tooth_ratio;
    difference() {
        union() {
            cylinder(d=wrench_od, h=washer_thickness);
            intersection() {
                cylinder(d=wrench_od, h=washer_thickness+lock_tooth_thickness+1);
                for (i = [0:lock_teeth-1]) {
                    theta = 360/lock_teeth*i;
                    rotate([0,0,theta])
                        translate([0,-lock_tooth_size/2,0])
                        rotate([0,0,90])
                        rotate([90,0,0])
                        linear_extrude(wrench_od/2)
                        polygon([
                            [0,0],
                            [0,washer_thickness+lock_tooth_thickness],
                            [lock_tooth_size,washer_thickness],
                            [lock_tooth_size,0],
                        ]);
                }
            }
        }
        translate([0,0,-10]) cylinder(d=washer_inner_diameter, h=washer_thickness+20);
    }
}

if (major_diameter >= wrench_size-0.5) {
    linear_extrude(2) text("Error: inner size > outer size.");
} else {
    if (part==-1 || part=="ALL") {
        translate([ 0*dx,0*dy,0]) hex_nut();
        translate([ 1*dx,0*dy,0]) jam_nut();
        translate([ 2*dx,0*dy,0]) cap_nut();
        translate([ 3*dx,0*dy,0]) thumb_nut();
        translate([ 4*dx,0*dy,0]) square_nut();
        translate([ 5*dx,0*dy,0]) wing_nut();
        translate([ 6*dx,0*dy,0]) coupling_nut();
        translate([ 0*dx,1*dy,0]) tooth_lock_washer();
        translate([ 1*dx,1*dy,0]) small_washer();
        translate([ 2*dx,1*dy,0]) standard_washer();
        translate([ 3.5*dx,1*dy,0]) fender_washer();
        //translate([ 5*dx,1*dy,0]) dowel_pin();
    } else if (part==-2 || part=="TESTSOME") {
        translate([ 0*dx,0*dy,0]) hex_nut();
        translate([ 1*dx,0*dy,0]) thumb_nut();
        translate([ 2*dx,0*dy,0]) wing_nut();
        translate([ 3*dx,0*dy,0]) dowel_pin();
        translate([ 0*dx,1*dy,0]) tooth_lock_washer();
        translate([ 1*dx,1*dy,0]) small_washer();
        translate([ 2*dx,1*dy,0]) standard_washer();
    }
    else if (part == 0 || part=="Hex nut") { hex_nut(); }
    else if (part == 1 || part=="Jam nut") { jam_nut(); }
    else if (part == 2 || part=="Cap nut") { cap_nut(); }
    else if (part == 3 || part=="Thumb nut") { thumb_nut(); }
    else if (part == 4 || part=="Square nut") { square_nut(); }
    else if (part == 5 || part=="Wing nut") { wing_nut(); }
    else if (part == 6 || part=="Coupling nut") { coupling_nut(); }
    else if (part == 7 || part=="Lock washer") { tooth_lock_washer(); }
    else if (part == 8 || part=="Small washer") { small_washer(); }
    else if (part == 9 || part=="Standard washer") { standard_washer(); }
    else if (part ==10 || part=="Fender washer") { fender_washer(); }
    else if (part ==11 || part=="Dowel pin") { dowel_pin(); }
}

    


