import React, { useState } from 'react';
import { 
  GitFork, Activity, Layers, Presentation, Search, 
  Sparkles, ShieldAlert, Cpu, Radio, Video, Mic, 
  HelpCircle, Eye, Download, ExternalLink, Zap 
} from 'lucide-react';
import { SYSTEM_METRICS, COMPONENTS } from './data/architectureData';
import TreeView from './components/TreeView';
import FlowView from './components/FlowView';
import SlidePresentationMode from './components/SlidePresentationMode';
import Hardware3DView from './components/Hardware3DView';
import ComponentDrawer from './components/ComponentDrawer';

export default function App() {
  const [activeTab, setActiveTab] = useState('slide'); // default to 'slide' as requested for PPT!
  const [selectedComponent, setSelectedComponent] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <div className="min-h-screen bg-[#070b14] text-slate-100 flex flex-col font-sans selection:bg-blue-600 selection:text-white">
      {/* Top Main Navigation Header */}
      <header className="sticky top-0 z-40 bg-[#070b14]/90 backdrop-blur-md border-b border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 py-3.5 flex flex-col md:flex-row items-center justify-between gap-4">
          
          {/* Brand & Title */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-cyan-400 flex items-center justify-center shadow-lg shadow-blue-500/20 font-black text-white text-lg">
              SC
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-black text-white tracking-tight">SMART INTELLIGENT CANE</h1>
                <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-blue-500/20 text-blue-400 border border-blue-500/30">
                  SIH 2026
                </span>
                <span className="px-1.5 py-0.5 text-[9px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 flex items-center gap-1">
                  <Sparkles size={9} /> Rev B
                </span>
              </div>
              <p className="text-xs text-slate-400">
                End-to-End System Architecture, Hardware Schematic & Edge AI Dataflow
              </p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-slate-900 border border-slate-800 text-xs font-semibold">
            <button
              onClick={() => setActiveTab('slide')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition-all ${
                activeTab === 'slide'
                  ? 'bg-blue-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Presentation size={15} />
              <span>1-Slide PPT View</span>
            </button>

            <button
              onClick={() => setActiveTab('tree')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition-all ${
                activeTab === 'tree'
                  ? 'bg-blue-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <GitFork size={15} />
              <span>Tree Architecture</span>
            </button>

            <button
              onClick={() => setActiveTab('flow')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition-all ${
                activeTab === 'flow'
                  ? 'bg-blue-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Activity size={15} />
              <span>Flow Diagrams</span>
            </button>

            <button
              onClick={() => setActiveTab('3d')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition-all ${
                activeTab === '3d'
                  ? 'bg-blue-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Layers size={15} />
              <span>3D Model & Renders</span>
            </button>
          </div>

        </div>

        {/* Global Key Specs Status Strip */}
        <div className="bg-slate-950/80 border-t border-slate-800/60 py-1.5 px-4 text-[11px] text-slate-400 overflow-x-auto">
          <div className="max-w-7xl mx-auto flex items-center justify-between gap-6 whitespace-nowrap">
            <div className="flex items-center gap-5">
              <span className="flex items-center gap-1.5 text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-red-400" />
                <strong>Safety Loop:</strong> {SYSTEM_METRICS.primarySafetyLoop}
              </span>
              <span className="flex items-center gap-1.5 text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-purple-400" />
                <strong>Cameras:</strong> {SYSTEM_METRICS.cameraConfig}
              </span>
              <span className="flex items-center gap-1.5 text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                <strong>PIR Sensors:</strong> {SYSTEM_METRICS.pirConfig}
              </span>
              <span className="flex items-center gap-1.5 text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <strong>Ear Assistant:</strong> {SYSTEM_METRICS.audioAssistant}
              </span>
            </div>

            <span className="text-cyan-400 font-mono text-[10px]">
              {SYSTEM_METRICS.batteryLifePowerSave}
            </span>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        {activeTab === 'slide' && (
          <SlidePresentationMode onSelectComponent={setSelectedComponent} />
        )}

        {activeTab === 'tree' && (
          <TreeView 
            onSelectComponent={setSelectedComponent} 
            searchQuery={searchQuery}
            setSearchQuery={setSearchQuery}
          />
        )}

        {activeTab === 'flow' && (
          <FlowView onSelectComponent={setSelectedComponent} />
        )}

        {activeTab === '3d' && (
          <Hardware3DView onSelectComponent={setSelectedComponent} />
        )}
      </main>

      {/* Slide-over Component Inspector Drawer */}
      <ComponentDrawer 
        component={selectedComponent} 
        onClose={() => setSelectedComponent(null)} 
      />

      {/* Footer */}
      <footer className="bg-slate-950 border-t border-slate-900 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <span>Smart India Hackathon (SIH 2026) • Team Submission</span>
          <span>Hardware Architecture & Interactive System Flow Model</span>
          <span className="text-slate-400 font-mono">ESP32-S3 + Raspberry Pi Zero 2 W</span>
        </div>
      </footer>
    </div>
  );
}
