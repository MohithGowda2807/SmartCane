import React, { useRef, useState } from 'react';
import { 
  Download, Copy, Maximize2, Minimize2, Check, ShieldAlert, 
  Sparkles, Video, Mic, Radio, Cpu, BatteryCharging, Cloud, Layers, CheckCircle2 
} from 'lucide-react';
import { toPng, toBlob } from 'html-to-image';

export default function SlidePresentationMode({ onSelectComponent }) {
  const slideRef = useRef(null);
  const [isExporting, setIsExporting] = useState(false);
  const [copySuccess, setCopySuccess] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  const handleExportPng = async () => {
    if (!slideRef.current) return;
    try {
      setIsExporting(true);
      const dataUrl = await toPng(slideRef.current, { 
        quality: 0.98,
        pixelRatio: 2, // 2x high resolution for crisp presentation projection
        backgroundColor: '#070b14'
      });
      const link = document.createElement('a');
      link.download = 'SmartCane_System_Architecture_SIH2026.png';
      link.href = dataUrl;
      link.click();
    } catch (err) {
      console.error('Failed to export slide image', err);
      alert('Could not generate slide PNG image. Please use browser print or screenshot.');
    } finally {
      setIsExporting(false);
    }
  };

  const handleCopyToClipboard = async () => {
    if (!slideRef.current) return;
    try {
      setCopySuccess(true);
      const blob = await toBlob(slideRef.current, { 
        quality: 0.98,
        pixelRatio: 2,
        backgroundColor: '#070b14' 
      });
      if (blob && navigator.clipboard && window.ClipboardItem) {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/png': blob })
        ]);
        setTimeout(() => setCopySuccess(false), 2500);
      } else {
        handleExportPng();
      }
    } catch (err) {
      console.error('Copy failed, downloading instead', err);
      handleExportPng();
    }
  };

  return (
    <div className="w-full flex flex-col items-center">
      {/* Action Toolbar */}
      <div className="w-full max-w-7xl flex items-center justify-between gap-3 mb-4 p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs">
        <div className="flex items-center gap-2">
          <span className="px-2.5 py-1 font-bold uppercase tracking-wider rounded-md bg-blue-600 text-white">
            1-Slide PPT Mode (16:9)
          </span>
          <span className="text-slate-400 hidden sm:inline">
            Optimized high-density layout designed to fit directly on 1 PowerPoint slide for SIH submission.
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleExportPng}
            disabled={isExporting}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold shadow-md transition disabled:opacity-50"
          >
            <Download size={14} />
            {isExporting ? 'Generating PNG...' : 'Download Slide Image (PNG)'}
          </button>

          <button
            onClick={handleCopyToClipboard}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold transition"
          >
            {copySuccess ? <Check size={14} className="text-emerald-400" /> : <Copy size={14} />}
            {copySuccess ? 'Copied to Clipboard!' : 'Copy Slide'}
          </button>

          <button
            onClick={() => setIsFullscreen(!isFullscreen)}
            className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
            title={isFullscreen ? 'Exit Fullscreen' : 'Fullscreen'}
          >
            {isFullscreen ? <Minimize2 size={16} /> : <Maximize2 size={16} />}
          </button>
        </div>
      </div>

      {/* The 16:9 Slide Canvas */}
      <div 
        className={`w-full transition-all duration-300 ${
          isFullscreen 
            ? 'fixed inset-0 z-50 bg-[#070b14] p-4 flex items-center justify-center overflow-auto' 
            : 'max-w-7xl'
        }`}
      >
        <div 
          ref={slideRef}
          className="w-full bg-[#070b14] border-2 border-slate-800 rounded-2xl p-6 shadow-2xl relative overflow-hidden text-slate-100 flex flex-col justify-between"
          style={{ minHeight: '740px', aspectRatio: '16 / 9' }}
        >
          {/* Subtle Ambient Background Gradients */}
          <div className="absolute top-0 right-0 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl pointer-events-none" />
          <div className="absolute bottom-0 left-0 w-96 h-96 bg-purple-600/10 rounded-full blur-3xl pointer-events-none" />

          {/* SLIDE HEADER */}
          <div className="relative z-10 pb-4 border-b border-slate-800 flex items-start justify-between">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="text-[11px] font-bold tracking-widest uppercase px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 border border-blue-500/30">
                  Smart India Hackathon (SIH 2026) • Assistive Hardware & Robotics
                </span>
                <span className="text-[11px] font-mono text-cyan-400 font-semibold">
                  System Architecture Rev B
                </span>
              </div>
              <h1 className="text-2xl md:text-3xl font-black text-white tracking-tight flex items-center gap-3">
                SMART INTELLIGENT CANE — END-TO-END SYSTEM ARCHITECTURE
              </h1>
              <p className="text-xs text-slate-400 mt-0.5">
                Dual-Processor Edge AI & Autonomous Reflex Safety Architecture with Spatial Sensing & Bone-Conduction Ear Assistant
              </p>
            </div>

            {/* Quick Metrics Badges in Header */}
            <div className="hidden lg:grid grid-cols-3 gap-2 text-right">
              <div className="px-2.5 py-1 rounded bg-slate-900 border border-slate-800 text-[11px]">
                <span className="text-slate-500 block text-[9px] uppercase font-bold">Safety Loop</span>
                <span className="font-mono font-bold text-red-400">50 ms (20 Hz)</span>
              </div>
              <div className="px-2.5 py-1 rounded bg-slate-900 border border-slate-800 text-[11px]">
                <span className="text-slate-500 block text-[9px] uppercase font-bold">Power-Save</span>
                <span className="font-mono font-bold text-cyan-400">36+ Hours</span>
              </div>
              <div className="px-2.5 py-1 rounded bg-slate-900 border border-slate-800 text-[11px]">
                <span className="text-slate-500 block text-[9px] uppercase font-bold">Ear Assistant</span>
                <span className="font-mono font-bold text-emerald-400">BLE Audio</span>
              </div>
            </div>
          </div>

          {/* SLIDE CORE ARCHITECTURE: 4 DISTINCT COLUMNS */}
          <div className="relative z-10 grid grid-cols-1 md:grid-cols-4 gap-4 my-4 flex-1">
            
            {/* COLUMN 1: PERCEPTION & SENSOR SUITE */}
            <div className="flex flex-col rounded-xl bg-slate-900/90 border border-blue-900/40 p-3.5 shadow-lg relative">
              <div className="flex items-center justify-between pb-2 mb-2.5 border-b border-slate-800">
                <span className="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
                  <Video size={14} /> 1. Multi-Modal Perception
                </span>
                <span className="text-[9px] font-mono bg-blue-500/10 text-blue-300 px-1.5 py-0.5 rounded">
                  8 Sensors
                </span>
              </div>

              <div className="space-y-2 text-xs flex-1 flex flex-col justify-between">
                {/* Top Camera */}
                <div className="p-2 rounded bg-slate-950/80 border border-slate-800">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white flex items-center gap-1">
                      <Sparkles size={10} className="text-amber-400" /> Top Forward Camera
                    </span>
                    <span className="text-[10px] font-mono text-purple-400">CSI-2</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">OV5647 5MP: Scene understanding, text OCR, pedestrian & sign detection</p>
                </div>

                {/* Bottom Camera */}
                <div className="p-2 rounded bg-slate-950/80 border border-amber-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-amber-300 flex items-center gap-1">
                      <Sparkles size={10} className="text-amber-400" /> Bottom Pavement Cam
                    </span>
                    <span className="text-[10px] font-mono text-purple-400">USB / UVC</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Wide 120° angled 35° down: Potholes, curbs, stairs, puddles & tactile paving</p>
                </div>

                {/* Ultrasonic & ToF */}
                <div className="p-2 rounded bg-slate-950/80 border border-red-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-red-300 flex items-center gap-1">
                      <ShieldAlert size={10} className="text-red-400" /> Ultrasonic + Laser ToF
                    </span>
                    <span className="text-[10px] font-mono text-cyan-400">GPIO + I2C</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">JSN-SR04T 40kHz (20-450cm) + VL53L1X laser step-down/drop-off detector</p>
                </div>

                {/* Dual PIR Sensors */}
                <div className="p-2 rounded bg-slate-950/80 border border-amber-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-amber-300 flex items-center gap-1">
                      <Sparkles size={10} className="text-amber-400" /> Dual Spatial PIRs (2x)
                    </span>
                    <span className="text-[10px] font-mono text-emerald-400">INT Lines</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Upper: Approaching pedestrians/cyclists. Lower: Low-angle blind spot moving hazards</p>
                </div>

                {/* IMU & Health */}
                <div className="p-2 rounded bg-slate-950/80 border border-slate-800">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-slate-200">BMI270 IMU + PPG Oximeter</span>
                    <span className="text-[10px] font-mono text-cyan-400">Diff I2C</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Fall impact spike, terrain vibration FFT + MAX30102 palm vitals & water pins</p>
                </div>
              </div>
            </div>

            {/* COLUMN 2: DUAL-PROCESSOR COMPUTE & SAFETY */}
            <div className="flex flex-col rounded-xl bg-slate-900/90 border border-purple-900/40 p-3.5 shadow-lg relative">
              <div className="flex items-center justify-between pb-2 mb-2.5 border-b border-slate-800">
                <span className="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                  <Cpu size={14} /> 2. Dual-Core Brain
                </span>
                <span className="text-[9px] font-mono bg-purple-500/10 text-purple-300 px-1.5 py-0.5 rounded">
                  RTOS + Linux
                </span>
              </div>

              <div className="space-y-3 text-xs flex-1 flex flex-col justify-between">
                {/* ESP32-S3 Box */}
                <div className="p-3 rounded-lg bg-red-950/20 border border-red-500/40">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-red-300 flex items-center gap-1.5">
                      <ShieldAlert size={12} className="text-red-400" /> ESP32-S3 Safety Core
                    </span>
                    <span className="text-[9px] font-bold px-1.5 py-0.2 rounded bg-red-500/20 text-red-300">
                      ALWAYS ON
                    </span>
                  </div>
                  <p className="text-[10px] font-mono text-slate-300">Dual Xtensa @ 240MHz • 50ms Deterministic Loop</p>
                  <ul className="text-[10px] text-slate-400 mt-1.5 space-y-1 list-disc pl-3">
                    <li>Zero-lag hazard arbitration: Fall &gt; Curb &gt; Obstacle &gt; Water</li>
                    <li>Sub-15ms trigger to palm vibrotactile haptic engine</li>
                    <li>Direct AT UART to SIM7600G for autonomous SOS</li>
                    <li>Manages TCA9555 power rail load-shedding switches</li>
                  </ul>
                </div>

                {/* Inter-link arrow */}
                <div className="flex items-center justify-center gap-2 py-0.5 text-[10px] font-mono text-cyan-400">
                  <span>Framed UART + RTS/CTS (921,600 baud)</span>
                </div>

                {/* RPi Zero 2 W Box */}
                <div className="p-3 rounded-lg bg-purple-950/20 border border-purple-500/40">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-purple-300 flex items-center gap-1.5">
                      <Cpu size={12} className="text-purple-400" /> Raspberry Pi Zero 2 W
                    </span>
                    <span className="text-[9px] font-bold px-1.5 py-0.2 rounded bg-purple-500/20 text-purple-300">
                      SWITCHABLE
                    </span>
                  </div>
                  <p className="text-[10px] font-mono text-slate-300">Quad Cortex-A53 @ 1.0 GHz • Linux 64-bit</p>
                  <ul className="text-[10px] text-slate-400 mt-1.5 space-y-1 list-disc pl-3">
                    <li>Dual-Camera Vision AI: YOLO-Fastest & MobileNet</li>
                    <li>Whisper.tflite speech recognition & multimodal NLP</li>
                    <li>Hosts Bluetooth 5.x audio stream to ear assistant</li>
                    <li>Cleanly shuts down in Power-Save mode (&lt;20% batt)</li>
                  </ul>
                </div>
              </div>
            </div>

            {/* COLUMN 3: AUDIO ASSISTANT & TACTILE HMI */}
            <div className="flex flex-col rounded-xl bg-slate-900/90 border border-emerald-900/40 p-3.5 shadow-lg relative">
              <div className="flex items-center justify-between pb-2 mb-2.5 border-b border-slate-800">
                <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                  <Mic size={14} /> 3. Assistive Output & HMI
                </span>
                <span className="text-[9px] font-mono bg-emerald-500/10 text-emerald-300 px-1.5 py-0.5 rounded">
                  Ears-Free & Haptics
                </span>
              </div>

              <div className="space-y-2 text-xs flex-1 flex flex-col justify-between">
                {/* Bluetooth Ear Assistant */}
                <div className="p-2 rounded bg-slate-950/80 border border-emerald-500/40">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-emerald-300 flex items-center gap-1">
                      <Sparkles size={10} className="text-amber-400" /> Bluetooth Ear Assistant
                    </span>
                    <span className="text-[10px] font-mono text-blue-400">BLE / A2DP</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Dedicated audio link to bone-conduction headset: Spoken turn-by-turn guidance, obstacle distance pings, and AI answers without blocking ambient hearing.</p>
                </div>

                {/* Top Microphone */}
                <div className="p-2 rounded bg-slate-950/80 border border-amber-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-amber-300 flex items-center gap-1">
                      <Sparkles size={10} className="text-amber-400" /> Top Apex Voice Mic
                    </span>
                    <span className="text-[10px] font-mono text-cyan-400">I2S Audio</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">High-SNR MEMS acoustic port at handle top; directed at user mouth for noise-free conversational AI queries.</p>
                </div>

                {/* Palm Haptic Engine */}
                <div className="p-2 rounded bg-slate-950/80 border border-red-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white flex items-center gap-1">
                      <ShieldAlert size={10} className="text-red-400" /> DRV2605L Haptic Palm Motor
                    </span>
                    <span className="text-[10px] font-mono text-red-400">&lt;15ms Latency</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Vibrotactile waveforms directly in palm: Proximity ticks, curb double-pulse, and severe emergency vibration.</p>
                </div>

                {/* Braille Tactile & SOS Button */}
                <div className="p-2 rounded bg-slate-950/80 border border-slate-800">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-slate-200">Tactile Braille + Guarded SOS</span>
                    <span className="text-[10px] font-mono text-slate-400">Active-Low</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">V (Voice), E (Env), I (Incident), P (Power) Braille switches + 2s recessed SOS button.</p>
                </div>

                {/* Adaptive Tip Legs */}
                <div className="p-2 rounded bg-slate-950/80 border border-amber-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-amber-300">Quad-Pod Adaptive Tip</span>
                    <span className="text-[10px] font-mono text-cyan-400">DRV8830</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Motor-deployed 3 articulated legs expand on rough gravel or inclines to prevent falls.</p>
                </div>
              </div>
            </div>

            {/* COLUMN 4: POWER & CLOUD INFRASTRUCTURE */}
            <div className="flex flex-col rounded-xl bg-slate-900/90 border border-cyan-900/40 p-3.5 shadow-lg relative">
              <div className="flex items-center justify-between pb-2 mb-2.5 border-b border-slate-800">
                <span className="text-xs font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-1.5">
                  <BatteryCharging size={14} /> 4. Power & Cloud Subsystem
                </span>
                <span className="text-[9px] font-mono bg-cyan-500/10 text-cyan-300 px-1.5 py-0.5 rounded">
                  5 Rails & LTE
                </span>
              </div>

              <div className="space-y-2 text-xs flex-1 flex flex-col justify-between">
                {/* 1S2P Battery Pack */}
                <div className="p-2 rounded bg-slate-950/80 border border-cyan-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-cyan-300">1S2P 6800 mAh Li-Ion</span>
                    <span className="text-[10px] font-mono text-cyan-400">USB-C PD</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Dual 18650 cells in parallel; single-cell charging eliminates balancing failure modes.</p>
                </div>

                {/* 5 Switched Rails */}
                <div className="p-2 rounded bg-slate-950/80 border border-slate-800">
                  <span className="font-bold text-white block mb-1">5 Isolated Power Rails</span>
                  <div className="space-y-0.5 text-[9px] font-mono">
                    <div className="flex justify-between text-emerald-400"><span>3V3_MAIN:</span><span>Buck-Boost (Always On)</span></div>
                    <div className="flex justify-between text-purple-400"><span>5V_PI:</span><span>Boost (Switched for Pi/Cams)</span></div>
                    <div className="flex justify-between text-cyan-400"><span>5V_AUX:</span><span>Boost (Ultrasonic & Amp)</span></div>
                    <div className="flex justify-between text-amber-400"><span>VBAT_MODEM:</span><span>Direct Cell (2A Bursts)</span></div>
                    <div className="flex justify-between text-slate-400"><span>VBAT_MOTOR:</span><span>Fused Adaptive Tip</span></div>
                  </div>
                </div>

                {/* SIM7600G Modem */}
                <div className="p-2 rounded bg-slate-950/80 border border-pink-500/40">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-pink-300">SIM7600G-H LTE & GNSS</span>
                    <span className="text-[10px] font-mono text-pink-400">Dual-Link</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Direct UART to ESP32 (Autonomous SOS SMS & Calls) + USB link to Pi for IoT telemetry.</p>
                </div>

                {/* Caregiver Cloud Portal */}
                <div className="p-2 rounded bg-slate-950/80 border border-blue-500/30">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-blue-300 flex items-center gap-1">
                      <Cloud size={10} className="text-blue-400" /> Caregiver IoT Cloud
                    </span>
                    <span className="text-[10px] font-mono text-blue-400">MQTT TLS</span>
                  </div>
                  <p className="text-[10px] text-slate-400 mt-0.5">Live GPS location, geo-fenced safe zones, fall incident alerts, and walking vitals dashboard.</p>
                </div>
              </div>
            </div>

          </div>

          {/* SLIDE FOOTER: KEY ARCHITECTURAL ADVANTAGES */}
          <div className="relative z-10 pt-3 border-t border-slate-800 grid grid-cols-1 md:grid-cols-4 gap-3 text-[11px]">
            <div className="flex items-center gap-2 text-slate-300">
              <CheckCircle2 size={14} className="text-red-400 shrink-0" />
              <span><strong>Deterministic Safety:</strong> 50ms FreeRTOS loop guarantees sub-15ms reflex haptic alert.</span>
            </div>
            <div className="flex items-center gap-2 text-slate-300">
              <CheckCircle2 size={14} className="text-amber-400 shrink-0" />
              <span><strong>Dual-Tier Sensing:</strong> Forward optical scene recognition + downward curb/stair detection.</span>
            </div>
            <div className="flex items-center gap-2 text-slate-300">
              <CheckCircle2 size={14} className="text-emerald-400 shrink-0" />
              <span><strong>Ears-Free Guidance:</strong> Bone-conduction Bluetooth ear assistant preserves environmental hearing.</span>
            </div>
            <div className="flex items-center gap-2 text-slate-300">
              <CheckCircle2 size={14} className="text-cyan-400 shrink-0" />
              <span><strong>Fail-Safe SOS:</strong> ESP32 autonomously executes 112 calls & SMS with GPS even if Pi is offline.</span>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
