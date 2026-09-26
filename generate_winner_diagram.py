import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, BoxStyle, Circle, ArrowStyle
import numpy as np

# Set high DPI for crisp presentation graphic
fig, ax = plt.subplots(figsize=(10, 14), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Coordinates range: X: 0 to 100, Y: 0 to 140
ax.set_xlim(0, 100)
ax.set_ylim(0, 140)
ax.axis('off')

# Helper: Draw smooth rounded pill / badge
def draw_pill(ax, x, y, w, h, text, bg_color, text_color='#FFFFFF', font_size=11, font_weight='bold', border_color=None, border_width=1.5):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.2,rounding_size=2.0",
                       facecolor=bg_color, edgecolor=border_color if border_color else bg_color,
                       linewidth=border_width, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, text, ha='center', va='center', color=text_color,
            fontsize=font_size, fontweight=font_weight, zorder=4, family='sans-serif')

def draw_card(ax, x, y, w, h, bg_color='#F8FAFC', border_color='#E2E8F0', border_width=1.5):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.3,rounding_size=1.2",
                       facecolor=bg_color, edgecolor=border_color,
                       linewidth=border_width, zorder=2)
    ax.add_patch(p)

def draw_circle_icon(ax, x, y, r, bg_color, text, text_color='#FFFFFF', font_size=14):
    c = Circle((x, y), r, facecolor=bg_color, edgecolor='#FFFFFF', linewidth=2, zorder=3)
    ax.add_patch(c)
    ax.text(x, y, text, ha='center', va='center', color=text_color,
            fontsize=font_size, fontweight='bold', zorder=4, family='sans-serif')

# Helper: Draw professional arrows
def draw_arrow(ax, x1, y1, x2, y2, color='#1E293B', lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=14, shrinkA=2, shrinkB=2),
                zorder=5)

# ==================== 1. TOP HEADER: USER -> POWER ON -> SYSTEM HEALTH ====================
# User icon / representation
c_user = Circle((14, 131), 3.5, facecolor='#E0E7FF', edgecolor='#4F46E5', linewidth=2, zorder=3)
ax.add_patch(c_user)
ax.text(14, 131.2, "👤", ha='center', va='center', fontsize=18, zorder=4)
ax.text(14, 125, "USER\n(Grip Hold)", ha='center', va='top', fontsize=9, fontweight='bold', color='#1E293B', family='sans-serif')

# Arrow: User -> Power On
draw_arrow(ax, 19, 131, 30, 131, color='#1E293B')

# Power On / Bio-Grip Pill
draw_pill(ax, 48, 131, 32, 6, "POWER ON & BIO-GRIP", bg_color='#38BDF8', text_color='#FFFFFF', font_size=10)
# Sub-bullet below
ax.text(48, 126, "PPG Vitals Validated (MAX30102)", ha='center', va='top', fontsize=7.5, color='#64748B', family='sans-serif')

# Arrow: Power On -> Health Check
draw_arrow(ax, 65, 131, 74, 131, color='#1E293B')

# Shield / Authentication icon
c_shield = Circle((82, 131), 3.8, facecolor='#ECFDF5', edgecolor='#10B981', linewidth=2, zorder=3)
ax.add_patch(c_shield)
ax.text(82, 131.2, "🛡️", ha='center', va='center', fontsize=16, zorder=4)
# Green checkmark badge
c_chk = Circle((85, 128.5), 1.5, facecolor='#10B981', edgecolor='#FFFFFF', linewidth=1.5, zorder=5)
ax.add_patch(c_chk)
ax.text(85, 128.5, "✓", ha='center', va='center', fontsize=8, color='#FFFFFF', fontweight='bold', zorder=6)
ax.text(82, 124.5, "Reflex Core Active\n(FreeRTOS 50ms Loop)", ha='center', va='top', fontsize=8, fontweight='bold', color='#0F766E', family='sans-serif')

