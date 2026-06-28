export default function PerformanceCard({ report }) {

    const performance = report?.result?.performance;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Performance
            </h2>

            <p>Response Time: {performance?.response_time_seconds} sec</p>
            <p>Page Size: {performance?.page_size_kb} KB</p>
            <p>Status Code: {performance?.status_code}</p>

        </div>

    );

}