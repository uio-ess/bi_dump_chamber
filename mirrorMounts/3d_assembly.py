#!/usr/bin/env python3
import cadquery as cq

# the plate
plate_thickness = 15
plate_dxf_filename = 'plate_layout_no_dim.dxf'
plate2d = cq.importers.importShape(cq.importers.ImportTypes.DXF, plate_dxf_filename, tol=1e-3)
tmp = plate2d.faces().wires()
tmp.ctx.pendingWires = tmp.vals()
plate = tmp.extrude(plate_thickness)
plate_x = plate.findSolid().BoundingBox().xlen
plate_y = plate.findSolid().BoundingBox().ylen
plate = plate.translate((-plate_x/2,-plate_y/2,-plate_thickness))

# post
post_y_offset_from_center = 145
post_filename = 'P200_M-Step.step'
post = cq.importers.importShape(cq.importers.ImportTypes.STEP, post_filename)
post = post.rotateAboutCenter(axisEndPoint=(1,0,0),angleDegrees=90)
post_z = post.findSolid().BoundingBox().zlen
post = post.translate((0,post_y_offset_from_center,post_z/2))

# post base clamp
clamp_filename = "PF175B-Step.step"
clamp = cq.importers.importShape(cq.importers.ImportTypes.STEP, clamp_filename)
clamp = clamp.rotate((0,0,0), (1,0,0), angleDegrees=90)
clamp = clamp.rotate((0,0,0), (0,0,1), angleDegrees=90)
clamp = clamp.translate((0,post_y_offset_from_center,0))

# post base flange
base_filename = "PB4_M-Step.step"
base = cq.importers.importShape(cq.importers.ImportTypes.STEP, base_filename)
base = base.rotate((0,0,0), (1,0,0), angleDegrees=90)
base_thickness = 6.1
base = base.translate((0,post_y_offset_from_center,base_thickness))
post = post.translate((0,0,base_thickness))

# polaris 45
polaris45_filename = "POLARIS-MA45_M-Step.step"
polaris45_stepfile_offset = 10.2794
polaris45 = cq.importers.importShape(cq.importers.ImportTypes.STEP, polaris45_filename)
polaris45 = polaris45.rotate((0,0,0), (1,0,0), angleDegrees=90)
polaris45_z = polaris45.findSolid().BoundingBox().zlen
polaris45 = polaris45.translate((0,0,polaris45_stepfile_offset))
mirror_angle_from_vertical = 15
polaris45 = polaris45.rotate((0,0,0), (0,0,1), angleDegrees=90+mirror_angle_from_vertical)
polaris45 = polaris45.translate((0,post_y_offset_from_center,base_thickness+post_z))