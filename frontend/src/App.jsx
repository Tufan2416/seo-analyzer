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

      if (err.response) {
        console.error("Status:", err.response.status);
        console.error("Data:", err.response.data);

        alert(
          err.response.data?.detail ||
          `Server Error (${err.response.status})`
        );
      } else if (err.request) {
        alert("Backend is not responding. Please try again in a few seconds.");
      } else {
        alert(err.message);
      }
    }

  };

  return (

    <div className="min-h-screen bg-slate-900 flex flex-col items-center text-white px-4 py-10">

      <h1 className="text-4xl md:text-6xl font-bold">
        SEO Analyzer
      </h1>

      <p className="mt-4 text-gray-400">
        Analyze any website's SEO in seconds
      </p>

      <input

        value={url}

        onChange={(e)=>setUrl(e.target.value)}

        placeholder="https://example.com"

        className="mt-10 w-full max-w-xl rounded-xl p-4 text-black"

      />

      <button

        onClick={analyzeWebsite}

        className="mt-6 w-full max-w-xs py-4 bg-blue-600 rounded-xl hover:bg-blue-700"

      >

        Analyze Website

      </button>
      {report && (

        <div className="mt-10 w-full max-w-3xl bg-slate-800 rounded-xl p-6">

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