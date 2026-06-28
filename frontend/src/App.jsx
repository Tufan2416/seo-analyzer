import { useState } from "react";
import api from "./api/api";
import Dashboard from "./components/Dashboard";
function App() {

  const [url, setUrl] = useState("");
  const [report, setReport] = useState(null);

  const analyzeWebsite = async () => {

    if (!url) {
      alert("Please enter a URL");
      return;
    }

    try {

      const response = await api.post("/analyze", {
        url: url
      });

      const jobId = response.data.job_id;

      const result = await api.get(`/results/${jobId}`);

      setReport(result.data);

    } catch (err) {
      console.error(err);
      alert("Backend connection failed");
    }

  };

  return (

    <div className="min-h-screen bg-slate-900 flex flex-col justify-center items-center text-white">

      <h1 className="text-5xl font-bold">
        SEO Analyzer
      </h1>

      <p className="mt-4 text-gray-400">
        Analyze any website's SEO in seconds
      </p>

      <input

        value={url}

        onChange={(e)=>setUrl(e.target.value)}

        placeholder="https://example.com"

        className="mt-10 w-[500px] rounded-xl p-4 text-black"

      />

      <button

        onClick={analyzeWebsite}

        className="mt-6 px-8 py-4 bg-blue-600 rounded-xl hover:bg-blue-700"

      >

        Analyze Website

      </button>
      {report && (

        <div className="mt-10 w-[700px] bg-slate-800 rounded-xl p-6">

        <h2 className="text-2xl font-bold mb-4">
        SEO Report
        </h2>

        <p>
        <b>Status:</b> {report.status}
        </p>

        <Dashboard report={report} />

        </div>

      )}
    </div>

  );

}

export default App;