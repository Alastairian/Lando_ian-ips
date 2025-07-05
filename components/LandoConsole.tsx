import { useState } from 'react';

export default function LandoConsole() {
  const [input, setInput] = useState('');
  const [logs, setLogs] = useState<string[]>([]);

  const handleSubmit = async () => {
    if (!input.trim()) return;
    setLogs((prev) => [...prev, `> ${input}`]);
    const res = await fetch('/api/iqcl', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input }),
    });
    const data = await res.json();
    setLogs((prev) => [...prev, data.output]);
    setInput('');
  };

  return (
    <div className="bg-black p-4 rounded-xl shadow-lg">
      <div className="h-64 overflow-y-auto mb-2 whitespace-pre-wrap font-mono text-sm bg-gray-800 p-2 rounded">
        {logs.map((log, idx) => (
          <div key={idx}>{log}</div>
        ))}
      </div>
      <div className="flex">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
          className="flex-1 bg-gray-700 text-white p-2 rounded-l outline-none"
          placeholder="Enter IQCL command..."
        />
        <button
          onClick={handleSubmit}
          className="bg-blue-600 hover:bg-blue-700 p-2 rounded-r"
        >
          Send
        </button>
      </div>
    </div>
  );
}