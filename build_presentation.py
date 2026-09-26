import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import traceback

def remove_shape(slide, shape):
    elm = shape.element
    elm.getparent().remove(elm)

def add_text_box(slide, left, top, width, height, text, font_size=12, bold=False):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    return txBox

def add_styled_text_box(slide, left, top, width, height, content_blocks):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    
    first = True
    for block in content_blocks:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
            
        run = p.add_run()
        run.text = block.get('text', '')
        run.font.size = Pt(block.get('size', 10))
        run.font.bold = block.get('bold', False)
        
        if 'color' in block:
            run.font.color.rgb = block['color']
            
    return txBox

try:
    template_path = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SIH2026-IDEA-Presentation-Format (1).pptx"
    output_path = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SmartCane_SIH2026_FINAL.pptx"
    
    prs = Presentation(template_path)
    
    # SLIDE 1
    slide1 = prs.slides[0]
    content_text1 = (
        "Problem Statement ID: [TO BE FILLED]\n"
        "Problem Statement Title: [TO BE FILLED - Smart Assistive Mobility Device]\n"
        "Theme: MedTech / Assistive Hardware & Robotics\n"
        "PS Category: Hardware\n"
        "Team ID: [TO BE FILLED]\n"
        "Team Name: [TO BE FILLED]\n"
        "College: R.V. College of Engineering, Bengaluru\n"
        "Project Name: SMART INTELLIGENT CANE\n"
        "Tagline: \"Asymmetric Dual-Processor Assistive Mobility Platform with Fail-Safe Reflex Safety\"\n\n"
        "⚡50ms Safety Loop | 📷 Dual AI Cameras | 🦴 Ears-Free Audio | 🔋 36h+ Battery | 🚨 Autonomous SOS | 🦿 Motorized Quad-Pod"
    )
    slide1.shapes[5].text_frame.clear()
    p = slide1.shapes[5].text_frame.add_paragraph()
    p.text = content_text1
    p.font.size = Pt(14)
    
    # SLIDE 2
    slide2 = prs.slides[1]
    slide2.shapes[1].text = "IDEA TITLE — Problem, Solution & Architecture"
    
    shapes_to_remove = []
    for i in range(7, len(slide2.shapes)):
        shapes_to_remove.append(slide2.shapes[i])
    for s in shapes_to_remove:
        remove_shape(slide2, s)
        
    left_col_text = (
        "PROBLEM:\n"
        "1. \"I can feel the ground with my cane, but I can't detect the low branch at head height.\"\n"
        "2. \"I never hear the electric scooter until it's too late.\"\n"
        "3. \"My smart cane uses earbuds, so I can't hear traffic anymore.\"\n"
        "4. \"The app crashed and I had no warning at the curb.\"\n"
        "5. Short 3-4 hour battery, no autonomous SOS if user falls unconscious.\n\n"
        "SOLUTION — 6 Pillars:\n"
        "1. ⚡ Asymmetric Dual-Processor Fail-Safe\n"
        "2. 📷 Dual-Tier 8-Sensor 360° Perception\n"
        "3. 🦴 Ears-Free Bone-Conduction\n"
        "4. ✋ Sub-15ms Haptic Palm Reflex\n"
        "5. 🚨 Autonomous Cellular SOS\n"
        "6. 🦿 Motorized Quad-Pod Tip\n\n"
        "UVP: \"World's first assistive cane with hardware-guaranteed safety reflex independent of any OS, with autonomous cellular SOS and ears-free guidance.\""
    )
    add_text_box(slide2, Inches(0.5), Inches(1.5), Inches(3.5), Inches(5.5), left_col_text, 10)
    
    arch_img = r"C:\Users\mohit\.gemini\antigravity\brain\13e1aa93-8675-42eb-a066-11ab86283371\system_architecture_1790429512186.jpg"
    if os.path.exists(arch_img):
        slide2.shapes.add_picture(arch_img, Inches(4.2), Inches(1.5), width=Inches(5.5))
        
    # SLIDE 3
    slide3 = prs.slides[2]
    slide3.shapes[1].text = "TECHNICAL APPROACH"
    remove_shape(slide3, slide3.shapes[2]) 
    
    flowchart_img = r"C:\Users\mohit\.gemini\antigravity\brain\13e1aa93-8675-42eb-a066-11ab86283371\methodology_flowchart_1790429568572.jpg"
    if os.path.exists(flowchart_img):
        slide3.shapes.add_picture(flowchart_img, Inches(0.5), Inches(1.5), width=Inches(4.5))
        
    right_text = (
        "Tech Stack Grid:\n"
        "• ESP32-S3 + FreeRTOS: Always-on safety, 50ms loop, C/C++\n"
        "• RPi Zero 2 W + Linux RT: Edge AI, YOLO-Fastest, MobileNetV3, Python\n"
        "• Computer Vision: YOLO-Fastest + MobileNetV3-SSD Int8 @ 12-15fps\n"
        "• Audio & HMI: BLE 5.x bone-conduction, Knowles MEMS mic array, Whisper STT\n"
        "• Power: TPS63020 Buck-Boost, BQ25895 charger, 5 isolated rails, 6800mAh Li-Ion\n"
        "• Cloud: SIM7600G-H LTE Cat-4 + GPS, MQTT/TLS, AWS/Firebase IoT\n"
        "• 3D CAD: Blender 5.2, 63K+ face mesh, CNC aluminum linkages\n"
        "• Mechanical: DRV8830 motor driver, quad-pod linkage, over-current protection\n\n"
        "Inter-Processor Bridge:\n"
        "ESP32-S3 ↔ RPi: 4-wire UART + RTS/CTS @ 921,600 baud (COBS + CRC16)\n"
        "PCA9615 Differential I²C for 1.1m shaft sensors"
    )
    add_text_box(slide3, Inches(5.2), Inches(1.5), Inches(4.5), Inches(3.5), right_text, 10)
    
    sensor_img = r"C:\Users\mohit\.gemini\antigravity\brain\13e1aa93-8675-42eb-a066-11ab86283371\sensor_coverage_map_1790429608010.jpg"
    if os.path.exists(sensor_img):
        slide3.shapes.add_picture(sensor_img, Inches(5.2), Inches(5.2), width=Inches(4.5))
        
    # SLIDE 4
    slide4 = prs.slides[3]
    slide4.shapes[1].text = "FEASIBILITY & VIABILITY"
    remove_shape(slide4, slide4.shapes[2])
    
    feasibility_text = (
        "Technical Feasibility\n"
        "• ESP32-S3 FreeRTOS: Industry-proven for safety-critical IoT\n"
        "• YOLO-Fastest + MobileNetV3 validated on RPi Zero 2 W at 12-15 fps\n"
        "• PCA9615 differential I²C validated up to 3m (shaft = 1.1m)\n"
        "• Complete 3D CAD (63K+ face mesh) manufacturing-ready\n\n"
        "Economic Viability\n"
        "• BOM: ₹8,000-12,000 (vs ₹50,000-2,00,000 for competitors)\n"
        "• Market: 12M+ VI in India (WHO), ~2% with smart aids. TAM: ₹9,600 Cr\n"
        "• Revenue: B2G (ADIP scheme), B2B, D2C, SaaS cloud dashboard\n"
        "• Aligned with: Accessible India Campaign, RPwD Act 2016"
    )
    add_text_box(slide4, Inches(0.5), Inches(1.5), Inches(4.5), Inches(3.5), feasibility_text, 10)
    
    op_text = (
        "Operational Feasibility\n"
        "• Zero smartphone dependency for safety\n"
        "• Offline-first: All safety + edge AI local\n"
        "• 4 Braille buttons: No screen needed\n"
        "• 36+ hours in Power-Save mode\n\n"
        "Challenges & Risk Mitigation\n"
        "1. AI accuracy in Indian conditions → Multi-modal redundancy (8 sensors)\n"
        "2. RPi crash during use → Asymmetric architecture; ESP32 safety continues\n"
        "3. Mechanical tip failure → IP54 enclosure, over-current shutoff, spring fallback\n"
        "4. LTE unavailable rural → Multi-band fallback, all safety offline, GPS cache\n"
        "5. User adoption resistance → <400g weight, Braille buttons, ears-free"
    )
    add_text_box(slide4, Inches(5.2), Inches(1.5), Inches(4.5), Inches(4.5), op_text, 10)
    
    # SLIDE 5 (NEW ENHANCEMENTS)
    slide5 = prs.slides[4]
    slide5.shapes[1].text = "IMPACT & BENEFITS"
    remove_shape(slide5, slide5.shapes[2])
    
    # Left Box
    impact_blocks = [
        {'text': "THREE NATIONAL IMPACT PILLARS\n\n", 'size': 14, 'bold': True},
        {'text': "🏥 SOCIAL & ACCESSIBILITY\n", 'size': 11, 'bold': True, 'color': RGBColor(0, 112, 192)},
        {'text': "• 12M+ visually impaired beneficiaries (WHO 2023)\n• Only ~2% have access to any smart mobility aid\n• 60% projected fall injury reduction via sub-15ms haptics\n• Autonomous SOS saves lives — no smartphone needed\n• Ears-free design preserves full independence\n• Voice AI enables independent navigation & sign reading\n\n", 'size': 10, 'bold': False},
        {'text': "💰 ECONOMIC IMPACT\n", 'size': 11, 'bold': True, 'color': RGBColor(0, 176, 80)},
        {'text': "• ₹9,600 Cr addressable market in India\n• 70-90% cost reduction vs commercial alternatives\n• Make in India: 100% COTS, domestic SMT assembly\n• 5,000+ manufacturing & support jobs\n• ₹2-5K Cr healthcare savings over 5 years\n\n", 'size': 10, 'bold': False},
        {'text': "🇮🇳 GOVERNMENT MISSION ALIGNMENT\n", 'size': 11, 'bold': True, 'color': RGBColor(255, 192, 0)},
        {'text': "• Accessible India Campaign (Sugamya Bharat Abhiyan)\n• RPwD Act 2016 — Sec 42 (accessibility), Sec 25 (assistive tech)\n• ADIP Scheme — BPL subsidy eligible (MoSJE)\n• Digital India — IoT caregiver cloud dashboard\n• Ayushman Bharat — PPG vitals health records integration", 'size': 10, 'bold': False}
    ]
    add_styled_text_box(slide5, Inches(0.5), Inches(1.5), Inches(4.5), Inches(5.0), impact_blocks)
    
    # Right Box
    comp_blocks = [
        {'text': "COMPETITIVE COMPARISON\n\n", 'size': 14, 'bold': True},
        {'text': "Feature              | WeWALK | Sunu | Ours\nDual-Processor       |   ✗    |  ✗   |  ✓\nSub-15ms Haptic      |   ✗    |  ~   |  ✓\nDual AI Cameras      |   ✗    |  ✗   |  ✓\nBone-Conduction      |   ✗    |  ✗   |  ✓\nAutonomous SOS       |   ✗    |  ✗   |  ✓\n8-Sensor 360°        |   1    |  1   |  8\nMotorized Tip        |   ✗    |  ✗   |  ✓\nFall + Auto SOS      |   ✗    |  ✗   |  ✓\nPPG Health           |   ✗    |  ✗   |  ✓\nVoice AI (Gemini)    |   ~    |  ✗   |  ✓\n36h+ Battery         |  4-5h  | 6-8h | 36h+\nPrice (India)        | ₹50K+  | ₹30K+| ₹8-12K\n\n", 'size': 10, 'bold': False},
        {'text': "12M+ Beneficiaries | 90% Cost Reduction | <5s SOS | 36h+ Battery | 50ms Reflex | 8 Sensors", 'size': 10, 'bold': True}
    ]
    add_styled_text_box(slide5, Inches(5.2), Inches(1.5), Inches(4.5), Inches(5.0), comp_blocks)
    
    # SLIDE 6 (NEW ENHANCEMENTS)
    slide6 = prs.slides[5]
    slide6.shapes[1].text = "RESEARCH & REFERENCES"
    remove_shape(slide6, slide6.shapes[2])
    
    ref_blocks = [
        {'text': "STANDARDS & RESEARCH CITATIONS\n\n", 'size': 14, 'bold': True},
        {'text': "Standards & Regulatory:\n", 'size': 11, 'bold': True},
        {'text': "• WHO Global Report on Assistive Technology (2022)\n• RPwD Act 2016 (India) — Sec 42 & 25\n• Accessible India Campaign (Sugamya Bharat Abhiyan)\n• IEC 62366-1:2015 — Medical device usability\n• ISO 11334-1 — Walking aids standard\n\n", 'size': 10, 'bold': False},
        {'text': "Key Research Papers:\n", 'size': 11, 'bold': True},
        {'text': "• Bai et al. (2019) IEEE Trans. Consumer Electronics — Dual-camera + ultrasonic validation\n• Elmannai & Elleithy (2017) MDPI Sensors — Assistive sensing modalities\n• Saaid et al. (2016) IEEE ICEEI — Baseline smart cane architecture\n• Lin et al. (2020) YOLO-Fastest — Sub-100ms edge inference\n• Radford et al. (2022) Whisper — Robust speech recognition\n• NSO (2021) MoSPI — 12M+ visually impaired stats", 'size': 10, 'bold': False}
    ]
    add_styled_text_box(slide6, Inches(0.5), Inches(1.5), Inches(4.5), Inches(5.0), ref_blocks)
    
    img_width = Inches(2.2)
    img_height = Inches(1.8)
    # Top-left
    cad_render = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SmartCane\renders\shot1_1.png"
    if os.path.exists(cad_render):
        slide6.shapes.add_picture(cad_render, Inches(5.2), Inches(1.5), width=img_width, height=img_height)
        add_text_box(slide6, Inches(5.2), Inches(3.3), img_width, Inches(0.5), "3D CAD Model (Blender 5.2, 63K+ faces)", 8)
        
    # Top-right
    arch_webapp = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SIH_PPT_Slide_System_Architecture.png"
    if os.path.exists(arch_webapp):
        slide6.shapes.add_picture(arch_webapp, Inches(7.5), Inches(1.5), width=img_width, height=img_height)
        add_text_box(slide6, Inches(7.5), Inches(3.3), img_width, Inches(0.5), "Interactive Architecture Web App", 8)
        
    # Bottom-left
    tip_render = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SmartCane\renders\render_tip_1.png"
    if os.path.exists(tip_render):
        slide6.shapes.add_picture(tip_render, Inches(5.2), Inches(4.0), width=img_width, height=img_height)
        add_text_box(slide6, Inches(5.2), Inches(5.8), img_width, Inches(0.5), "Quad-Pod Adaptive Tip Detail", 8)
        
    # Bottom-right
    handle_render = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\SmartCane\renders\render_handle_1.png"
    if os.path.exists(handle_render):
        slide6.shapes.add_picture(handle_render, Inches(7.5), Inches(4.0), width=img_width, height=img_height)
        add_text_box(slide6, Inches(7.5), Inches(5.8), img_width, Inches(0.5), "Handle Assembly Detail", 8)
        
    add_text_box(slide6, Inches(5.2), Inches(6.5), Inches(4.5), Inches(0.5), "23-page Engineering Specification (Rev A) + Engineering Diagrams Package + Full 3D CAD Model + Interactive Architecture Web App", 8, bold=True)
    
    # Delete slide 7
    rId = prs.slides._sldIdLst[-1].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[-1]
    
    prs.save(output_path)
    print("Successfully generated with enhancements:", output_path)

except Exception as e:
    print("Error:")
    traceback.print_exc()
