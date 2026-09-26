import pptx
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.action import PP_ACTION
import os

print("--- BUILDING SIH 2026 SYSTEM ARCHITECTURE POWERPOINT (TOP-DOWN TREE DESIGN) ---")

prs = pptx.Presentation()
# Set widescreen 16:9 (13.333 x 7.5 inches)
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Theme Colors
C_BG       = RGBColor(11, 17, 32)      # #0B1120 Deep Navy
C_CARD     = RGBColor(22, 30, 49)      # #161E31 Slate Card
C_BORDER   = RGBColor(40, 54, 85)      # Slate border
C_TEXT_H   = RGBColor(255, 255, 255)   # White
C_TEXT_P   = RGBColor(203, 213, 225)   # Slate 300
C_TEXT_M   = RGBColor(148, 163, 184)   # Slate 400

# Accent Colors
C_BLUE     = RGBColor(56, 189, 248)    # Perception / Vision
C_RED      = RGBColor(248, 113, 113)   # Safety RTOS
C_PURPLE   = RGBColor(168, 85, 247)    # Edge AI
C_GREEN    = RGBColor(52, 211, 153)    # Audio & HMI
C_AMBER    = RGBColor(251, 191, 36)    # Actuation / New
C_CYAN     = RGBColor(34, 211, 238)    # Power
C_PINK     = RGBColor(244, 114, 182)   # Cloud & SOS

def create_slide():
    slide = prs.slides.add_slide(blank_layout)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_BG
    bg.line.fill.background()
    return slide

def add_header(slide, title, subtitle, target_home_slide=None):
    # Top pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.35), Inches(4.5), Inches(0.3))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(15, 23, 42)
    pill.line.color.rgb = C_BLUE
    pill.line.width = Pt(1)
    tf = pill.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2026 • SYSTEM ARCHITECTURE"
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.alignment = PP_ALIGN.CENTER

    # Title box
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(8.5), Inches(0.65))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(16.5)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_H

    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(9)
    p2.font.color.rgb = C_TEXT_M

    # Breadcrumb & Return button if applicable
    if target_home_slide:
        btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(0.42), Inches(2.7), Inches(0.45))
        btn.fill.solid()
        btn.fill.fore_color.rgb = RGBColor(30, 41, 59)
        btn.line.color.rgb = C_BLUE
        btn.line.width = Pt(1.5)
        tf = btn.text_frame
        p = tf.paragraphs[0]
        p.text = "⬅ BACK TO 4-BLOCK OVERVIEW"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_H
        p.alignment = PP_ALIGN.CENTER
        btn.click_action.target_slide = target_home_slide

# Create all 6 slides
s1 = create_slide() # 4-Block Executive Overview
s2 = create_slide() # Perception Subsystem Tree
s3 = create_slide() # Dual-Brain Compute & Safety Tree
s4 = create_slide() # Assistive HMI & Actuation Tree
s5 = create_slide() # Power & Cloud Infrastructure Tree
s6 = create_slide() # Master Consolidated Tree

# ==============================================================================
# SLIDE 1: 4-BLOCK EXECUTIVE OVERVIEW (MAIN MENU)
# ==============================================================================
add_header(s1, "SMART INTELLIGENT CANE — EXECUTIVE SYSTEM ARCHITECTURE",
           "Interactive Architecture: Click any of the 4 core architecture blocks below to drill down into its detailed Tree Structure")

# Quick specs strip
strip = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.35))
strip.fill.solid()
strip.fill.fore_color.rgb = RGBColor(15, 23, 42)
strip.line.color.rgb = C_BORDER
tf = strip.text_frame
p = tf.paragraphs[0]
p.text = "⚡ 50ms Deterministic Safety Loop  |  📷 Dual AI Cameras (Top + Ground)  |  🌡️ Dual Spatial PIRs  |  🎧 Bluetooth Ear Assistant  |  🔋 36h Battery Runtime"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = C_TEXT_P
p.alignment = PP_ALIGN.CENTER

# 4 Main Blocks Layout
col_w = Inches(2.78)
col_h = Inches(4.55)
gap = Inches(0.2)
start_x = Inches(0.8)
start_y = Inches(1.95)

