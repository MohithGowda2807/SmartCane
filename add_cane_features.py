import bpy, bmesh, math
from math import radians, sin, cos, pi
from mathutils import Vector, Matrix, Euler
import os

print("--- STARTING HARDWARE ADDITIONS TO BLENDER MODEL ---")

def get_mat(name, default_color=(0.5, 0.5, 0.5), metallic=0.0, rough=0.5, alpha=1.0, emit=0.0):
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get('Principled BSDF')
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (*default_color, 1.0)
        bsdf.inputs['Metallic'].default_value = metallic
        bsdf.inputs['Roughness'].default_value = rough
        if emit > 0:
            bsdf.inputs['Emission Color'].default_value = (*default_color, 1.0)
            bsdf.inputs['Emission Strength'].default_value = emit
    return m

# Materials
M_WHITE   = get_mat('Plastic_White', (0.9, 0.9, 0.88), rough=0.35)
M_STEEL   = get_mat('Metal_Steel', (0.65, 0.65, 0.67), metallic=1.0, rough=0.25)
M_ALU     = get_mat('Metal_Alu', (0.8, 0.8, 0.82), metallic=1.0, rough=0.35)
M_GOLD    = get_mat('Metal_Gold', (1.0, 0.72, 0.28), metallic=1.0, rough=0.2)
M_LENS    = get_mat('Lens_Dark', (0.01, 0.01, 0.02), metallic=0.7, rough=0.05)
M_GLASS   = get_mat('Glass_Clear', (0.7, 0.85, 0.95), rough=0.05, alpha=0.35)
M_PCB_BLU = get_mat('PCB_Blue', (0.015, 0.08, 0.35), rough=0.4)
M_PCB_BLK = get_mat('PCB_Black', (0.02, 0.02, 0.02), rough=0.4)
M_SHIELD  = get_mat('Shield_Silver', (0.8, 0.8, 0.82), metallic=1.0, rough=0.3)
M_HOLE    = get_mat('Hole_Dark', (0.01, 0.01, 0.01), rough=0.9)
M_SPK_CONE= get_mat('Speaker_Cone', (0.15, 0.15, 0.15), rough=0.7)
M_TEAL    = get_mat('Accent_Teal', (0.0, 0.42, 0.48), rough=0.35)
M_LED_GRN = get_mat('LED_Green', (0.05, 0.95, 0.15), emit=5.0)
M_ANT     = get_mat('Ceramic_Ant', (0.85, 0.82, 0.78), rough=0.5)

# Parent empties
handle_unit = bpy.data.objects.get('HANDLE_UNIT')
shaft_unit  = bpy.data.objects.get('SHAFT_UNIT')
tip_unit    = bpy.data.objects.get('TIP_UNIT')
main_col    = bpy.context.scene.collection

def create_mesh_object(name, parent, bm, mats):
    # Remove existing if already present
    old = bpy.data.objects.get(name)
    if old:
        bpy.data.objects.remove(old, do_unlink=True)
    me = bpy.data.meshes.new(name + "_mesh")
    bm.to_mesh(me)
    bm.free()
    for m in mats:
        me.materials.append(m)
    for p in me.polygons:
        p.use_smooth = True
    try:
        me.set_sharp_from_angle(angle=radians(35))
    except Exception:
        pass
    ob = bpy.data.objects.new(name, me)
    main_col.objects.link(ob)
    if parent:
        ob.parent = parent
    return ob

# ---------------------------------------------------------
# 1. TOP MICROPHONE (Handle Apex / Thumb-Arch Top)
# ---------------------------------------------------------
print("Adding Handle_TopMicrophone...")
bm = bmesh.new()
mats = [M_STEEL, M_GOLD, M_SPK_CONE, M_HOLE]

# Outer bezel ring at top of cane (Z=1.256)
mx1 = Matrix.Translation((0.003, 0.0, 1.2565))
res1 = bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=0.0050, radius2=0.0048, depth=0.0020, matrix=mx1)
for f in [f for v in res1['verts'] for f in v.link_faces]: f.material_index = 0

# Gold decorative acoustic trim ring
mx2 = Matrix.Translation((0.003, 0.0, 1.2575))
res2 = bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=0.0042, radius2=0.0040, depth=0.0010, matrix=mx2)
for f in [f for v in res2['verts'] for f in v.link_faces]: f.material_index = 1

# Recessed acoustic protective mesh
mx3 = Matrix.Translation((0.003, 0.0, 1.2576))
res3 = bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=0.0035, radius2=0.0035, depth=0.0006, matrix=mx3)
for f in [f for v in res3['verts'] for f in v.link_faces]: f.material_index = 2