# Loop arrow down from User/Bio-Grip to Central Decision
ax.plot([14, 14, 50], [123, 116, 116], color='#1E293B', lw=2, zorder=5)
draw_arrow(ax, 50, 116, 50, 114, color='#1E293B')

# ==================== 2. CENTRAL DECISION NODE ====================
draw_card(ax, 50, 110, 52, 7.5, bg_color='#F1F5F9', border_color='#CBD5E1', border_width=1.5)
ax.text(50, 111.5, "⚠️ Environmental Hazard & Terrain State?", ha='center', va='center',
        fontsize=10.5, fontweight='bold', color='#0F172A', family='sans-serif')
ax.text(50, 107.5, "Obstacle Ahead? • Abrupt Drop-off / Curb? • Severe Fall Spike?", ha='center', va='center',
        fontsize=7.5, color='#64748B', family='sans-serif')

# ==================== 3. THREE DISTINCT COLOR BRANCHES ====================
# Branch split arrows
# Left: Blue (X: 18)
ax.plot([50, 18], [106, 102], color='#0284C7', lw=2.5, zorder=5)
draw_arrow(ax, 18, 102, 18, 98, color='#0284C7', lw=2.5)

# Center: Orange (X: 50)
draw_arrow(ax, 50, 106, 50, 98, color='#EA580C', lw=2.5)

# Right: Green (X: 82)
ax.plot([50, 82], [106, 102], color='#16A34A', lw=2.5, zorder=5)
draw_arrow(ax, 82, 102, 82, 98, color='#16A34A', lw=2.5)

# ----------------- LANE 1: BLUE (NORMAL WALKING & EDGE AI) -----------------
draw_pill(ax, 18, 95, 28, 5.5, "NORMAL WALKING", bg_color='#0284C7', text_color='#FFFFFF', font_size=9.5)
ax.text(18, 90.5, "(Battery > 25% • 16-18h Runtime)", ha='center', va='top', fontsize=7, color='#0369A1', family='sans-serif')

# Step 1: Dual Cameras
draw_arrow(ax, 18, 88, 18, 83, color='#0284C7')
draw_card(ax, 18, 77, 26, 9.5, bg_color='#F0F9FF', border_color='#BAE6FD')
ax.text(18, 80, "📷", ha='center', va='center', fontsize=18)
ax.text(18, 76, "Dual AI Vision", ha='center', va='center', fontsize=9, fontweight='bold', color='#0369A1')
ax.text(18, 73.5, "Forward CAM1 (5MP)\n+ Lower CAM2 (120°)", ha='center', va='center', fontsize=6.8, color='#0284C7')

# Step 2: Edge Inference & Scene OCR
draw_arrow(ax, 18, 71.5, 18, 66.5, color='#0284C7')
draw_card(ax, 18, 60.5, 26, 9.5, bg_color='#F0F9FF', border_color='#BAE6FD')
ax.text(18, 63.5, "🧠", ha='center', va='center', fontsize=18)
ax.text(18, 59.5, "YOLO Edge AI", ha='center', va='center', fontsize=9, fontweight='bold', color='#0369A1')
ax.text(18, 57, "Sign OCR • Pedestrians\nCrosswalk Signal Light", ha='center', va='center', fontsize=6.8, color='#0284C7')

# Step 3: Bone-Conduction Ears-Free Audio
draw_arrow(ax, 18, 55, 18, 50, color='#0284C7')
draw_card(ax, 18, 44, 26, 9.5, bg_color='#F0F9FF', border_color='#BAE6FD')
ax.text(18, 47, "🎧", ha='center', va='center', fontsize=18)
ax.text(18, 43, "Ears-Free Guidance", ha='center', va='center', fontsize=9, fontweight='bold', color='#0369A1')
ax.text(18, 40.5, "Bluetooth Bone Link\nAmbient Hearing 100% Free", ha='center', va='center', fontsize=6.8, color='#0284C7')

