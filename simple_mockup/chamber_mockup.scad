flangeT=23; // thickness of flange
flangeExtra = 45; //extra diameter of flange beyond inner diameter

pipeWallT = 4.78;

pipeInnerD = 250;
pipeWallT = 4.78;
pipeOuterD = pipeWallT + pipeInnerD;

//topPipeInnerD = 450;
topPipeInnerD = 350;
topPipeOuterD = topPipeInnerD + pipeWallT;

subtractFudge = 2;

module drawChamber ( botPipeL=460, topPipeL=630, upstreamPipeL=400, downstreamPipeL=300, viewPipeL=380, viewPortZAngle=-135 ) {
    difference(){
        union(){
            //vert Pipe
            translate([0,0,-botPipeL]) union(){
                cylinder(h=flangeT, d=topPipeInnerD+flangeExtra); //bot flange
                cylinder(h=botPipeL+topPipeL, d=topPipeOuterD); //vert pipe
                translate([0,0,botPipeL+topPipeL-flangeT]) cylinder(h=flangeT, d=topPipeInnerD+flangeExtra); //top flange
            }
            //horz pipe
            rotate([0,-90,0]) translate([0,0,-downstreamPipeL]) union(){
                cylinder(h=flangeT, d=pipeInnerD + flangeExtra); //downstream flange
                cylinder(h=downstreamPipeL+upstreamPipeL, d=pipeOuterD); //horz pipe
                translate([0,0,downstreamPipeL+upstreamPipeL-flangeT]) cylinder(h=flangeT, d=pipeInnerD + flangeExtra); //upstream flange
            }
            //view pipe
            rotate([-90,0,viewPortZAngle+90]) translate([0,0,-viewPipeL]) union(){
                cylinder(h=flangeT, d=pipeInnerD + flangeExtra); //view flange
                cylinder(h=viewPipeL, d=pipeOuterD); //vert pipe
            }
        }
        rotate([0,-90,0]) translate([0,0,-downstreamPipeL-subtractFudge/2]) cylinder(h=downstreamPipeL+upstreamPipeL+subtractFudge, d=pipeOuterD-2*pipeWallT); // inner horz pipe
        translate([0,0,-botPipeL-subtractFudge/2]) cylinder(h=botPipeL+topPipeL+subtractFudge, d=topPipeOuterD-2*pipeWallT); //inner vert pipe
        rotate([-90,0,viewPortZAngle+90]) translate([0,0,-viewPipeL-subtractFudge/2]) cylinder(h=viewPipeL+subtractFudge, d=pipeOuterD-2*pipeWallT); //inner view pipe
    }
}


