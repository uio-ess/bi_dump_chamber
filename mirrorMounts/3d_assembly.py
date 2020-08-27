#!/usr/bin/env python3
import cadquery as cq
import math
import copy

asy=[]


# the plate
plate_thickness = 15
post_y_offset_from_center = 145
plate_dxf_filename = 'plate_layout.dxf'
plate2d = cq.importers.importShape(cq.importers.ImportTypes.DXF, plate_dxf_filename, ignored_layers=['dims'])
tmp = plate2d.faces().wires()
tmp.ctx.pendingWires = tmp.vals()
plate = tmp.extrude(plate_thickness)
plate_x = plate.findSolid().BoundingBox().xlen
plate_y = plate.findSolid().BoundingBox().ylen
plate = plate.translate((-plate_x/2,-plate_y/2,-plate_thickness))
asy.extend(plate.vals())

# post base clamp
clamp_filename = "PF175B-Step.step"
clamp = cq.importers.importShape(cq.importers.ImportTypes.STEP, clamp_filename)
clamp = clamp.rotate((0,0,0), (1,0,0), angleDegrees=90)
clamp = clamp.rotate((0,0,0), (0,0,1), angleDegrees=90)
clamp = clamp.translate((0,post_y_offset_from_center,0))
asy.extend(clamp.vals())

# post base flange
base_filename = "PB4_M-Step.step"
base = cq.importers.importShape(cq.importers.ImportTypes.STEP, base_filename)
base = base.rotate((0,0,0), (1,0,0), angleDegrees=90)
base_thickness = 6.1
base = base.translate((0,post_y_offset_from_center,base_thickness))
asy.extend(base.vals())


# post (for top)
post_filename = 'P250_M-Step.step'
post = cq.importers.importShape(cq.importers.ImportTypes.STEP, post_filename)
post = post.rotateAboutCenter(axisEndPoint=(1,0,0),angleDegrees=90)
#post_z = post.findSolid().BoundingBox().zlen
post = post.translate((0,0,base_thickness))
post = post.translate((0,post_y_offset_from_center,post.findSolid().BoundingBox().zlen/2))
asy.extend(post.vals())

asy2 = copy.copy(asy) # copy for top

# camera pipe
pipe_outer = 127
pipe_inner = 119
pipe_length = 1500
pipe = cq.Workplane("XY").circle(pipe_outer/2).extrude(-pipe_length).circle(pipe_inner/2).cutThruAll()

# post2 (shorter, for bottom)
#post2_filename = 'P75_M-Step.step'
#post2 = cq.importers.importShape(cq.importers.ImportTypes.STEP, post2_filename)
#post2 = post2.rotateAboutCenter(axisEndPoint=(1,0,0),angleDegrees=90)
#post2 = post2.translate((0,0,base_thickness))
#post2_z = post2.findSolid().BoundingBox().zlen
#post2 = post2.translate((0,post_y_offset_from_center,post2_z/2))
#asy.extend(post2.vals())

# polaris 45
polaris45_filename = "POLARIS-MA45_M-Step.step"
polaris45_stepfile_base_offset = 10.2794
polaris45_angled_face_offset = 2.6952
polaris45_mount_hole_offset = 11.023385
##polaris45_mounting_hole_offset = (0,-math.sin(polaris45_angled_face_offset),math.sin(polaris45_angled_face_offset))
##polaris45 = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris45_filename)
##polaris45 = polaris45.rotate((0,0,0), (1,0,0), angleDegrees=90)
##polaris45_z = polaris45.findSolid().BoundingBox().zlen
##polaris45 = polaris45.translate((0,0,polaris45_stepfile_base_offset))
##mirror_angle_from_vertical = 0
##polaris45 = polaris45.rotate((0,0,0), (0,0,1), angleDegrees=90+mirror_angle_from_vertical)
##polaris45 = polaris45.translate((0,post_y_offset_from_center,base_thickness+post2_z))
##asy.extend(polaris45.vals())

bot_plate = cq.Compound.makeCompound(asy)

# polaris adjuster
mirror_ass = []
polaris_filename = "POLARIS-K1M4_M-Step.step"
polaris = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris_filename)
polaris = polaris.rotate((0,0,0), (1,0,0), angleDegrees=180)
polaris_base_plate_thickness = 6.4
polaris = polaris.translate((0,0,-polaris_base_plate_thickness))
polaris_base_face_to_mounting_face = 25.3
polaris_mount_offset_from_center = (-7,-7,polaris_base_face_to_mounting_face+polaris45_angled_face_offset)
mirror_ass.extend(polaris.vals())

