include <assembly.scad>
include <threads.scad>


translate([0,0,long_rod_length]) metric_thread (diameter=5, pitch=0.8, length=8);
assembly();