# Step 4: Verified Safe Path Output
draw_arrow(ax, 18, 38.5, 18, 33.5, color='#0284C7')
draw_pill(ax, 18, 30.5, 24, 4.5, "✓ VERIFIED SAFE", bg_color='#0284C7', text_color='#FFFFFF', font_size=8)
ax.text(18, 25.5, "Continuous 30 fps\nSafe Trajectory Tracking", ha='center', va='top', fontsize=7, color='#0369A1', family='sans-serif')


# ----------------- LANE 2: ORANGE (ALWAYS-ON REFLEX SAFETY) -----------------
# Star badge for Innovation
ax.text(37, 98, "⭐", ha='center', va='center', fontsize=12, zorder=6)
draw_pill(ax, 50, 95, 28, 5.5, "REFLEX SAFETY", bg_color='#EA580C', text_color='#FFFFFF', font_size=9.5)
ax.text(50, 90.5, "(Sub-15ms • Always-On • Pi-Crash Proof)", ha='center', va='top', fontsize=7, color='#C2410C', family='sans-serif')

# Step 1: Acoustic + Laser Ranging
draw_arrow(ax, 50, 88, 50, 83, color='#EA580C')
draw_card(ax, 50, 77, 26, 9.5, bg_color='#FFF7ED', border_color='#FED7AA')
ax.text(50, 80, "📡", ha='center', va='center', fontsize=18)
ax.text(50, 76, "50ms FreeRTOS Loop", ha='center', va='center', fontsize=9, fontweight='bold', color='#C2410C')
ax.text(50, 73.5, "Acoustic US (SEN1)\n+ Laser ToF Depth (SEN2)", ha='center', va='center', fontsize=6.8, color='#EA580C')

# Step 2: Sub-15ms Palm Haptic Reflex
draw_arrow(ax, 50, 71.5, 50, 66.5, color='#EA580C')
draw_card(ax, 50, 60.5, 26, 9.5, bg_color='#FFF7ED', border_color='#FED7AA')
ax.text(50, 63.5, "✋", ha='center', va='center', fontsize=18)
ax.text(50, 59.5, "Tactile Palm Reflex", ha='center', va='center', fontsize=9, fontweight='bold', color='#C2410C')
ax.text(50, 57, "<15ms DRV2605L LRA\nDrop-off / Curb / Water Alert", ha='center', va='center', fontsize=6.8, color='#EA580C')

# Step 3: Motorized Quad-Pod Stabilization
draw_arrow(ax, 50, 55, 50, 50, color='#EA580C')
draw_card(ax, 50, 44, 26, 9.5, bg_color='#FFF7ED', border_color='#FED7AA')
ax.text(50, 47, "🦿", ha='center', va='center', fontsize=18)
ax.text(50, 43, "Adaptive Quad-Pod", ha='center', va='center', fontsize=9, fontweight='bold', color='#C2410C')
ax.text(50, 40.5, "1.2s Motorized Base Deploy\nStops Fall on Rough Incline", ha='center', va='center', fontsize=6.8, color='#EA580C')

# Step 4: Power-Save Mode Continuity
draw_arrow(ax, 50, 38.5, 50, 33.5, color='#EA580C')
draw_pill(ax, 50, 30.5, 26, 4.5, "🔋 36h+ FAIL-SAFE", bg_color='#EA580C', text_color='#FFFFFF', font_size=8)
ax.text(50, 25.5, "Zero Single-Point Failure\nRuns with Pi / Phone Dead", ha='center', va='top', fontsize=7, color='#C2410C', family='sans-serif')


# ----------------- LANE 3: GREEN (AUTONOMOUS SOS & CARE RESCUE) -----------------
# Star badge for Innovation
ax.text(69, 98, "⭐", ha='center', va='center', fontsize=12, zorder=6)
draw_pill(ax, 82, 95, 28, 5.5, "AUTONOMOUS SOS", bg_color='#16A34A', text_color='#FFFFFF', font_size=9.5)
ax.text(82, 90.5, "(Direct-AT LTE • No Smartphone Needed)", ha='center', va='top', fontsize=7, color='#15803D', family='sans-serif')

