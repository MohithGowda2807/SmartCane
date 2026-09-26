from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

template_path = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SIH2026-IDEA-Presentation-Format (1).pptx"
output_path = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SmartCane_SIH2026_WINNING_DECK.pptx"
assets_dir = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\PPT_Assets"

prs = Presentation(template_path)

# Ensure only 6 slides
while len(prs.slides) > 6:
    rId = prs.slides._sldIdLst[len(prs.slides) - 1].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[len(prs.slides) - 1]

# Clear existing non-background shapes on slides 2 to 6 so we can lay out clean professional content
for slide_idx in range(1, len(prs.slides)):
    slide = prs.slides[slide_idx]
    # Keep the slide header / template title if present, remove content placeholders
    shapes_to_remove = []
    for shape in slide.shapes:
        # Check if shape is a content box or old table/image (keep top template title bar)
        if shape.top > Inches(1.3):
            shapes_to_remove.append(shape)
    for shape in shapes_to_remove:
        sp = shape._element
        sp.getparent().remove(sp)

# Slide 1: Update Title Slide text
s1 = prs.slides[0]
for shape in s1.shapes:
    if shape.has_text_frame:
        for p in shape.text_frame.paragraphs:
            if "Problem Statement ID" in p.text or "Team Name" in p.text:
                # Keep text box clean with proper styling
                pass

# ==================== SLIDE 2: PROPOSED SOLUTION & 3-LANE ARCHITECTURE ====================
s2 = prs.slides[1]
# Title
txBox = s2.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.8))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "PROPOSED SOLUTION & HIGH-LEVEL SYSTEM FLOW"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = RGBColor(15, 23, 42)

# Left Column: Problem & 6-Pillar Breakthrough
left_box = s2.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(5.2), Inches(5.6))
ltf = left_box.text_frame
ltf.word_wrap = True

p = ltf.paragraphs[0]
p.text = "🔴 REAL USER MOBILITY PAIN POINTS:"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = RGBColor(225, 29, 72)

p_prob = ltf.add_paragraph()
p_prob.text = '• "I feel the ground, but hit low tree branches at head level."\n• "Silent electric scooters approach without any audio warning."\n• "Earbuds in existing smart canes block traffic hearing—a death trap."\n• "If phone OS or app crashes, all safety warnings immediately die."'
p_prob.font.size = Pt(9.5)
p_prob.font.color.rgb = RGBColor(71, 85, 105)

p_sol_hdr = ltf.add_paragraph()
p_sol_hdr.text = "\n🟢 ECOWIPE-INSPIRED 6-PILLAR BREAKTHROUGH:"
p_sol_hdr.font.size = Pt(12)
p_sol_hdr.font.bold = True
p_sol_hdr.font.color.rgb = RGBColor(5, 150, 105)

p_sol = ltf.add_paragraph()
p_sol.text = "1. Asymmetric Dual-Core: ESP32-S3 (Always-on 50ms reflex) + RPi Zero 2 W.\n2. 8-Sensor 360° Perception: Dual cameras, Ultrasonic, ToF, dual PIRs, IMU.\n3. Ears-Free Bone Conduction: BLE 5.x keeps ear canals 100% open for traffic.\n4. Sub-15ms Palm Haptics: DRV2605L LRA waveform for drop-offs & obstacles.\n5. Autonomous Direct-AT SOS: Standalone 112 call + GPS SMS via LTE (No phone).\n6. Motorized Quad-Pod Tip: Auto-deploying 1.2s base stabilizes rough inclines."
p_sol.font.size = Pt(9.5)
p_sol.font.color.rgb = RGBColor(30, 41, 59)

# Right Column: Insert Winner-Style 3-Lane Flowchart Image
img_s2 = os.path.join(assets_dir, "winner_style_3lane_flowchart.png")
if os.path.exists(img_s2):
    s2.shapes.add_picture(img_s2, Inches(6.3), Inches(1.3), width=Inches(6.3))