# bottom mirror holder
mirror_mount_filename = "Mirror_Assembly_M9_B.stp"
mm = cq.importers.importShape(cq.importers.ImportTypes.STEP, mirror_mount_filename)
mirror_ass.extend(mm.vals())

# manipulate the bottom mirror assembly
bot_mirror_cpnd = cq.Compound.makeCompound(mirror_ass)
bot_mirror_cpnd = bot_mirror_cpnd.translate(polaris_mount_offset_from_center)
bot_mirror_cpnd = bot_mirror_cpnd.rotate((0,0,0), (0,0,1), angleDegrees=45)
bot_mirror_cpnd = bot_mirror_cpnd.translate((0,polaris45_mount_hole_offset,0))
bot_mirror_cpnd = bot_mirror_cpnd.rotate((0,0,0), (1,0,0), angleDegrees=-45)
#bot_mirror_cpnd = bot_mirror_cpnd.rotate((0,0,0), (0,0,1), angleDegrees=mirror_angle_from_vertical) 
#bot_mirror_cpnd = bot_mirror_cpnd.translate((0,post_y_offset_from_center,base_thickness+post2_z+polaris45_stepfile_base_offset))

top_plate = cq.Compound.makeCompound(asy2)
show_object(top_plate)

tm_asy =[]
# clamp board
clamp_filename = "C1545_M-Step.step"
clamp = cq.importers.importShape(cq.importers.ImportTypes.STEP, clamp_filename)
clamp = clamp.rotate((0,0,0), (1,0,0), angleDegrees=-90)
clamp_along_post = 190
clamp_plate_face_offset = 38.1
clamp = clamp.translate((0,post_y_offset_from_center,clamp_along_post))
tm_asy.extend(clamp.vals())

# polaris clamp
pclamp_filename = "POLARIS-CA25_M-Step.step"
pclamp = cq.importers.importShape(cq.importers.ImportTypes.STEP, pclamp_filename)
pclamp_stepfile_offset = (33+20.3,-19.878,0)
pclamp = pclamp.translate(pclamp_stepfile_offset)
pclamp = pclamp.rotate((0,0,0), (0,1,0), angleDegrees=90)
pclamp = pclamp.rotate((0,0,0), (0,0,1), angleDegrees=180)
pclamp = pclamp.rotate((0,0,0), (0,1,0), angleDegrees=180)
clamp_shift = 1*12.5 # how many breadboard slots to shift the post
pclamp = pclamp.translate((0,post_y_offset_from_center-clamp_plate_face_offset,clamp_along_post-clamp_shift))
tm_asy.extend(pclamp.vals())
bm_asy = copy.copy(tm_asy)

# polaris_post
ppost_filename = "PLS-P605_M-Step.step"
ppost = cq.importers.importShape(cq.importers.ImportTypes.STEP, ppost_filename)
ppost_stepfile_offset = (10.28635,-28.8969,-6.34722)
ppost = ppost.translate(ppost_stepfile_offset)
ppost = ppost.rotate((0,0,0), (0,1,0), angleDegrees=90)
ppost = ppost.rotate((0,0,0), (0,0,1), angleDegrees=180)
ppost_len = ppost.findSolid().BoundingBox().ylen
ppost = ppost.translate((0,-ppost_len,0))
ppost = ppost.translate((0,post_y_offset_from_center-clamp_plate_face_offset,clamp_along_post-clamp_shift))
tm_asy.extend(ppost.vals())

# top 45
polaris45_top = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris45_filename)
polaris45_top = polaris45_top.rotate((0,0,0), (0,0,1), angleDegrees=180)
polaris45_top = polaris45_top.rotate((0,0,0), (0,1,0), angleDegrees=-90)
polaris45_top = polaris45_top.translate((0,-polaris45_stepfile_base_offset,0))
polaris45_top = polaris45_top.translate((0,post_y_offset_from_center-clamp_plate_face_offset-ppost_len,clamp_along_post-clamp_shift))
tm_asy.extend(polaris45_top.vals())

bot_mirror_cpnd = bot_mirror_cpnd.translate((0,post_y_offset_from_center+clamp_plate_face_offset+ppost_len+polaris45_stepfile_base_offset,clamp_along_post-clamp_shift))


top_base_cpnd = cq.Compound.makeCompound(tm_asy)
show_object(top_base_cpnd)

