export default function HeadingCard({ report }) {

    const headings = report?.result?.headings;

    if (!headings) return null;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Headings
            </h2>

            <p>H1 : {headings.h1}</p>
            <p>H2 : {headings.h2}</p>
            <p>H3 : {headings.h3}</p>
            <p>H4 : {headings.h4}</p>
            <p>H5 : {headings.h5}</p>
            <p>H6 : {headings.h6}</p>

            <p>Total : {headings.total}</p>

            <br />

            <p>
                <strong>Status:</strong> {headings.status}
            </p>

            {headings.issues?.length > 0 ? (
                <div className="mt-4">
                    <strong>Issues</strong>

                    <ul className="list-disc ml-5 mt-2 space-y-1">
                        {headings.issues.map((issue, index) => (
                            <li key={index}>
                                {issue}
                            </li>
                        ))}
                    </ul>
                </div>
            ) : (
                <p className="text-green-400 mt-3">
                    ✅ Heading hierarchy is valid.
                </p>
            )}

        </div>

    );
}