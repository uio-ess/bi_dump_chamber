#!/usr/bin/env python3

import logging
import pathlib
import cadquery as cq

# constants to define geometry, in mm
screen = {'dims': [290, 230, 1.5]}
screen['hole_spacing'] = [270, 210]
screen['hole_dia'] = 5.8

ext = {'dim': 25} # extrusion crosssection dimension

forks = {'length': 467}
forks['plane_down'] = 5 # amount of material to "plane down" from inner fork faces

shaft = {'length': 835.05}
shaft['swing_hole_offset'] = 12

crossbar = {'length': screen['hole_spacing'][0]+ext['dim']}

lock_tap_offset = 10 # m4 lock setscrew offset from end

# hole diameters
holes = {'m6close': 6.3}
holes['m4tap'] = 3.3


assembly = []

# get the extrusion from thorlabs
if "__file__" in locals():
    here = pathlib.Path(__file__).parent.absolute()
else:
    here = pathlib.Path('.') # we don't have __file__, do our best
stockfile = here.joinpath('step_input', 'XE25RL2-Step.step')
afp = cq.importers.importStep(str(stockfile))

# make a screen
s = cq.Workplane('XY').box(*screen['dims'], centered=[True, True, False]).rotate((0,0,0),(1,0,0),-90)
s = s.faces(">Y").workplane().rect(*screen['hole_spacing'], forConstruction=True).vertices().hole(screen['hole_dia'])
s = s.translate((0,ext['dim']/2,0))

# bottom screen
bs = s.translate((0,0,-ext['dim']-forks['length']+screen['dims'][1]/2))
assembly.extend(bs.vals())

# top screen
ts = bs.translate((0,0,screen['dims'][1]))
assembly.extend(ts.vals())

# central shaft
cs = afp.split(keepTop=True)
cs = cs.faces('<Z').workplane(-shaft['length']).split(keepTop=True)
cs = cs.faces('>Z').workplane(-shaft['swing_hole_offset']).transformed(rotate=(90,-90,0)).circle(holes['m6close']/2).cutThruAll()
cs = cs.faces('<Z').workplane(-lock_tap_offset).transformed(rotate=(90,0,0)).hole(holes['m4tap'])
cs = cs.rotateAboutCenter((0,0,1),45)
assembly.extend(cs.vals())

# right fork
rf = afp.split(keepBottom=True)
rf = rf.faces(">Z").workplane(-forks['length']).split(keepTop=True)
rf = rf.faces('>Z').workplane(-lock_tap_offset).transformed(rotate=(-90,90,0)).hole(holes['m4tap'])
rf = rf.faces(">X").workplane(-forks['plane_down']).split(keepBottom=True)
rf = rf.translate((-screen['hole_spacing'][0]/2, 0, -ext['dim']))
assembly.extend(rf.vals())

# left fork
lf = rf.mirror('ZY')
assembly.extend(lf.vals())

# crossbar
cb = afp.workplane(crossbar['length']/2).split(keepBottom=True)
cb = cb.faces('>Z').workplane(-crossbar['length']).split(keepTop=True)
cb = cb.rotateAboutCenter((0,1,0),90).translate((0,0,-ext['dim']/2))
cb = cb.faces('<Z').workplane().rarray(screen['hole_spacing'][0]/2,1,3,1).hole(holes['m6close'])
assembly.extend(cb.vals())

# draw the assembly if we're in cq's GUI, otherwise export a step file
if "show_object" in locals():
    for thing in assembly:
        show_object(thing)
else:
    cpnd = cq.Compound.makeCompound(assembly)
    export_filename = here.joinpath('step_output', 'assembly.step')
    with open(str(export_filename), "w") as fh:
        cq.exporters.exportShape(cpnd, cq.exporters.ExportTypes.STEP, fh)