view_pipe_angle = 45
# polaris_post for bottom
ppost2 = cq.importers.importShape(cq.importers.ImportTypes.STEP, ppost_filename)
ppost2 = ppost2.translate(ppost_stepfile_offset)
ppost2 = ppost2.rotate((0,0,0), (0,1,0), angleDegrees=90-view_pipe_angle)
ppost2 = ppost2.rotate((0,0,0), (0,0,1), angleDegrees=180)
ppost2 = ppost2.translate((0,-ppost_len,0))
ppost2 = ppost2.translate((0,post_y_offset_from_center-clamp_plate_face_offset,clamp_along_post-clamp_shift))
bm_asy.extend(ppost2.vals())

# bottom 45
polaris45_bot = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris45_filename)
polaris45_bot = polaris45_bot.rotate((0,0,0), (0,0,1), angleDegrees=180)
polaris45_bot = polaris45_bot.rotate((0,0,0), (0,1,0), angleDegrees=90+view_pipe_angle)
polaris45_bot = polaris45_bot.translate((0,-polaris45_stepfile_base_offset,0))
polaris45_bot = polaris45_bot.translate((0,post_y_offset_from_center-clamp_plate_face_offset-ppost_len,clamp_along_post-clamp_shift))
bm_asy.extend(polaris45_bot.vals())

# slide clampboard for bottom
bot_clampboard_diff = -45

bot_mirror_cpnd = bot_mirror_cpnd.rotate((0,0,clamp_along_post-clamp_shift), (0,1,clamp_along_post-clamp_shift), angleDegrees=-view_pipe_angle)
bot_mirror_cpnd = bot_mirror_cpnd.translate((0,0,bot_clampboard_diff))

bot_base_cpnd = cq.Compound.makeCompound(bm_asy)
bot_base_cpnd = bot_base_cpnd.rotate((0,post_y_offset_from_center,0), (0,post_y_offset_from_center,1), angleDegrees=180)
bot_base_cpnd = bot_base_cpnd.translate((0,0,bot_clampboard_diff))

tmir_asy = []
# top polaris adjuster
polaris_top = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris_filename)
polaris_top = polaris_top.rotate((0,0,0), (1,0,0), angleDegrees=180)
polaris_top = polaris_top.translate((0,0,-polaris_base_plate_thickness))
polaris_top = polaris_top.rotate((0,0,0), (0,0,1), angleDegrees=45)
tmir_asy.extend(polaris_top.vals())


# top mirror
top_mirror_dims = (110,150,25)
top_mirror = cq.Workplane().box(top_mirror_dims[0],top_mirror_dims[1],top_mirror_dims[2],centered=(True,True,False))
made_up_mount_thickness = 5 # for imaginary mount
top_mirror = top_mirror.translate((0,0,made_up_mount_thickness))

# manipulate the top mirror assembly
tmir_asy.extend(top_mirror.vals())
top_mirror_cpnd = cq.Compound.makeCompound(tmir_asy)
top_mirror_cpnd = top_mirror_cpnd.translate((0,-math.sqrt(7**2+7**2),polaris_base_face_to_mounting_face+polaris45_angled_face_offset))
top_mirror_cpnd = top_mirror_cpnd.translate((0,polaris45_mount_hole_offset,0))
top_mirror_cpnd = top_mirror_cpnd.rotate((0,0,0), (1,0,0), angleDegrees=90+45)
top_mirror_cpnd = top_mirror_cpnd.translate((0,post_y_offset_from_center-clamp_plate_face_offset-ppost_len-polaris45_stepfile_base_offset,clamp_along_post-clamp_shift))
show_object(top_mirror_cpnd)

# lights
lamps = []
lamp_filename = "lamp.step"
lampa = cq.importers.importShape(cq.importers.ImportTypes.STEP, lamp_filename)
lamp_array_x = 100
lamp_array_y = 50
lamp = lampa.translate((-lamp_array_x,0,lamp_array_y))
lamps.extend(lamp.vals())
lamp = lampa.translate((lamp_array_x,0,lamp_array_y))
lamps.extend(lamp.vals())
lamp = lampa.translate((-lamp_array_x,0,-lamp_array_y))
lamps.extend(lamp.vals())
lamp = lampa.translate((lamp_array_x,0,-lamp_array_y))
lamps.extend(lamp.vals())
lamp_cpnd = cq.Compound.makeCompound(lamps)
lamp_cpnd = lamp_cpnd.translate((0,post_y_offset_from_center-clamp_plate_face_offset,clamp_along_post))



# translate the bottom setup
bottom_translate = 1500
show_object(bot_mirror_cpnd.translate((0,-bottom_translate,0)))
show_object(bot_plate.translate((0,-bottom_translate,0)))
show_object(bot_base_cpnd.translate((0,-bottom_translate,0)))
show_object(pipe)
show_object(lamp_cpnd)