blocks_data = [
    {
        "num": "BLOCK 1",
        "title": "Multi-Modal Perception\n& Sensing Layer",
        "accent": C_BLUE,
        "badge": "8 SENSORS • DUAL-TIER",
        "desc": "Full-body 360° environmental awareness from head height to pavement level:",
        "bullets": [
            "Top Forward Camera (OV5647 CSI-2)",
            "Bottom Ground Camera (120° USB UVC)",
            "Ultrasonic Sensor (40kHz JSN-SR04T)",
            "Laser ToF Step Sensor (VL53L1X)",
            "Dual Spatial PIRs (Torso + Blind Spot)",
            "BMI270 6-DOF IMU + Water Contact Pins"
        ],
        "target": s2
    },
    {
        "num": "BLOCK 2",
        "title": "Dual-Processor Brain\n& Safety Core",
        "accent": C_RED,
        "badge": "RTOS + LINUX EDGE AI",
        "desc": "Asymmetric computing separating hard safety reflex from computer vision:",
        "bullets": [
            "ESP32-S3 Safety Core (Always-On)",
            "50ms Deterministic FreeRTOS Loop",
            "Zero-Lag Hazard Priority Arbitration",
            "Raspberry Pi Zero 2 W (Switchable)",
            "YOLO-Fastest & MobileNet Vision AI",
            "Whisper.tflite Voice AI + 921k UART"
        ],
        "target": s3
    },
    {
        "num": "BLOCK 3",
        "title": "Assistive Output, HMI\n& Actuation Layer",
        "accent": C_GREEN,
        "badge": "EARS-FREE AUDIO + HAPTICS",
        "desc": "Multi-channel sensory feedback leaving ears open for environmental hearing:",
        "bullets": [
            "Bluetooth 5.x Bone-Conduction Ear Link",
            "Top Apex Voice Mic (Mouth Aligned)",
            "DRV2605L Haptic Palm Reflex (<15ms)",
            "4x Tactile Braille Buttons (V, E, I, P)",
            "Guarded Recessed Emergency SOS",
            "Quad-Pod Motorized Adaptive Tip"
        ],
        "target": s4
    },
    {
        "num": "BLOCK 4",
        "title": "Power Distribution,\nCellular & Cloud",
        "accent": C_CYAN,
        "badge": "5 RAILS • STANDALONE SOS",
        "desc": "Fail-safe energy management and direct cellular emergency dispatch:",
        "bullets": [
            "1S2P 6800 mAh Li-Ion Battery Pack",
            "5 Isolated Switched Regulated Rails",
            "36+ Hours Runtime in Power-Save",
            "SIM7600G-H LTE Cat-4 & GNSS Module",
            "Autonomous Direct-AT SOS (No Pi needed)",
            "Caregiver IoT Telemetry & Geo-Fencing"
        ],
        "target": s5
    }
]

for i, b in enumerate(blocks_data):
    bx = start_x + i * (col_w + gap)
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, start_y, col_w, col_h)
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD
    card.line.color.rgb = b["accent"]
    card.line.width = Pt(1.5)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.18)
    tf.margin_left = Inches(0.18)
    tf.margin_right = Inches(0.18)

    p0 = tf.paragraphs[0]
    p0.text = f"{b['num']}  •  {b['badge']}"
    p0.font.size = Pt(8)
    p0.font.bold = True
    p0.font.color.rgb = b["accent"]

    p1 = tf.add_paragraph()
    p1.text = b["title"]
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_H
    p1.space_before = Pt(4)
    p1.space_after = Pt(4)

    p2 = tf.add_paragraph()
    p2.text = b["desc"]
    p2.font.size = Pt(8)
    p2.font.color.rgb = C_TEXT_M
    p2.space_after = Pt(6)

    for bullet in b["bullets"]:
        pb = tf.add_paragraph()
        pb.text = f"• {bullet}"
        pb.font.size = Pt(8.5)
        pb.font.color.rgb = C_TEXT_P
        pb.space_after = Pt(2)

    # Click to expand button
    btn = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx + Inches(0.15), start_y + col_h - Inches(0.65), col_w - Inches(0.3), Inches(0.45))
    btn.fill.solid()
    btn.fill.fore_color.rgb = RGBColor(15, 23, 42)
    btn.line.color.rgb = b["accent"]
    btn.line.width = Pt(1.5)
    btf = btn.text_frame
    bp = btf.paragraphs[0]
    bp.text = "CLICK TO EXPAND TREE ➔"
    bp.font.size = Pt(8.5)
    bp.font.bold = True
    bp.font.color.rgb = b["accent"]
    bp.alignment = PP_ALIGN.CENTER
    btn.click_action.target_slide = b["target"]
    card.click_action.target_slide = b["target"]

fn = s1.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.4))
ftf = fn.text_frame
fp = ftf.paragraphs[0]
fp.text = "Tip: In PowerPoint Slide Show Mode (F5), clicking any block acts as an interactive button that opens that subsystem's full tree architecture."
fp.font.size = Pt(8.5)
fp.font.italic = True
fp.font.color.rgb = C_TEXT_M
fp.alignment = PP_ALIGN.CENTER

# ==============================================================================
# HELPER: DRAW LINES USING THIN RECTANGLES (PowerPoint COM compatible)
# ==============================================================================
def draw_line_v(slide, cx, y1, y2, color, width_pt=2):
    """Draw a vertical line as a thin rectangle from (cx, y1) to (cx, y2)."""
    w = Pt(width_pt)
    h = y2 - y1
    if h <= 0:
        return
    x = cx - w // 2
    ln = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y1, w, h)
    ln.fill.solid()
    ln.fill.fore_color.rgb = color
    ln.line.fill.background()
    ln.rotation = 0.0

def draw_line_h(slide, x1, x2, cy, color, width_pt=2):
    """Draw a horizontal line as a thin rectangle from (x1, cy) to (x2, cy)."""
    h = Pt(width_pt)
    w = x2 - x1
    if w <= 0:
        return
    y = cy - h // 2
    ln = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x1, y, w, h)
    ln.fill.solid()
    ln.fill.fore_color.rgb = color
    ln.line.fill.background()
    ln.rotation = 0.0

