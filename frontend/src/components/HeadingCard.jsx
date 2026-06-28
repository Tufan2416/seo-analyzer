export default function HeadingCard({ report }) {

    const headings = report?.result?.headings;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold mb-4">
                Headings
            </h2>

            <p>H1 : {headings?.h1_count}</p>
            <p>H2 : {headings?.h2_count}</p>
            <p>Total : {headings?.total_headings}</p>

            <br />

            <p>{headings?.status}</p>

        </div>

    );

}