# ==================== SLIDE 3: TECHNICAL APPROACH ====================
s3 = prs.slides[2]
txBox = s3.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "TECHNICAL APPROACH & SENSOR COVERAGE"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = RGBColor(15, 23, 42)

# Insert Sensor Coverage Map on Left
img_cov = os.path.join(assets_dir, "3_sensor_coverage_map.jpg")
if os.path.exists(img_cov):
    s3.shapes.add_picture(img_cov, Inches(0.8), Inches(1.4), width=Inches(6.2))

# Right Column: Tech Stack & Architecture Highlights
right_box = s3.shapes.add_textbox(Inches(7.2), Inches(1.4), Inches(5.4), Inches(5.6))
rtf = right_box.text_frame
rtf.word_wrap = True

p = rtf.paragraphs[0]
p.text = "🛠️ MULTI-TIER ENGINEERING STACK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = RGBColor(14, 116, 144)

tech_details = [
    ("⚡ ESP32-S3 Firmware (Safety Core):", "Dual Xtensa @ 240MHz executing FreeRTOS 50ms deterministic loop. Direct GPIO/I2C arbitration; bypasses OS entirely."),
    ("🧠 Raspberry Pi Zero 2 W (Edge AI):", "Quad Cortex-A53 running Linux RT kernel. YOLO-Fastest & MobileNetV3-SSD Int8 quantized at 12–15 fps for scene OCR."),
    ("📡 Differential I²C Bus (PCA9615):", "Eliminates EMI across the 1.1m shaft, ensuring zero noise for tip-mounted ToF and IMU sensors."),
    ("🦴 Wireless Audio Transceiver:", "Dedicated BLE 5.x A2DP stream to bone-conduction headphones for zero ear obstruction."),
    ("🚨 SIM7600G-H LTE Cat-4 & GNSS:", "Direct-AT emergency dialing to 112 + automated SMS with live Google Maps coordinate pinpoint."),
    ("🔋 5-Rail Power Distribution:", "1S2P 6800 mAh Li-Ion with TI BQ25895 fast charging and TI TPS63020 buck-boost regulator. 36h+ Power-Save runtime.")
]

for title, desc in tech_details:
    p_t = rtf.add_paragraph()
    p_t.text = title
    p_t.font.size = Pt(10)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(30, 41, 59)
    
    p_d = rtf.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = RGBColor(71, 85, 105)

# ==================== SLIDE 4: FEASIBILITY & VIABILITY ====================
s4 = prs.slides[3]
txBox = s4.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "FEASIBILITY, VIABILITY & RISK MITIGATION"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = RGBColor(15, 23, 42)

# Insert Slide 4 Image (2x2 Matrix + Challenges)
img_s4 = os.path.join(assets_dir, "slide4_feasibility_matrix.png")
if os.path.exists(img_s4):
    s4.shapes.add_picture(img_s4, Inches(0.8), Inches(1.3), width=Inches(11.7))

# ==================== SLIDE 5: IMPACT & BENEFITS ====================
s5 = prs.slides[4]
txBox = s5.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "IMPACT, BENEFITS & COMPETITIVE ADVANTAGE"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = RGBColor(15, 23, 42)

# Insert Slide 5 Image (11-Point Table + National Pillars + Metrics)
img_s5 = os.path.join(assets_dir, "slide5_impact_and_matrix.png")
if os.path.exists(img_s5):
    s5.shapes.add_picture(img_s5, Inches(0.8), Inches(1.3), width=Inches(11.7))

# ==================== SLIDE 6: RESEARCH, STANDARDS & PROOF ====================
s6 = prs.slides[5]
txBox = s6.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "RESEARCH, STANDARDS & PROOF OF EXECUTION"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = RGBColor(15, 23, 42)

# Insert Slide 6 Image (Standards + Citations + Proof of Work)
img_s6 = os.path.join(assets_dir, "slide6_research_and_proof.png")
if os.path.exists(img_s6):
    s6.shapes.add_picture(img_s6, Inches(0.8), Inches(1.3), width=Inches(11.7))

prs.save(output_path)
print("Successfully generated final clean presentation:", output_path)