# ==============================================================================
# HIERARCHICAL TOP-DOWN TREE LAYOUT FUNCTION (SLIDES 2, 3, 4, 5)
# ==============================================================================
def draw_topdown_tree(slide, title, subtitle, root_name, root_accent, subtrees):
    add_header(slide, title, subtitle, target_home_slide=s1)

    # 1. TOP ROOT NODE (Centered)
    root_w = Inches(5.8)
    root_h = Inches(0.68)
    root_x = Inches(3.766)
    root_y = Inches(1.35)

    root = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, root_x, root_y, root_w, root_h)
    root.fill.solid()
    root.fill.fore_color.rgb = C_CARD
    root.line.color.rgb = root_accent
    root.line.width = Pt(2)
    rtf = root.text_frame
    rtf.word_wrap = True
    rp0 = rtf.paragraphs[0]
    rp0.text = f"ROOT ARCHITECTURAL BLOCK: {root_name.upper()}"
    rp0.font.size = Pt(9.5)
    rp0.font.bold = True
    rp0.font.color.rgb = root_accent
    rp0.alignment = PP_ALIGN.CENTER

    rp1 = rtf.add_paragraph()
    rp1.text = "Hierarchical Tree: Subsystems ➔ Dedicated Hardware Modules ➔ Software Drivers & Protocols"
    rp1.font.size = Pt(7.8)
    rp1.font.color.rgb = C_TEXT_M
    rp1.alignment = PP_ALIGN.CENTER

    # 2. MAIN BUS CONNECTOR BAR
    bus_y = Inches(2.25)
    # Vertical trunk from root down to bus
    draw_line_v(slide, root_x + root_w // 2, root_y + root_h, bus_y, root_accent, width_pt=2)

    # 3. SUBTREE COLUMNS
    num_sub = len(subtrees)
    sub_w = Inches(2.78)
    gap = Inches(0.2)
    total_w = num_sub * sub_w + (num_sub - 1) * gap
    start_x = Inches(0.8) + (Inches(11.733) - total_w) // 2

    # Horizontal bus bar across all sub-branches
    bus_left = start_x + sub_w // 2
    bus_right = start_x + total_w - sub_w // 2
    draw_line_h(slide, bus_left, bus_right, bus_y, root_accent, width_pt=2)

    for s_idx, sub in enumerate(subtrees):
        sx = start_x + s_idx * (sub_w + gap)
        sy = Inches(2.55)

        # Drop line from bus bar to branch header
        draw_line_v(slide, sx + sub_w // 2, bus_y, sy, sub.get("color", root_accent), width_pt=2)

        # Branch Header Card
        sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, sy, sub_w, Inches(0.58))
        sh.fill.solid()
        sh.fill.fore_color.rgb = RGBColor(15, 23, 42)
        sh.line.color.rgb = sub.get("color", root_accent)
        sh.line.width = Pt(1.5)
        shtf = sh.text_frame
        shtf.word_wrap = True
        shp0 = shtf.paragraphs[0]
        shp0.text = sub["branch_name"]
        shp0.font.size = Pt(9)
        shp0.font.bold = True
        shp0.font.color.rgb = sub.get("color", root_accent)
        shp0.alignment = PP_ALIGN.CENTER
        shp1 = shtf.add_paragraph()
        shp1.text = sub.get("branch_tag", "Subsystem")
        shp1.font.size = Pt(7.2)
        shp1.font.color.rgb = C_TEXT_M
        shp1.alignment = PP_ALIGN.CENTER

        # Child Cards stacked vertically under this branch
        child_start_y = sy + Inches(0.68)
        card_h = Inches(1.10)
        card_gap = Inches(0.12)

        for c_idx, child in enumerate(sub["children"]):
            cy = child_start_y + c_idx * (card_h + card_gap)

            # Vertical line between branch header and child, or between child cards
            if c_idx == 0:
                draw_line_v(slide, sx + sub_w // 2, sy + Inches(0.58), cy, sub.get("color", root_accent), width_pt=1)
            else:
                prev_cy = child_start_y + (c_idx - 1) * (card_h + card_gap)
                draw_line_v(slide, sx + sub_w // 2, prev_cy + card_h, cy, sub.get("color", root_accent), width_pt=1)

            c_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, cy, sub_w, card_h)
            c_card.fill.solid()
            c_card.fill.fore_color.rgb = C_CARD
            c_card.line.color.rgb = child.get("border", C_BORDER)
            c_card.line.width = Pt(1)

            ctf = c_card.text_frame
            ctf.word_wrap = True
            ctf.margin_top = Inches(0.06)
            ctf.margin_left = Inches(0.1)
            ctf.margin_right = Inches(0.1)

            cp0 = ctf.paragraphs[0]
            cp0.text = child["name"]
            cp0.font.size = Pt(8.5)
            cp0.font.bold = True
            cp0.font.color.rgb = C_TEXT_H

            cp1 = ctf.add_paragraph()
            cp1.text = f"Part: {child.get('part', 'N/A')} • Bus: {child.get('bus', 'N/A')}"
            cp1.font.size = Pt(7.2)
            cp1.font.color.rgb = C_BLUE

            cp2 = ctf.add_paragraph()
            cp2.text = f"Power: {child.get('power', 'N/A')} • Rate: {child.get('rate', 'N/A')}"
            cp2.font.size = Pt(7)
            cp2.font.color.rgb = C_AMBER

            cp3 = ctf.add_paragraph()
            cp3.text = child.get("desc", "")
            cp3.font.size = Pt(7)
            cp3.font.color.rgb = C_TEXT_P

# --- SUBTREES DEFINITIONS ---

subtrees_p = [
    {
        "branch_name": "1. Optical Vision Suite",
        "branch_tag": "Dual-Camera Semantic Vision",
        "color": C_BLUE,
        "children": [
            {
                "name": "Top Forward Camera (CAM1)",
                "part": "OmniVision OV5647 (5MP)",
                "bus": "22-pin CSI-2 to RPi",
                "power": "5V_PI (250mA)",
                "rate": "30 fps @ 1080p",
                "desc": "Scene comprehension, sign text OCR, crosswalks & pedestrian detection."
            },
            {
                "name": "Bottom Pavement Camera (CAM2)",
                "part": "Wide 120° Mini CMOS",
                "bus": "USB UVC / CSI Mux",
                "power": "5V_PI (190mA)",
                "rate": "30 fps ground flow",
                "desc": "Angled 35° down: Real-time curb, stair, pothole & drop-off segmentation.",
                "border": C_AMBER
            },
            {
                "name": "Optical Vision AI Pipeline",
                "part": "YOLO-Fastest + MobileNet",
                "bus": "V4L2 Pipeline (Linux)",
                "power": "Included in Pi",
                "rate": "15 fps quantized",
                "desc": "Fused visual inference delivering obstacle tokens to audio guidance engine."
            }
        ]
    },
    {
        "branch_name": "2. Acoustic & Laser Ranging",
        "branch_tag": "Zero-Lag Reflex Safety Path",
        "color": C_RED,
        "children": [
            {
                "name": "Ultrasonic Sensor (SEN1)",
                "part": "Waterproof JSN-SR04T (40kHz)",
                "bus": "GPIO Trigger/Echo (ESP32)",
                "power": "5V_AUX (15mA)",
                "rate": "20 Hz (50ms cycle)",
                "desc": "Acoustic distance ranging (20-450cm); triggers palm haptics directly.",
                "border": C_RED
            },
            {
                "name": "Laser ToF Step Sensor (SEN2)",
                "part": "ST VL53L1X (940nm VCSEL)",
                "bus": "Diff I2C (PCA9615 buffer)",
                "power": "3V3_MAIN (16mA)",
                "rate": "50 Hz (20ms)",
                "desc": "Millimeter pavement distance profiling; detects curbs & >8cm drop-offs.",
                "border": C_RED
            },
            {
                "name": "Liquid Water Contact Pins (SEN5)",
                "part": "Gold Electrode Contact Pins",
                "bus": "Analog ADC (ESP32-S3)",
                "power": "3V3_MAIN (<10µA)",
                "rate": "Polled every 50ms",
                "desc": "Conductivity drop alerts user to standing water puddles before stepping."
            }
        ]
    },
    {
        "branch_name": "3. Spatial Thermal Motion",
        "branch_tag": "Pedestrian & Blind-Spot Guard",
        "color": C_AMBER,
        "children": [
            {
                "name": "Upper Spatial PIR (SEN3)",
                "part": "Panasonic PaPIRs (120° FOV)",
                "bus": "Hardware INT (ESP32-S3)",
                "power": "3V3_MAIN (<50µA)",
                "rate": "Asynchronous IRQ",
                "desc": "Mounted at torso height; detects approaching pedestrians & cyclists 4m away.",
                "border": C_AMBER
            },
            {
                "name": "Lower Peripheral PIR (SEN4)",
                "part": "Dual-Element Miniature PIR",
                "bus": "TCA9555 Expander INT",
                "power": "3V3_MAIN (<50µA)",
                "rate": "Asynchronous IRQ",
                "desc": "Low-angle blind spot detection for moving pets, children, and scooters.",
                "border": C_AMBER
            },
            {
                "name": "PIR Thermal Filter Engine",
                "part": "ESP32 Firmware Interrupt ISR",
                "bus": "FreeRTOS Event Group",
                "power": "N/A (Firmware)",
                "rate": "<1ms wake latency",
                "desc": "Differentiates moving human heat signatures from ambient temperature drift."
            }
        ]
    },
    {
        "branch_name": "4. Inertial & Vitals Tracking",
        "branch_tag": "Fall Detection & User Health",
        "color": C_PURPLE,
        "children": [
            {
                "name": "6-DOF IMU Sensor (U4)",
                "part": "Bosch BMI270 (Ultra-low noise)",
                "bus": "Diff I2C (Addr 0x68)",
                "power": "3V3_MAIN (680µA)",
                "rate": "100 Hz continuous",
                "desc": "Freefall detection, impact spike trigger, gait cadence & terrain vibration FFT.",
                "border": C_RED
            },
            {
                "name": "MAX30102 PPG Optical Vitals (U5)",
                "part": "Maxim MAX30102 Heart/SpO2",
                "bus": "Handle I2C (Addr 0x57)",
                "power": "3V3_MAIN (600µA)",
                "rate": "25 Hz PPG",
                "desc": "Monitors palm pulse and blood oxygen; validates consciousness post-fall."
            },
            {
                "name": "Cadence & Freefall Algorithm",
                "part": "Firmware Core 0 Classifier",
                "bus": "FreeRTOS Safety Loop",
                "power": "N/A (Firmware)",
                "rate": "10ms evaluation",
                "desc": "Dual-threshold fall detection: freefall + high-G impact + 5s immobility."
            }
        ]
    }
]

subtrees_c = [
    {
        "branch_name": "1. ESP32-S3 Safety Core (HW)",
        "branch_tag": "Always-On Hard Safety Master",
        "color": C_RED,
        "children": [
            {
                "name": "ESP32-S3-WROOM-1 (U1)",
                "part": "Dual Xtensa LX7 @ 240MHz",
                "bus": "I2C, 2x I2S, 3x UART, ADC",
                "power": "3V3_MAIN (Always-On)",
                "rate": "240 MHz clock",
                "desc": "Hardware root of trust; owns all safety sensors, haptics, and autonomous SOS.",
                "border": C_RED
            },
            {
                "name": "TCA9555 16-Bit Expander (U7)",
                "part": "TI TCA9555 I2C Expander",
                "bus": "I2C (Addr 0x20) + INT",
                "power": "3V3_MAIN (5µA)",
                "rate": "100 kHz I2C",
                "desc": "Gates power switches for Pi, cameras, and modem to enforce power saving."
            },
            {
                "name": "PCA9615 Differential Buffer",
                "part": "NXP PCA9615 I2C Buffer",
                "bus": "Differential dI2C Pair",
                "power": "3V3_MAIN (12mA)",
                "rate": "400 kHz over 1.2m",
                "desc": "Guarantees noise-immune I2C communication along cane shaft to tip sensors."
            }
        ]
    },
    {
        "branch_name": "2. FreeRTOS Safety Firmware",
        "branch_tag": "Deterministic 50ms Real-Time Loop",
        "color": C_RED,
        "children": [
            {
                "name": "50ms Deterministic Safety Loop",
                "part": "FreeRTOS Real-Time Scheduler",
                "bus": "Core 0 Task (Priority 10)",
                "power": "N/A (Firmware)",
                "rate": "Strict 50.0ms cycle",
                "desc": "Executes 5 synchronized safety evaluations: Fall > Drop-off > Obstacle > Water.",
                "border": C_RED
            },
            {
                "name": "DRV2605L Haptic Engine Driver",
                "part": "I2C Waveform Synthesizer",
                "bus": "Handle I2C (Addr 0x5A)",
                "power": "3V3_MAIN",
                "rate": "<15ms trigger latency",
                "desc": "Synthesizes distinct vibrotactile waveforms directly into user's palm."
            },
            {
                "name": "Autonomous Direct-AT Modem Link",
                "part": "UART AT Command Sequencer",
                "bus": "UART1 to SIM7600G",
                "power": "N/A (Firmware)",
                "rate": "115,200 baud direct",
                "desc": "Dispatches emergency SMS and 112 call autonomously without Raspberry Pi."
            }
        ]
    },
    {
        "branch_name": "3. Raspberry Pi Zero 2 W (HW)",
        "branch_tag": "Switchable Edge AI Gateway",
        "color": C_PURPLE,
        "children": [
            {
                "name": "Raspberry Pi Zero 2 W (U2)",
                "part": "Broadcom BCM2710A1",
                "bus": "CSI-2, USB OTG, UART, BLE",
                "power": "5V_PI (Switched rail)",
                "rate": "Quad 1.0 GHz Cortex-A53",
                "desc": "Runs computer vision models, Whisper voice engine, and Bluetooth ear link."
            },
            {
                "name": "Bluetooth 5.x BLE Transceiver",
                "part": "Dedicated Audio Module",
                "bus": "UART / PCM Audio Link",
                "power": "3V3_MAIN / 5V_PI",
                "rate": "2.4 GHz A2DP / LE Audio",
                "desc": "Streams spoken guidance and obstacle tones to bone-conduction ear assistant.",
                "border": C_GREEN
            },
            {
                "name": "Inter-Processor UART Bridge",
                "part": "4-Wire Framed Serial Protocol",
                "bus": "Mini-UART + RTS/CTS + IRQ",
                "power": "3.3V Logic Level",
                "rate": "921,600 baud packetized",
                "desc": "Bidirectional link exchanging obstacle tokens, voice chunks, and system health."
            }
        ]
    },
    {
        "branch_name": "4. Edge AI Software Stack",
        "branch_tag": "Vision, Voice & Scene Engine",
        "color": C_PURPLE,
        "children": [
            {
                "name": "Dual-Camera Vision Inference",
                "part": "YOLO-Fastest + MobileNet SSD",
                "bus": "TFLite Int8 Engine",
                "power": "N/A (Software)",
                "rate": "12-15 fps inference",
                "desc": "Identifies obstacles, stairs, crosswalk signals, storefronts, and text OCR."
            },
            {
                "name": "Whisper.tflite Voice Assistant",
                "part": "Local Speech-to-Text Model",
                "bus": "ALSA Audio Pipeline",
                "power": "N/A (Software)",
                "rate": "Triggered on 'V' hold",
                "desc": "Transcribes user voice queries; pairs with cloud Gemini API for natural dialog."
            },
            {
                "name": "Context & Caregiver Sync Engine",
                "part": "MQTT Client + Local SQLite",
                "bus": "SIM7600 USB Network Link",
                "power": "N/A (Software)",
                "rate": "60s telemetry push",
                "desc": "Maintains offline queue; syncs GPS tracks and incident logs to cloud."
            }
        ]
    }
]

subtrees_h = [
    {
        "branch_name": "1. Audio Guidance & Ear Assistant",
        "branch_tag": "Ears-Free Wireless Navigation",
        "color": C_GREEN,
        "children": [
            {
                "name": "Bluetooth Ear Assistant Transceiver",
                "part": "Dedicated BT 5.x / LE Audio",
                "bus": "UART/PCM to RPi Zero 2 W",
                "power": "3V3_MAIN (18mA streaming)",
                "rate": "Sub-30ms audio latency",
                "desc": "Guides user via bone-conduction headphones; keeps ears open for traffic.",
                "border": C_GREEN
            },
            {
                "name": "Top Apex Voice Microphone (MIC1)",
                "part": "Knowles SPH0645LM4H High-SNR",
                "bus": "I2S Audio Bus (64x Fs)",
                "power": "3V3_MAIN (1.4mA active)",
                "rate": "16 kHz / 24-bit PCM",
                "desc": "Acoustic port on top cap directed at mouth for crystal-clear voice AI commands.",
                "border": C_AMBER
            },
            {
                "name": "Thumb-Arch Tri-Mic Array",
                "part": "3x Knowles MEMS Microphones",
                "bus": "I2S0 (Stereo) + I2S1 to ESP32",
                "power": "3V3_MAIN (3.5mA total)",
                "rate": "Spatial beamforming",
                "desc": "Suppresses wind noise and detects approaching sirens or vehicle horns."
            },
            {
                "name": "Handle Siren & Speaker Amp (U8)",
                "part": "MAX98357A I2S Class-D Amp",
                "bus": "I2S1 Bus (shared clocks)",
                "power": "5V_AUX (600mA loud siren)",
                "rate": "Up to 92 dBA alarm",
                "desc": "High-decibel audible emergency siren alerts passersby during a fall or distress."
            }
        ]
    },
    {
        "branch_name": "2. Palm Haptics & Tactile Inputs",
        "branch_tag": "Sub-15ms Tactile Reflex Interface",
        "color": C_AMBER,
        "children": [
            {
                "name": "DRV2605L Haptic Motor Driver",
                "part": "TI DRV2605L + Grip LRA Motor",
                "bus": "Handle I2C (Addr 0x5A)",
                "power": "3V3_MAIN (80mA pulse)",
                "rate": "<15ms reflex trigger",
                "desc": "Immediate palm vibration: Proximity ticks, curb double-pulse, and emergency buzz.",
                "border": C_RED
            },
            {
                "name": "4x Tactile Braille Buttons",
                "part": "Raised Braille Tactile Switches",
                "bus": "Dedicated GPIOs (Active-Low)",
                "power": "Internal Pull-Up",
                "rate": "10ms debounced IRQ",
                "desc": "V (Voice AI), E (Environment summary), I (Incident tag), P (Power toggle)."
            },
            {
                "name": "Guarded Emergency SOS Button",
                "part": "Recessed Switch with Guard Ring",
                "bus": "ESP32 Deep Sleep Wake GPIO",
                "power": "Pull-Up to 3V3_MAIN",
                "rate": "2-second hold required",
                "desc": "Prevents accidental press; 2s hold triggers autonomous SMS/Call with GPS.",
                "border": C_RED
            }
        ]
    },
    {
        "branch_name": "3. Mechanical Quad-Pod Stabilization",
        "branch_tag": "Motorized Adaptive Terrain Tip",
        "color": C_BLUE,
        "children": [
            {
                "name": "Quad-Pod Tip Motor Driver",
                "part": "TI DRV8830 I2C Motor Driver",
                "bus": "Diff I2C (Addr 0x60)",
                "power": "VBAT_MOTOR (Fused 3.7V)",
                "rate": "1.2s deployment time",
                "desc": "Drives miniature DC gear-motor and lead screw collar to expand support legs."
            },
            {
                "name": "3 Articulated Folding Support Legs",
                "part": "CNC Aluminum Linkage Legs",
                "bus": "Mechanical Lead Screw Hub",
                "power": "N/A (Mechanical)",
                "rate": "Full 4-point ground base",
                "desc": "Deploys automatically on rough gravel or inclines; allows cane to self-stand."
            },
            {
                "name": "Ergonomic Thumb-Arch Handle",
                "part": "Overmolded Polycarbonate Chassis",
                "bus": "Keyed 20-Pin Joint J1",
                "power": "N/A (Mechanical)",
                "rate": "Rated for 50 kg load",
                "desc": "Optimized palm posture, integrated camera pod, and quick-release latch."
            }
        ]
    }
]

subtrees_w = [
    {
        "branch_name": "1. Energy Storage & Charging",
        "branch_tag": "1S2P 6800 mAh Li-Ion Architecture",
        "color": C_CYAN,
        "children": [
            {
                "name": "1S2P 6800 mAh Li-Ion Battery",
                "part": "2x Panasonic NCR18650GA",
                "bus": "Direct Raw Cell (VSYS)",
                "power": "3.0V to 4.2V (24.5 Wh)",
                "rate": "Up to 8A burst current",
                "desc": "Single-cell parallel configuration eliminates cell balancing failure modes.",
                "border": C_CYAN
            },
            {
                "name": "BQ25895 USB-C Fast Charger",
                "part": "TI BQ25895 Switch-Mode Charger",
                "bus": "USB-C CC1/CC2 PD Logic",
                "power": "Up to 3.0A fast charge",
                "rate": "93% charging efficiency",
                "desc": "Charges cane in <2.5 hours with thermal regulation and overvoltage protection."
            },
            {
                "name": "BQ27441 Fuel Gauge IC",
                "part": "TI BQ27441-G1 System-Side Gauge",
                "bus": "I2C Bus (Addr 0x55)",
                "power": "VSYS (<50µA draw)",
                "rate": "1 Hz state-of-charge",
                "desc": "Provides accurate battery state-of-charge (%) to drive power-save transitions."
            }
        ]
    },
    {
        "branch_name": "2. Five Isolated Switched Rails",
        "branch_tag": "Independent Rail Gating Architecture",
        "color": C_CYAN,
        "children": [
            {
                "name": "3V3_MAIN Rail (Always-On)",
                "part": "TPS63020 Buck-Boost Regulator",
                "bus": "Powers ESP32, IMU, ToF, Mics",
                "power": "3.30V @ up to 2.0A",
                "rate": "96% efficiency",
                "desc": "Seamless 3.3V regulation across full 3.0V-4.2V battery discharge curve.",
                "border": C_RED
            },
            {
                "name": "5V_PI Rail (Switched)",
                "part": "TPS61088 Boost + TPS22918 Switch",
                "bus": "Powers Pi Zero 2 W & Cams",
                "power": "5.0V @ up to 2.5A",
                "rate": "Switched by TCA9555 P00",
                "desc": "Cleanly disabled in POWER_SAVE mode (<20% battery) to extend runtime to 36+ hrs."
            },
            {
                "name": "5V_AUX Rail (Switched)",
                "part": "TPS61088 Boost + TPS22918 Switch",
                "bus": "Powers Ultrasonic & Audio Amp",
                "power": "5.0V @ up to 1.0A",
                "rate": "Switched by TCA9555 P03",
                "desc": "Stays active during POWER_SAVE mode so ultrasonic safety protection never stops."
            },
            {
                "name": "VBAT_MODEM & VBAT_MOTOR",
                "part": "Dedicated TPS22918 Load Switches",
                "bus": "Direct VSYS with 1000µF cap",
                "power": "Raw Cell (3.0V - 4.2V)",
                "rate": "2.0A peak RF bursts",
                "desc": "Isolates noisy modem bursts and motor inrush from sensitive digital sensors."
            }
        ]
    },
    {
        "branch_name": "3. Cellular SOS & Cloud IoT",
        "branch_tag": "Dual-Link Autonomous Emergency Link",
        "color": C_PINK,
        "children": [
            {
                "name": "SIM7600G-H LTE & GNSS Module",
                "part": "Global LTE Cat-4 + Multi-GNSS",
                "bus": "Dual: UART (ESP) + USB (Pi)",
                "power": "VBAT_MODEM (2A bursts)",
                "rate": "150 Mbps DL / 50 Mbps UL",
                "desc": "Dual-path cellular modem allowing autonomous SOS calls from ESP32-S3.",
                "border": C_RED
            },
            {
                "name": "Autonomous Emergency SOS Dispatch",
                "part": "Direct AT Command Firmware",
                "bus": "ESP32-S3 UART1 to Modem",
                "power": "Active in all modes",
                "rate": "<5s dispatch latency",
                "desc": "Sends emergency SMS with Google Maps pin & places 112 calls without needing Pi.",
                "border": C_RED
            },
            {
                "name": "Caregiver IoT Cloud Dashboard",
                "part": "MQTT TLS 1.3 / REST API",
                "bus": "Cellular IP Socket (RPi)",
                "power": "Cloud Infrastructure",
                "rate": "60s heartbeat telemetry",
                "desc": "Caregiver portal: Real-time map location, fall incident history & geo-fence alerts."
            }
        ]
    }
]

all_pillars = [
    {
        "title": "1. Multi-Modal Perception",
        "color": C_BLUE,
        "tag": "Sensors & Drivers",
        "nodes": [
            ("Top Forward Camera (CAM1)", "OV5647 5MP • CSI-2 (22-pin)"),
            ("Bottom Ground Camera (CAM2)", "120° Wide • USB UVC • Curbs/Stairs", C_AMBER),
            ("Ultrasonic Rangefinder (SEN1)", "JSN-SR04T 40kHz • 50ms Safety Loop", C_RED),
            ("Laser ToF Step Sensor (SEN2)", "ST VL53L1X • Diff I2C • Drop-offs", C_RED),
            ("Upper Spatial PIR (SEN3)", "Panasonic 120° • Pedestrian IRQ", C_AMBER),
            ("Lower Blind-Spot PIR (SEN4)", "Low-angle blind spot detection", C_AMBER),
            ("6-DOF IMU Sensor (U4)", "BMI270 100Hz • Freefall Spike", C_RED),
            ("MAX30102 PPG + Water Pins", "Heart Rate/SpO2 + Puddle Immersion")
        ]
    },
    {
        "title": "2. Dual-Processor Brain",
        "color": C_RED,
        "tag": "RTOS Safety + Edge AI",
        "nodes": [
            ("ESP32-S3 Safety Core (U1)", "Dual Xtensa 240MHz • Always-On", C_RED),
            ("50ms FreeRTOS Safety Loop", "Deterministic Priority Arbitration", C_RED),
            ("DRV2605L Haptic Engine", "Sub-15ms Palm Reflex Waveforms", C_RED),
            ("TCA9555 Expander & Load Switch", "Gates Rails for 36h Power-Save"),
            ("Raspberry Pi Zero 2 W (U2)", "Quad Cortex-A53 1.0 GHz • Switchable"),
            ("Dual-Camera Vision Pipeline", "YOLO-Fastest & MobileNet Int8"),
            ("Whisper.tflite Voice Assistant", "Local STT + Cloud Multimodal NLP"),
            ("Inter-Processor UART Bridge", "Framed 4-Wire Serial @ 921,600 baud")
        ]
    },
    {
        "title": "3. Assistive Output & HMI",
        "color": C_GREEN,
        "tag": "Audio, Haptics & Legs",
        "nodes": [
            ("Bluetooth Ear Assistant (U3)", "Dedicated BLE/A2DP Bone Conduction", C_GREEN),
            ("Top Apex Voice Mic (MIC1)", "Mouth-Aligned Acoustic Port", C_AMBER),
            ("Thumb-Arch Tri-Mic Array", "Spatial Beamforming & Sirens"),
            ("DRV2605L Haptic Palm Motor", "Linear Resonant Actuator (LRA)", C_RED),
            ("Tactile Braille Buttons", "V (Voice), E (Env), I (Inc), P (Pwr)"),
            ("Guarded Emergency SOS Button", "Recessed Switch • 2s Hold Dispatches", C_RED),
            ("MAX98357A 92dBA Siren", "Audible Siren for Falls & Distress"),
            ("Quad-Pod Adaptive Tip", "DRV8830 Motor + 3 Articulated Legs")
        ]
    },
    {
        "title": "4. Power, Cellular & Cloud",
        "color": C_CYAN,
        "tag": "5 Rails & IoT Cloud",
        "nodes": [
            ("1S2P 6800 mAh Li-Ion Pack", "2x 18650 Cells • USB-C Fast Charge", C_CYAN),
            ("3V3_MAIN Buck-Boost Rail", "TPS63020 Always-On • Full 3.0-4.2V", C_RED),
            ("5V_PI Switched Boost Rail", "TPS61088 Boost • Powers Pi/Cameras"),
            ("5V_AUX Switched Boost Rail", "Independent switch for Ultrasonic"),
            ("SIM7600G-H LTE & GNSS", "Multi-band 4G + GPS/GLONASS", C_RED),
            ("Autonomous Direct-AT SOS", "Dispatches SMS/Call without RPi", C_RED),
            ("Caregiver IoT Cloud Portal", "MQTT TLS 1.3 • Live GPS Tracking"),
            ("4-Stage Power State Machine", "Normal > Power-Save (36h) > SOS")
        ]
    }
]


# Draw Slides 2, 3, 4, 5 with Top-Down Clean Tree
draw_topdown_tree(s2, "MULTI-MODAL PERCEPTION & SENSING SUBSYSTEM TREE",
                  "Detailed Tree: 8 Multi-Modal Sensors with Buses, Voltages, Rates, and Fail-Safe Paths",
                  "Multi-Modal Perception & Sensing", C_BLUE, subtrees_p)

draw_topdown_tree(s3, "DUAL-PROCESSOR BRAIN & REAL-TIME SAFETY TREE",
                  "Detailed Tree: ESP32-S3 Hard RTOS & Raspberry Pi Zero 2 W Edge AI Architecture",
                  "Dual-Processor Brain & Compute", C_RED, subtrees_c)

draw_topdown_tree(s4, "ASSISTIVE HMI, AUDIO GUIDANCE & ACTUATION TREE",
                  "Detailed Tree: Bone-Conduction Ear Assistant, Top Voice Mic, Palm Haptics & Adaptive Tip",
                  "Assistive HMI & Output Actuation", C_GREEN, subtrees_h)

draw_topdown_tree(s5, "POWER DISTRIBUTION, CELLULAR SOS & CLOUD TREE",
                  "Detailed Tree: 5 Switched Rails, 6800mAh Battery, SIM7600G Modem & IoT Cloud",
                  "Power Distribution & Cloud Telemetry", C_CYAN, subtrees_w)

# ==============================================================================
# SLIDE 6: MASTER CONSOLIDATED SYSTEM ARCHITECTURE TREE (1-SLIDE MASTER)
# ==============================================================================
add_header(s6, "SMART INTELLIGENT CANE — MASTER SYSTEM ARCHITECTURE TREE",
           "Complete Consolidated Tree: 4 Architectural Pillars, Subsystems, Hardware Components & Software Dataflows",
           target_home_slide=s1)

m_col_w = Inches(2.78)
m_gap = Inches(0.2)
m_start_x = Inches(0.8)
m_start_y = Inches(1.42)

for col_idx, pil in enumerate(all_pillars):
    mx = m_start_x + col_idx * (m_col_w + m_gap)

    # Column Header
    ch = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, m_start_y, m_col_w, Inches(0.55))
    ch.fill.solid()
    ch.fill.fore_color.rgb = RGBColor(15, 23, 42)
    ch.line.color.rgb = pil["color"]
    ch.line.width = Pt(1.5)
    chtf = ch.text_frame
    chtf.word_wrap = True
    chp0 = chtf.paragraphs[0]
    chp0.text = pil["title"]
    chp0.font.size = Pt(9.5)
    chp0.font.bold = True
    chp0.font.color.rgb = pil["color"]
    chp1 = chtf.add_paragraph()
    chp1.text = pil["tag"]
    chp1.font.size = Pt(7.5)
    chp1.font.color.rgb = C_TEXT_M

    # Column Nodes
    node_y = m_start_y + Inches(0.62)
    for n_idx, n_item in enumerate(pil["nodes"]):
        n_name = n_item[0]
        n_desc = n_item[1]
        n_border = n_item[2] if len(n_item) > 2 else C_BORDER

        ny = node_y + n_idx * Inches(0.58)
        nc = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, ny, m_col_w, Inches(0.53))
        nc.fill.solid()
        nc.fill.fore_color.rgb = C_CARD
        nc.line.color.rgb = n_border
        nc.line.width = Pt(1)

        # Connector line between nodes
        if n_idx > 0:
            draw_line_v(s6, mx + Inches(0.15), ny - Inches(0.05), ny, pil["color"], width_pt=1)

        nctf = nc.text_frame
        nctf.word_wrap = True
        nctf.margin_top = Inches(0.04)
        nctf.margin_left = Inches(0.1)
        nctf.margin_right = Inches(0.1)

        np0 = nctf.paragraphs[0]
        np0.text = n_name
        np0.font.size = Pt(8)
        np0.font.bold = True
        np0.font.color.rgb = C_TEXT_H

        np1 = nctf.add_paragraph()
        np1.text = n_desc
        np1.font.size = Pt(6.8)
        np1.font.color.rgb = C_TEXT_P

# Save the presentation
output_pptx = "SmartCane_System_Architecture_SIH2026.pptx"
prs.save(output_pptx)
print(f"SUCCESS: PowerPoint saved to {output_pptx} with clean top-down tree architecture!")