# Center MEMS acoustic port hole
mx4 = Matrix.Translation((0.003, 0.0, 1.2580))
res4 = bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.0010, radius2=0.0010, depth=0.0008, matrix=mx4)
for f in [f for v in res4['verts'] for f in v.link_faces]: f.material_index = 3

create_mesh_object("Handle_TopMicrophone", handle_unit, bm, mats)

# ---------------------------------------------------------
# 2. BOTTOM CAMERA ASSEMBLY (Totally 2 cameras: Top + Bottom)
# ---------------------------------------------------------
print("Adding Shaft_BottomCamera...")
bm = bmesh.new()
mats = [M_WHITE, M_TEAL, M_STEEL, M_LENS, M_GLASS, M_PCB_BLK]

# Located at lower shaft, Z=0.285, X=0.015, looking forward and angled 35 deg downwards
cam_center = Vector((0.016, 0.0, 0.285))
cam_rot = Euler((0.0, radians(35.0), 0.0))
rot_mat = cam_rot.to_matrix().to_4x4()

# Pod mounting housing (aerodynamic teardrop pod protruding from the red tube)
pod_mat = Matrix.Translation(cam_center) @ rot_mat
res_pod = bmesh.ops.create_cube(bm, size=1.0, matrix=pod_mat @ Matrix.LocRotScale(Vector((0.0, 0.0, 0.0)), Euler((0,0,0)), Vector((0.016, 0.022, 0.018))))
for f in [f for v in res_pod['verts'] for f in v.link_faces]: f.material_index = 0

# Bezel collar around camera lens
res_col = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0070, radius2=0.0068, depth=0.0040, matrix=pod_mat @ Matrix.LocRotScale(Vector((0.008, 0.0, 0.0)), Euler((0, radians(90), 0)), Vector((1,1,1))))
for f in [f for v in res_col['verts'] for f in v.link_faces]: f.material_index = 1

# Steel lens retaining ring
res_ring = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0055, radius2=0.0055, depth=0.0020, matrix=pod_mat @ Matrix.LocRotScale(Vector((0.010, 0.0, 0.0)), Euler((0, radians(90), 0)), Vector((1,1,1))))
for f in [f for v in res_ring['verts'] for f in v.link_faces]: f.material_index = 2

# Dark optical lens curved face
res_lens = bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=12, radius=0.0045, matrix=pod_mat @ Matrix.LocRotScale(Vector((0.010, 0.0, 0.0)), Euler((0,0,0)), Vector((0.4, 1.0, 1.0))))
for f in [f for v in res_lens['verts'] for f in v.link_faces]: f.material_index = 3

# Glass protective element
res_gl = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0048, radius2=0.0048, depth=0.0006, matrix=pod_mat @ Matrix.LocRotScale(Vector((0.011, 0.0, 0.0)), Euler((0, radians(90), 0)), Vector((1,1,1))))
for f in [f for v in res_gl['verts'] for f in v.link_faces]: f.material_index = 4

create_mesh_object("Shaft_BottomCamera", shaft_unit, bm, mats)

# ---------------------------------------------------------
# 3. PIR SENSORS (Upper Pedestrian PIR & Lower Hazard PIR)
# ---------------------------------------------------------
print("Adding Shaft_PIR_Sensor_Upper and Shaft_PIR_Sensor_Lower...")
# Upper PIR at Z=1.045m, X=0.021m
bm = bmesh.new()
mats = [M_TEAL, M_WHITE, M_SHIELD, M_GLASS]

mx_pir_u = Matrix.Translation((0.021, 0.0, 1.045))
# Bezel collar
res_b1 = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0062, radius2=0.0060, depth=0.0025, matrix=mx_pir_u @ Euler((0, radians(90), 0)).to_matrix().to_4x4())
for f in [f for v in res_b1['verts'] for f in v.link_faces]: f.material_index = 0

# Faceted Fresnel Dome (16 segments gives faceted appearance of PIR lens)
res_d1 = bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=8, radius=0.0050, matrix=Matrix.Translation((0.0225, 0.0, 1.045)) @ Matrix.Scale(0.65, 4, Vector((1, 0, 0))))
for f in [f for v in res_d1['verts'] for f in v.link_faces]: f.material_index = 1

# Internal dual element sensor
res_s1 = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((0.0195, 0.0, 1.045)) @ Matrix.Scale(0.0025, 4, Vector((1, 1.5, 1.2))))
for f in [f for v in res_s1['verts'] for f in v.link_faces]: f.material_index = 2

create_mesh_object("Shaft_PIR_Sensor_Upper", shaft_unit, bm, mats)

