import bpy, math
from math import radians
from mathutils import Vector, Euler
import os

print("--- RENDERING PRESENTATION SNAPSHOTS ---")

scene = bpy.context.scene
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGBA'
scene.render.film_transparent = True

os.makedirs('renders', exist_ok=True)

def setup_camera(name, loc, rot, lens=50.0):
    cam_ob = bpy.data.objects.get(name)
    if not cam_ob:
        cam_data = bpy.data.cameras.new(name)
        cam_ob = bpy.data.objects.new(name, cam_data)
        scene.collection.objects.link(cam_ob)
    cam_ob.location = loc
    cam_ob.rotation_euler = Euler((radians(rot[0]), radians(rot[1]), radians(rot[2])))
    cam_ob.data.lens = lens
    return cam_ob

# Shot 1: Full Cane Overview
cam_full = setup_camera("CAM_Presentation_Full", (1.8, -2.8, 0.9), (72, 0, 32), lens=42.0)
scene.camera = cam_full
scene.render.filepath = os.path.abspath("renders/cane_full_overview.png")
bpy.ops.render.render(write_still=True)
print("Rendered: renders/cane_full_overview.png")

# Shot 2: Handle & Top Mic Close-Up
cam_handle = setup_camera("CAM_Presentation_Handle", (0.35, -0.45, 1.25), (78, 0, 38), lens=65.0)
scene.camera = cam_handle
scene.render.filepath = os.path.abspath("renders/handle_top_mic_and_camera.png")
bpy.ops.render.render(write_still=True)
print("Rendered: renders/handle_top_mic_and_camera.png")

# Shot 3: Lower Shaft & Tip (Bottom Camera + Ultrasonic Sensor + Lower PIR)
cam_tip = setup_camera("CAM_Presentation_Tip", (0.42, -0.48, 0.26), (80, 0, 40), lens=60.0)
scene.camera = cam_tip
scene.render.filepath = os.path.abspath("renders/tip_bottom_camera_ultrasonic.png")
bpy.ops.render.render(write_still=True)
print("Rendered: renders/tip_bottom_camera_ultrasonic.png")

# Shot 4: Mid-Shaft Sensors (Upper PIR + Electronics Housing)
cam_shaft = setup_camera("CAM_Presentation_Shaft", (0.50, -0.65, 0.95), (82, 0, 36), lens=55.0)
scene.camera = cam_shaft
scene.render.filepath = os.path.abspath("renders/shaft_sensors_pir.png")
bpy.ops.render.render(write_still=True)
print("Rendered: renders/shaft_sensors_pir.png")

print("--- ALL 4 SNAPSHOT RENDERS FINISHED ---")
