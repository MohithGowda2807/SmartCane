import React, { useState } from 'react';
import { 
  ChevronRight, ChevronDown, Eye, ShieldAlert, Cpu, 
  Sparkles, Radio, Zap, Activity, Info, Search 
} from 'lucide-react';
import { DOMAINS, COMPONENTS } from '../data/architectureData';

export default function TreeView({ onSelectComponent, searchQuery, setSearchQuery }) {
  // State to track which domains are expanded
  const [expandedDomains, setExpandedDomains] = useState({
    perception: true,
    'safety-controller': true,
    'edge-ai': true,
    'audio-hmi': true,
    mechanical: false,
    power: false,
    'connectivity-cloud': false,
  });

  const toggleDomain = (domainId) => {
    setExpandedDomains(prev => ({
      ...prev,
      [domainId]: !prev[domainId]
    }));
  };

  const expandAll = () => {
    const all = {};
    DOMAINS.forEach(d => { all[d.id] = true; });
    setExpandedDomains(all);
  };

  const collapseAll = () => {
    const none = {};
    DOMAINS.forEach(d => { none[d.id] = false; });
    setExpandedDomains(none);
  };

  // Filter components based on search query
  const filteredComponents = COMPONENTS.filter(c => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    return (
      c.name.toLowerCase().includes(q) ||
      c.partNumber.toLowerCase().includes(q) ||
      c.category.toLowerCase().includes(q) ||
      c.description.toLowerCase().includes(q) ||
      c.interfaces.toLowerCase().includes(q) ||
      c.location.toLowerCase().includes(q)
    );
  });

  return (
    <div className="w-full">
      {/* Search & Actions Bar */}
      <div className="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 p-4 rounded-xl bg-slate-900/80 border border-slate-800">
        <div className="relative w-full md:w-96">
          <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Search components, chips, pinouts (e.g. PIR, camera, I2C, ESP32)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-4 py-2 text-sm bg-slate-950 border border-slate-700/80 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 transition"
          />
          {searchQuery && (
            <button 
              onClick={() => setSearchQuery('')}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-white"
            >
              Clear
            </button>
          )}
        </div>

        <div className="flex items-center gap-2 self-end md:self-center">
          <button
            onClick={expandAll}
            className="px-3 py-1.5 text-xs font-medium rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
          >
            Expand All Branches
          </button>
          <button
            onClick={collapseAll}
            className="px-3 py-1.5 text-xs font-medium rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
          >
            Collapse All
          </button>
        </div>
      </div>

      {/* Main Tree Container */}
      <div className="space-y-4">
        {DOMAINS.map((domain) => {
          const domainComponents = filteredComponents.filter(c => c.domain === domain.id);
          const isExpanded = expandedDomains[domain.id] || Boolean(searchQuery);

          if (searchQuery && domainComponents.length === 0) {
            return null; // hide empty domain when searching
          }

          return (
            <div 
              key={domain.id}
              className="rounded-xl bg-slate-900/90 border border-slate-800 overflow-hidden shadow-lg transition-all"
            >
              {/* Domain Root Node (Clickable Header) */}
              <div 
                onClick={() => toggleDomain(domain.id)}
                className="flex items-center justify-between p-4 cursor-pointer hover:bg-slate-800/50 transition select-none"
                style={{ borderLeft: `5px solid ${domain.color}` }}
              >
                <div className="flex items-center gap-3">
                  <div className="p-1 rounded bg-slate-800 text-slate-300">
                    {isExpanded ? <ChevronDown size={18} /> : <ChevronRight size={18} />}
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <h3 className="text-base font-bold text-white tracking-wide">
                        {domain.name}
                      </h3>
                      <span 
                        className="text-[10px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded-full"
                        style={{ backgroundColor: `${domain.color}20`, color: domain.color, border: `1px solid ${domain.color}50` }}
                      >
                        {domain.badge}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5 line-clamp-1">
                      {domain.description}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className="text-xs font-mono px-2.5 py-1 rounded-md bg-slate-800 text-slate-300">
                    {domainComponents.length} {domainComponents.length === 1 ? 'part' : 'parts'}
                  </span>
                </div>
              </div>

              {/* Children Nodes (Components List) */}
              {isExpanded && (
                <div className="p-4 pt-1 bg-slate-950/40 border-t border-slate-800/60">
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
                    {domainComponents.map((comp) => {
                      const isHardSafety = comp.safetyCriticality?.includes('HARD SAFETY');
                      const isNewFeature = comp.name.includes('Top') || 
                                           comp.name.includes('Bottom Pavement Camera') || 
                                           comp.name.includes('PIR') || 
                                           comp.name.includes('Bluetooth') || 
                                           comp.name.includes('Ultrasonic');

                      return (
                        <div
                          key={comp.id}
                          onClick={() => onSelectComponent(comp)}
                          className="group relative flex flex-col justify-between p-3.5 rounded-lg bg-slate-900/90 border border-slate-800 hover:border-blue-500/80 hover:bg-slate-800/80 cursor-pointer transition shadow-sm hover:shadow-md"
                        >
                          {/* Card Top: Category & Tags */}
                          <div>
                            <div className="flex items-center justify-between mb-2">
                              <span className="text-[11px] font-mono text-slate-400 bg-slate-800 px-2 py-0.5 rounded">
                                {comp.refDes || 'MOD'}
                              </span>

                              <div className="flex items-center gap-1.5">
                                {isNewFeature && (
                                  <span className="text-[10px] font-bold px-1.5 py-0.2 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 flex items-center gap-1">
                                    <Sparkles size={10} /> NEW
                                  </span>
                                )}
                                {isHardSafety && (
                                  <span className="text-[10px] font-bold px-1.5 py-0.2 rounded bg-red-500/20 text-red-400 border border-red-500/40 flex items-center gap-1" title="Deterministic Hard Safety Path">
                                    <ShieldAlert size={10} /> Safety
                                  </span>
                                )}
                              </div>
                            </div>

                            <h4 className="text-sm font-semibold text-white group-hover:text-blue-400 transition leading-snug">
                              {comp.name}
                            </h4>
                            <p className="text-xs font-mono text-cyan-400 mt-0.5 line-clamp-1">
                              {comp.partNumber}
                            </p>
                            <p className="text-xs text-slate-400 mt-2 line-clamp-2">
                              {comp.sihSlideHighlight}
                            </p>
                          </div>

                          {/* Card Bottom: Interface & Click prompt */}
                          <div className="mt-3 pt-2.5 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
                            <span className="truncate max-w-[170px]" title={comp.interfaces}>
                              {comp.interfaces.split('(')[0]}
                            </span>
                            <span className="text-blue-400 font-medium group-hover:underline flex items-center gap-1 shrink-0">
                              Inspect <Eye size={12} />
                            </span>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
