import React, { useState } from 'react';
import { 
  ArrowRight, ShieldAlert, Video, Mic, BellRing, 
  BatteryCharging, Cpu, Radio, Sparkles, CheckCircle2, ChevronRight 
} from 'lucide-react';
import { FLOW_STREAMS, COMPONENTS } from '../data/architectureData';

export default function FlowView({ onSelectComponent }) {
  const [selectedStreamId, setSelectedStreamId] = useState(FLOW_STREAMS[0].id);

  const activeStream = FLOW_STREAMS.find(s => s.id === selectedStreamId) || FLOW_STREAMS[0];

  const getStreamIcon = (type) => {
    switch (type) {
      case 'safety': return <ShieldAlert size={18} className="text-red-400" />;
      case 'vision': return <Video size={18} className="text-purple-400" />;
      case 'voice': return <Mic size={18} className="text-emerald-400" />;
      case 'sos': return <BellRing size={18} className="text-pink-400" />;
      case 'power': return <BatteryCharging size={18} className="text-cyan-400" />;
      default: return <Cpu size={18} className="text-blue-400" />;
    }
  };

  return (
    <div className="w-full space-y-6">
      {/* Stream Selector Buttons */}
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3">
        {FLOW_STREAMS.map((stream) => {
          const isSelected = stream.id === selectedStreamId;
          return (
            <button
              key={stream.id}
              onClick={() => setSelectedStreamId(stream.id)}
              className={`flex items-center gap-2.5 p-3 rounded-xl border text-left transition-all ${
                isSelected 
                  ? 'bg-slate-800/90 border-blue-500 shadow-lg ring-1 ring-blue-500/40' 
                  : 'bg-slate-900/70 border-slate-800 hover:bg-slate-800/50 hover:border-slate-700'
              }`}
            >
              <div className="p-2 rounded-lg bg-slate-950 shrink-0">
                {getStreamIcon(stream.type)}
              </div>
              <div className="min-w-0">
                <span className="text-[11px] font-bold uppercase tracking-wider block text-slate-400">
                  Stream {stream.id.split('-')[0]}
                </span>
                <span className="text-xs font-semibold text-white truncate block">
                  {stream.name.split('. ')[1] || stream.name}
                </span>
              </div>
            </button>
          );
        })}
      </div>

      {/* Active Flow Pipeline Display */}
      <div className="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-slate-800 border border-slate-700">
              {getStreamIcon(activeStream.type)}
            </div>
            <div>
              <h3 className="text-lg font-bold text-white tracking-wide">{activeStream.name}</h3>
              <p className="text-xs text-slate-400">Deterministic end-to-end data pipeline & signal routing</p>
            </div>
          </div>
          <span className="px-3 py-1 text-xs font-semibold rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/30 self-start md:self-auto">
            Live Protocol Pathway
          </span>
        </div>

        {/* Step-by-Step Interactive Flow Cards */}
        <div className="mt-8 flex flex-col lg:flex-row items-stretch justify-between gap-4 relative">
          {activeStream.flow.map((step, idx) => (
            <React.Fragment key={idx}>
              <div className="flex-1 p-5 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-slate-700 transition relative flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/30">
                      Phase {idx + 1}: {step.step}
                    </span>
                    <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                  </div>
                  <h4 className="text-sm font-bold text-white mb-1.5 leading-snug">
                    {step.label}
                  </h4>
                  <p className="text-xs text-slate-400 leading-relaxed">
                    {step.desc}
                  </p>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-500">
                  <span>Latency: {idx === 0 ? '<5ms' : idx === 1 ? '<15ms' : '<50ms total'}</span>
                  <span className="text-blue-400 font-medium">Active Pipeline</span>
                </div>
              </div>

              {idx < activeStream.flow.length - 1 && (
                <div className="hidden lg:flex items-center justify-center text-slate-600 px-1">
                  <div className="flex flex-col items-center">
                    <span className="text-[10px] font-mono text-cyan-400 mb-1">
                      {idx === 0 ? 'Differential I2C / CSI' : 'Bluetooth / Haptics / LTE'}
                    </span>
                    <ArrowRight size={24} className="text-blue-500 animate-pulse" />
                  </div>
                </div>
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Interconnect Bus & Pinout Architecture Matrix */}
      <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 shadow-xl">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Radio size={18} className="text-cyan-400" />
            <h3 className="text-base font-bold text-white tracking-wide">
              Hardware Bus & Interconnect Protocol Matrix
            </h3>
          </div>
          <span className="text-xs font-mono text-slate-400">Physical Harness (J1: 20-Pin, J2: 14-Pin)</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950/80 text-[11px] font-semibold text-slate-400 uppercase tracking-wider border-b border-slate-800">
              <tr>
                <th className="py-2.5 px-3">Subsystem Link</th>
                <th className="py-2.5 px-3">Physical Bus</th>
                <th className="py-2.5 px-3">Master / Slave</th>
                <th className="py-2.5 px-3">Bandwidth / Rate</th>
                <th className="py-2.5 px-3">Safety Redundancy</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono text-[11px]">
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Dual Ultrasonic & Laser ToF</td>
                <td className="py-2.5 px-3 text-cyan-300">Diff I2C (PCA9615) + GPIO</td>
                <td className="py-2.5 px-3">ESP32-S3 → Tip PCB</td>
                <td className="py-2.5 px-3 text-emerald-400">400 kHz / 50ms cycle</td>
                <td className="py-2.5 px-3 text-amber-300">Hard Safety Path</td>
              </tr>
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Dual Cameras (Top + Bottom)</td>
                <td className="py-2.5 px-3 text-purple-300">22-pin CSI-2 + USB UVC</td>
                <td className="py-2.5 px-3">Cam Modules → RPi Zero</td>
                <td className="py-2.5 px-3 text-emerald-400">1 Gbps MIPI / 30 fps</td>
                <td className="py-2.5 px-3 text-slate-400">Switches OFF in Power-Save</td>
              </tr>
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Bluetooth Ear Assistant Link</td>
                <td className="py-2.5 px-3 text-blue-300">Bluetooth 5.x / LE Audio</td>
                <td className="py-2.5 px-3">RPi Zero → Bone-Conduction</td>
                <td className="py-2.5 px-3 text-emerald-400">2.4 GHz / Sub-30ms audio</td>
                <td className="py-2.5 px-3 text-slate-400">Handle siren backup</td>
              </tr>
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Dual Spatial PIR Motion Sensors</td>
                <td className="py-2.5 px-3 text-amber-300">Hardware Interrupt (INT)</td>
                <td className="py-2.5 px-3">PIR Domes → ESP32 / TCA9555</td>
                <td className="py-2.5 px-3 text-emerald-400">Asynchronous &lt;1ms</td>
                <td className="py-2.5 px-3 text-amber-300">Active in Deep Sleep</td>
              </tr>
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Inter-Processor Control Link</td>
                <td className="py-2.5 px-3 text-cyan-300">4-Wire UART (RTS/CTS) + IRQ</td>
                <td className="py-2.5 px-3">ESP32-S3 ↔ RPi Zero 2 W</td>
                <td className="py-2.5 px-3 text-emerald-400">921,600 baud packetized</td>
                <td className="py-2.5 px-3 text-amber-300">Hardware Handshake Flow</td>
              </tr>
              <tr className="hover:bg-slate-800/40 transition">
                <td className="py-2.5 px-3 font-semibold text-white font-sans">Emergency SOS Autonomous Link</td>
                <td className="py-2.5 px-3 text-pink-300">Direct AT UART + PWRKEY</td>
                <td className="py-2.5 px-3">ESP32-S3 → SIM7600G-H</td>
                <td className="py-2.5 px-3 text-emerald-400">115,200 baud direct AT</td>
                <td className="py-2.5 px-3 text-red-400">Bypasses RPi & Linux OS</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