# Lower PIR at Z=0.535m, X=0.014m
bm = bmesh.new()
mats = [M_TEAL, M_WHITE, M_SHIELD, M_GLASS]

mx_pir_l = Matrix.Translation((0.014, 0.0, 0.535))
# Bezel collar
res_b2 = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0058, radius2=0.0056, depth=0.0025, matrix=mx_pir_l @ Euler((0, radians(90), 0)).to_matrix().to_4x4())
for f in [f for v in res_b2['verts'] for f in v.link_faces]: f.material_index = 0

# Faceted Fresnel Dome
res_d2 = bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=8, radius=0.0048, matrix=Matrix.Translation((0.0155, 0.0, 0.535)) @ Matrix.Scale(0.65, 4, Vector((1, 0, 0))))
for f in [f for v in res_d2['verts'] for f in v.link_faces]: f.material_index = 1

# Internal sensor
res_s2 = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((0.0125, 0.0, 0.535)) @ Matrix.Scale(0.0025, 4, Vector((1, 1.5, 1.2))))
for f in [f for v in res_s2['verts'] for f in v.link_faces]: f.material_index = 2

create_mesh_object("Shaft_PIR_Sensor_Lower", shaft_unit, bm, mats)

# ---------------------------------------------------------
# 4. BLUETOOTH AUDIO ASSISTANT MODULE (Internal Rail)
# ---------------------------------------------------------
print("Adding Shaft_BluetoothModule...")
bm = bmesh.new()
mats = [M_PCB_BLU, M_SHIELD, M_ANT, M_LED_GRN, M_GOLD]

# PCB Board in XZ plane (Z=0.910, X=-0.005, Y=0.006)
bt_center = Vector((-0.005, 0.006, 0.908))
res_pcb = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation(bt_center) @ Matrix.Scale(1.0, 4, Vector((0.012, 0.0016, 0.022))))
for f in [f for v in res_pcb['verts'] for f in v.link_faces]: f.material_index = 0

# RF Shield Can
res_rf = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((-0.005, 0.0072, 0.904)) @ Matrix.Scale(1.0, 4, Vector((0.009, 0.0018, 0.011))))
for f in [f for v in res_rf['verts'] for f in v.link_faces]: f.material_index = 1

# Ceramic Chip Antenna
res_ant = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((-0.005, 0.0072, 0.915)) @ Matrix.Scale(1.0, 4, Vector((0.004, 0.0018, 0.005))))
for f in [f for v in res_ant['verts'] for f in v.link_faces]: f.material_index = 2

# Status indicator LED (Audio Link Active)
res_led = bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=0.0008, radius2=0.0008, depth=0.0010, matrix=Matrix.Translation((-0.002, 0.0072, 0.911)) @ Euler((radians(90), 0, 0)).to_matrix().to_4x4())
for f in [f for v in res_led['verts'] for f in v.link_faces]: f.material_index = 3

create_mesh_object("Shaft_BluetoothModule", shaft_unit, bm, mats)

# ---------------------------------------------------------
# 5. ULTRASONIC SENSOR ENHANCEMENT (Twin Transducer Rings)
# ---------------------------------------------------------
print("Enhancing Tip_UltrasonicSensor...")
# Check if Tip_UltrasonicTransducers already exists
old_us = bpy.data.objects.get('Tip_UltrasonicTransducers')
if old_us:
    bpy.data.objects.remove(old_us, do_unlink=True)

bm = bmesh.new()
mats = [M_ALU, M_HOLE, M_TEAL]

# Twin transducers (Transmitter and Receiver) at Z=0.165m, X=0.024m, Y=+/-0.0065m
for y_side in [-0.0065, 0.0065]:
    mx_t = Matrix.Translation((0.0245, y_side, 0.165)) @ Euler((0, radians(90), 0)).to_matrix().to_4x4()
    # Aluminum cylindrical housing cup
    res_cup = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0052, radius2=0.0050, depth=0.0035, matrix=mx_t)
    for f in [f for v in res_cup['verts'] for f in v.link_faces]: f.material_index = 0
    
    # Recessed dark acoustic mesh diaphragm
    res_mesh = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.0042, radius2=0.0042, depth=0.0008, matrix=Matrix.Translation((0.0263, y_side, 0.165)) @ Euler((0, radians(90), 0)).to_matrix().to_4x4())
    for f in [f for v in res_mesh['verts'] for f in v.link_faces]: f.material_index = 1

create_mesh_object("Tip_UltrasonicTransducers", tip_unit, bm, mats)

# Save the blend file
bpy.ops.wm.save_mainfile(filepath="SmartCane/SmartIntelligentCane.blend")
print("SUCCESS: SmartIntelligentCane.blend saved successfully with all requested additions!")