# Step 1: Fall Detection & 92dBA Alarm
draw_arrow(ax, 82, 88, 82, 83, color='#16A34A')
draw_card(ax, 82, 77, 26, 9.5, bg_color='#F0FDF4', border_color='#BBF7D0')
ax.text(82, 80, "🚨", ha='center', va='center', fontsize=18)
ax.text(82, 76, "Fall Spike / 2s SOS", ha='center', va='center', fontsize=9, fontweight='bold', color='#15803D')
ax.text(82, 73.5, "IMU Impact + 5s Inactivity\n92dBA Siren Activated", ha='center', va='center', fontsize=6.8, color='#16A34A')

# Step 2: Direct Govt 112 & Ambulance Routing
draw_arrow(ax, 82, 71.5, 82, 66.5, color='#16A34A')
draw_card(ax, 82, 60.5, 26, 9.5, bg_color='#F0FDF4', border_color='#BBF7D0')
ax.text(82, 63.5, "🏛️", ha='center', va='center', fontsize=18)
ax.text(82, 59.5, "Govt Emergency 112", ha='center', va='center', fontsize=9, fontweight='bold', color='#15803D')
ax.text(82, 57, "Autonomous Direct-AT Dial\nGPS Coordinates Dispatched", ha='center', va='center', fontsize=6.8, color='#16A34A')

# Step 3: Caregiver Cloud Sync & Live Geofence
draw_arrow(ax, 82, 55, 82, 50, color='#16A34A')
draw_card(ax, 82, 44, 26, 9.5, bg_color='#F0FDF4', border_color='#BBF7D0')
ax.text(82, 47, "📲", ha='center', va='center', fontsize=18)
ax.text(82, 43, "Caregiver Cloud IoT", ha='center', va='center', fontsize=9, fontweight='bold', color='#15803D')
ax.text(82, 40.5, "MQTT over TLS 1.3\nLive Pin + Heart Rate Vitals", ha='center', va='center', fontsize=6.8, color='#16A34A')

# Step 4: Rapid Rescue Response Output
draw_arrow(ax, 82, 38.5, 82, 33.5, color='#16A34A')
draw_pill(ax, 82, 30.5, 24, 4.5, "🏅 RESCUE DISPATCHED", bg_color='#16A34A', text_color='#FFFFFF', font_size=8)
ax.text(82, 25.5, "< 5 Second Full Dispatch\n100% Standalone Rescue", ha='center', va='top', fontsize=7, color='#15803D', family='sans-serif')


# ==================== BOTTOM TRUST & CERTIFICATION FOOTER ====================
draw_card(ax, 50, 11, 94, 13, bg_color='#F8FAFC', border_color='#E2E8F0', border_width=1.5)
ax.text(50, 15, "GLOBAL STANDARDS & NATIONAL COMPLIANCE", ha='center', va='center',
        fontsize=9, fontweight='bold', color='#0F172A', family='sans-serif')

trust_badges = [
    ("NIST & FreeRTOS", "#EF4444"),
    ("RPwD Act 2016", "#2563EB"),
    ("Accessible India", "#059669"),
    ("ADIP Scheme", "#D97706"),
    ("IEC 62366 Usability", "#7C3AED")
]

bx_start = 12
bx_spacing = 19
for i, (b_text, b_col) in enumerate(trust_badges):
    draw_pill(ax, bx_start + i * bx_spacing, 7.5, 17, 4.2, b_text, bg_color=b_col, text_color='#FFFFFF', font_size=7)

plt.tight_layout()
output_path = r"c:\Users\mohit\RVCE\hackathons\SIH 2026\PPT_Assets\winner_style_decision_flowchart.png"
plt.savefig(output_path, dpi=300, facecolor='#FFFFFF', bbox_inches='tight')
print("Successfully generated winner-style flowchart at:", output_path)
