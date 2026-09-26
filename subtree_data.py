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
