import React from 'react';
import { X, ShieldAlert, Cpu, Zap, Radio, Activity, MapPin, Wrench, AlertTriangle, CheckCircle, ExternalLink } from 'lucide-react';

export default function ComponentDrawer({ component, onClose, onSelectRelated }) {
  if (!component) return null;

  const isHardSafety = component.safetyCriticality?.includes('HARD SAFETY');

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm transition-opacity animate-in fade-in">
      <div 
        className="w-full max-w-xl h-full bg-slate-900 border-l border-slate-700/80 p-6 overflow-y-auto shadow-2xl flex flex-col justify-between"
        onClick={(e) => e.stopPropagation()}
      >
        <div>
          {/* Header */}
          <div className="flex items-start justify-between pb-4 border-b border-slate-800">
            <div>
              <div className="flex items-center gap-2 mb-1.5 flex-wrap">
                <span className="px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wider rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/30">
                  {component.category}
                </span>
                <span className="px-2.5 py-0.5 text-xs font-mono font-medium rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                  {component.refDes || 'MOD'}
                </span>
                {isHardSafety ? (
                  <span className="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-red-500/20 text-red-400 border border-red-500/40 flex items-center gap-1">
                    <ShieldAlert size={12} /> Hard Safety Path
                  </span>
                ) : (
                  <span className="px-2.5 py-0.5 text-xs font-medium rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/20">
                    {component.safetyCriticality}
                  </span>
                )}
              </div>
              <h2 className="text-xl font-bold text-white tracking-tight">{component.name}</h2>
              <p className="text-sm font-mono text-cyan-400 mt-0.5">{component.partNumber}</p>
            </div>
            <button 
              onClick={onClose}
              className="p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700 transition"
              title="Close details"
            >
              <X size={18} />
            </button>
          </div>

          {/* Quick SIH Highlight Box */}
          <div className="mt-4 p-3 rounded-lg bg-gradient-to-r from-blue-950/60 to-purple-950/60 border border-blue-800/40 text-sm">
            <span className="font-semibold text-blue-300 flex items-center gap-1.5 mb-1">
              <CheckCircle size={15} className="text-blue-400" /> SIH PPT Innovation Highlight:
            </span>
            <p className="text-slate-200 text-xs leading-relaxed pl-5">
              {component.sihSlideHighlight}
            </p>
          </div>

          {/* Technical Specs Grid */}
          <div className="mt-5 grid grid-cols-2 gap-3 text-xs">
            <div className="p-3 rounded-lg bg-slate-800/60 border border-slate-700/60">
              <span className="text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
                <MapPin size={14} className="text-emerald-400" /> Physical Location
              </span>
              <p className="text-slate-200 font-medium">{component.location}</p>
            </div>

            <div className="p-3 rounded-lg bg-slate-800/60 border border-slate-700/60">
              <span className="text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
                <Radio size={14} className="text-purple-400" /> Bus / Interface
              </span>
              <p className="text-slate-200 font-medium">{component.interfaces}</p>
            </div>

            <div className="p-3 rounded-lg bg-slate-800/60 border border-slate-700/60">
              <span className="text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
                <Zap size={14} className="text-amber-400" /> Power Rail & Draw
              </span>
              <p className="text-slate-200 font-medium">{component.powerRail}</p>
              <p className="text-slate-400 text-[11px] mt-0.5">{component.powerConsumption}</p>
            </div>

            <div className="p-3 rounded-lg bg-slate-800/60 border border-slate-700/60">
              <span className="text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
                <Activity size={14} className="text-cyan-400" /> Frequency / Latency
              </span>
              <p className="text-slate-200 font-medium">{component.frequency}</p>
            </div>
          </div>

          {/* Detailed Description */}
          <div className="mt-5">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
              Functional Description & Operation
            </h4>
            <div className="p-4 rounded-lg bg-slate-950/70 border border-slate-800 text-sm text-slate-300 leading-relaxed">
              {component.description}
            </div>
          </div>

          {/* Safety Criticality & Fallback */}
          <div className="mt-4">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
              Safety Redundancy & Failure Fallback
            </h4>
            <div className="p-3.5 rounded-lg bg-amber-950/20 border border-amber-800/40 text-xs text-amber-200/90 leading-relaxed flex items-start gap-2.5">
              <AlertTriangle size={16} className="text-amber-400 shrink-0 mt-0.5" />
              <div>
                <span className="font-semibold text-amber-300">Fail-Safe Behavior: </span>
                {component.failureFallback}
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex items-center justify-between text-xs text-slate-500">
          <span>Smart Intelligent Cane Architecture • Rev B</span>
          <button 
            onClick={onClose}
            className="px-4 py-1.5 rounded-md bg-blue-600 hover:bg-blue-500 text-white font-medium transition"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
