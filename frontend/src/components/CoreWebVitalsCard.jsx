export default function CoreWebVitalsCard({ report }) {

    const cwv = report?.core_web_vitals;

    if (!cwv) {
        return (
            <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">
                <h2 className="text-xl font-bold mb-4">
                    Core Web Vitals
                </h2>
                <p>Data not available.</p>
            </div>
        );
    }

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Core Web Vitals
            </h2>

            <p>Load Time : {cwv.load_time}s</p>
            <p>Page Size : {cwv.page_size_kb} KB</p>
            <p>Compression : {cwv.compression}</p>
            <p>Cache Control : {cwv.cache_control}</p>
            <p>Server : {cwv.server}</p>

        </div>

    );

}