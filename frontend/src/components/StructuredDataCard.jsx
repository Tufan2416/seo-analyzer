export default function StructuredDataCard({ report }) {

    const data = report.structured_data;

    if (!data) return null;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Structured Data
            </h2>

            <p>JSON-LD : {data.json_ld}</p>

            <p>Microdata : {data.microdata}</p>

            <p>RDFa : {data.rdfa}</p>

            <p>Total : {data.total}</p>

            <p>Status : {data.status}</p>

        </div>

    );

}