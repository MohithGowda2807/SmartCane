import React, { useState } from 'react';
import { Eye, Layers, Sparkles, CheckCircle, Info, ExternalLink } from 'lucide-react';

export default function Hardware3DView({ onSelectComponent }) {
  const [activeShot, setActiveShot] = useState('full');

  const shots = [
    {
      id: 'full',
      title: 'Full Assembled 3D Cane',
      subtitle: 'Complete 1.26m smart assistive cane with dual vision, sensor array, and quad-pod tip',
      image: '/renders/shot1_1.png',
      badge: 'Overall Assembly',
      callouts: [
        { title: 'Top Microphone', desc: 'Apex acoustic voice intake directed at user mouth', pos: 'Top' },
        { title: 'Top Camera', desc: 'Forward-looking scene, sign OCR & pedestrian detection', pos: 'Handle' },
        { title: 'Upper PIR Sensor', desc: 'Torso-height 120° pedestrian & cyclist motion detection', pos: 'Upper Shaft' },
        { title: 'Bluetooth Assistant', desc: 'Bone-conduction wireless audio link for ear guidance', pos: 'Mid Shaft' },
        { title: 'Lower PIR Sensor', desc: 'Low-angle blind spot detection for children, pets & carts', pos: 'Lower Shaft' },
        { title: 'Bottom Camera', desc: 'Downward-angled camera for stairs, curbs, and potholes', pos: 'Lower Shaft' },
        { title: 'Ultrasonic & ToF', desc: 'Zero-latency 50ms reflex safety ranging at tip', pos: 'Tip Base' }
      ]
    },
    {
      id: 'handle',
      title: 'Handle & Top Voice Interface',
      subtitle: 'Ergonomic D-shaped thumb arch, Braille controls, top apex microphone, and forward camera',
      image: '/renders/render_handle_1.png',
      badge: 'Handle Subsystem',
      callouts: [
        { title: 'Top Microphone Grille', desc: 'Gold/steel acoustic port angled towards mouth for noise-free voice AI', pos: 'Apex' },
        { title: 'Forward Camera (CAM1)', desc: 'OmniVision 5MP module in protected pod angled 20° downward', pos: 'Arch Base' },
        { title: 'Braille Tactile Buttons', desc: 'Raised V (Voice), E (Env), I (Incident), P (Power) thumb buttons', pos: 'Arch' },
        { title: 'Guarded SOS Button', desc: 'Recessed apex switch prevents accidental press; 2s hold activates emergency', pos: 'Cap' },
        { title: 'MAX30102 PPG Sensor', desc: 'Optical heart rate and SpO2 monitoring embedded in grip', pos: 'Grip' }
      ]
    },
    {
      id: 'shaft',
      title: 'Shaft Electronics & Dual PIRs',
      subtitle: 'Split-shell aluminum channel housing dual processors, cellular modem, and spatial PIRs',
      image: '/renders/render_shaft_1.png',
      badge: 'Shaft Subsystem',
      callouts: [
        { title: 'Upper PIR Sensor (SEN3)', desc: 'Translucent faceted Fresnel dome detecting approaching pedestrians', pos: 'Upper Collar' },
        { title: 'Dual Processors Rail', desc: 'ESP32-S3 always-on safety RTOS + RPi Zero 2 W switchable edge AI', pos: 'Internal' },
        { title: 'Bluetooth 5.x Module', desc: 'Streams navigational voice cues to bone-conduction ear assistant', pos: 'Internal' },
        { title: 'SIM7600G-H LTE Modem', desc: '4G cellular + multi-constellation GPS/GLONASS with patch antenna', pos: 'Internal' },
        { title: 'Lower PIR Sensor (SEN4)', desc: 'Detects dynamic low obstacles in peripheral blind spots', pos: 'Lower Tube' }
      ]
    },
    {
      id: 'tip',
      title: 'Adaptive Tip, Bottom Cam & Ultrasonic',
      subtitle: 'Ground-facing vision, dual-transducer acoustic ranging, and motorized quad-pod legs',
      image: '/renders/render_tip_1.png',
      badge: 'Tip Subsystem',
      callouts: [
        { title: 'Bottom Pavement Camera', desc: 'Angled 35° downward for real-time curb, pothole, and drop-off segmentation', pos: 'Collar' },
        { title: 'Dual Ultrasonic Transducers', desc: 'Rugged waterproof 40 kHz acoustic ranging (20-450 cm)', pos: 'Front Face' },
        { title: 'VL53L1X Laser ToF', desc: 'Sub-millimeter curb & step-down profile detection', pos: 'Lower Face' },
        { title: 'Motorized Quad-Pod Legs', desc: 'DRV8830 motor deploys 3 articulated legs on gravel or incline', pos: 'Hub' },
        { title: 'Moisture Contact Pins', desc: 'Gold electrode pins detect standing water puddles before stepping', pos: 'Rubber Foot' }
      ]
    }
  ];

  const current = shots.find(s => s.id === activeShot) || shots[0];

  return (
    <div className="w-full space-y-6">
      {/* View Switcher Tabs */}
      <div className="flex items-center gap-3 overflow-x-auto pb-2">
        {shots.map((shot) => {
          const isSelected = shot.id === activeShot;
          return (
            <button
              key={shot.id}
              onClick={() => setActiveShot(shot.id)}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl border text-xs font-semibold whitespace-nowrap transition-all ${
                isSelected
                  ? 'bg-blue-600 text-white border-blue-500 shadow-lg shadow-blue-500/20'
                  : 'bg-slate-900 text-slate-300 border-slate-800 hover:bg-slate-800'
              }`}
            >
              <Layers size={14} />
              {shot.title}
            </button>
          );
        })}
      </div>

      {/* Main 3D Model Display Card */}
      <div className="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-2xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-2 mb-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                {current.badge}
              </span>
              <span className="text-xs font-mono text-slate-500">Blender 5.2 EEVEE 3D Render</span>
            </div>
            <h3 className="text-xl font-bold text-white tracking-wide">{current.title}</h3>
            <p className="text-xs text-slate-400 mt-0.5">{current.subtitle}</p>
          </div>
          <span className="px-3 py-1 text-xs font-medium rounded-lg bg-slate-800 text-slate-300 self-start md:self-auto flex items-center gap-1.5">
            <Sparkles size={13} className="text-amber-400" /> New Hardware Integrated
          </span>
        </div>

        {/* Image & Callouts Split View */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          {/* Render Preview Image */}
          <div className="lg:col-span-7 flex items-center justify-center p-4 rounded-xl bg-slate-950 border border-slate-800/80 min-h-[380px] relative overflow-hidden group">
            <img 
              src={current.image} 
              alt={current.title}
              className="max-h-[420px] w-auto object-contain rounded-lg shadow-md group-hover:scale-105 transition-transform duration-500"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'flex';
              }}
            />
            <div className="hidden absolute inset-0 items-center justify-center text-xs text-slate-400 p-6 text-center">
              <span>3D Render available at: {current.image}</span>
            </div>
          </div>

          {/* Feature Callouts List */}
          <div className="lg:col-span-5 space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
              Key Features Visible in this Angle:
            </h4>
            <div className="space-y-2.5 max-h-[420px] overflow-y-auto pr-1">
              {current.callouts.map((c, i) => (
                <div 
                  key={i}
                  className="p-3 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-blue-500/50 transition text-xs"
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-white flex items-center gap-1.5">
                      <CheckCircle size={13} className="text-emerald-400" /> {c.title}
                    </span>
                    <span className="text-[10px] font-mono text-cyan-400 px-1.5 py-0.5 rounded bg-slate-800">
                      {c.pos}
                    </span>
                  </div>
                  <p className="text-slate-400 leading-relaxed text-[11px]">
                    {c.desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
