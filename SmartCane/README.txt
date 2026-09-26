SMART INTELLIGENT CANE - 3D MODEL + EXPLODED-VIEW ANIMATION
Handover notes for the team
==========================================================

WHAT THIS IS
A concept visualization of the Smart Intelligent Cane, built in Blender from the
project's structural documentation. It is NOT an engineering CAD model: most
dimensions and part choices are still "to be finalized" in the documentation, so
the sizes here are working assumptions (see ASSUMPTIONS below).

FILES
  SmartIntelligentCane.blend   the model, animation, cameras, lights and scripts
  README.txt                   this note
  SmartCane_ExplodedView_*.mp4 the rendered film (only present once someone renders it)

HOW TO OPEN AND PREVIEW
  1. Install Blender 5.2 or later (free, blender.org). Older versions may not open it correctly.
  2. Open SmartIntelligentCane.blend.
  3. Press Space to play. The cameras switch automatically along the timeline.

HOW TO RENDER THE VIDEO
  Render > Render Animation (Ctrl+F12). Output is 1920x1080 MP4, 24 fps, 1020 frames
  (about 42 seconds). The output path is set to the original author's Documents\SmartCane
  folder - change it in Output Properties before rendering on another PC.
  The film has not been rendered or reviewed at full quality yet. When you watch it, check
  that the transparent shells look smooth, the labels are readable, and the feet rest on
  the stones in the last shot.

WHAT THE FILM SHOWS (frame ranges)
     1 -  120  Turntable: assembled cane, one full turn
   120 -  312  X-ray pass: outer shells go transparent, close-ups of handle, shaft, tip
   313 -  442  Sections separate, then every part explodes outward
   443 -  682  Labelled exploded close-ups: handle, shaft, tip
   683 -  762  Reassembly
   763 - 1020  Adaptive tip: cane moves from smooth floor to gravel, sensing pulse,
               support legs deploy automatically and settle at different heights,
               cane returns, legs retract

THE MODEL (about 50 named parts, real-world scale, cane ~1.26 m tall)
  HANDLE  Grip in line with the shaft; D-shaped thumb arch on the top side; camera pod at the
          arch's shaft-side foot, behind the thumb, looking down the cane (angled 20 deg away
          from the shaft). Four Braille buttons under the arch for the thumb (V round,
          E square, I triangle, P diamond); SOS on the end cap inside a guard ring; PPG pulse
          sensor on the finger side; 3 MEMS mics along the arch; haptic motor; speaker;
          control PCB; keyed shaft joint; wrist strap.
  SHAFT   Red lower tube (cable channel); split white electronics housing with USB-C port;
          mounting rail; ESP32-S3; Raspberry Pi Zero 2 W; LTE+GPS module (SIM7600G-H) with
          patch antenna; short-range RF board; power board; 2x18650 battery pack; wiring
          harness with connectors at both ends; magnetic stylus dock + Braille stylus.
  TIP     Rubber tip; moisture pins; stem; gear-motor + lead screw + drive collar; pivot hub
          with 3 folding support legs; sensor/motor-driver PCB; IMU; ultrasonic sensor;
          angled ToF step sensor (VL53L1X); split housing; quick-release connector.

USEFUL CONTROLS INSIDE THE FILE
  - Transparent shells for stills: select the empty CANE_ROOT > Object Properties >
    Custom Properties > "xray". It is keyframed; frames 140-291 are fully transparent.
  - Scripts live in the Scripting workspace (Text Editor):
      cane_animate  rebuilds the whole animation and labels. Explode distances are in the
                    OVR dictionary near the top. OFS = 312 reserves frames for the intro.
      cane_intro    turntable + x-ray pass      cane_terrain  closing adaptive-tip shot
      cane_labels   callout label text          cane_helpers / cane_materials  building blocks
    After editing, run cane_animate (Alt+P in the Text Editor).

ASSUMPTIONS AND OPEN POINTS - PLEASE REVIEW
  - All dimensions are placeholders (e.g. 40 mm housing so the Pi Zero 2 W fits, 2x18650 battery).
  - Handle layout (button, SOS, PPG, speaker positions) was chosen to suit the thumb-arch grip
    in the reference image; it is not specified in the documentation.
  - Braille: the documentation lists E as the L pattern (dots 1-2-3). The model uses the correct
    E (dots 1-5). Please fix this in the report as well.
  - IMU: the documentation places it in the shaft in one section and in the tip in another.
    The model puts it in the tip.
  - Adaptive tip: the leg mechanism has no linkage engineering, and the documentation does not
    say which sensors trigger deployment. The film shows intended behaviour and labels it
    "concept"; the caption only says "tip sensors".


UPDATE - 20 September 2026: REALISM PASS
  Every part was rebuilt with much more detail (about 63,000 faces in total). Part names, positions and the
  animation are unchanged. The Raspberry Pi Zero 2 W follows the real board layout closely; the other boards
  are plausible representations because their exact parts are not finalized. None of it is a manufacturing model.
  New scripts in the Text Editor: hd_all re-runs the whole detail pass and then cane_animate;
  hd_pi, hd_shaft, hd_handle, hd_tip and hd_misc re-run one area each.
  CAM_Inspect is a leftover inspection camera; the film never uses it and it can be deleted.
  Rendering is slower than before. The film is still 1020 frames (about 42 s) and has NOT been rendered yet.
