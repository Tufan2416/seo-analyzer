export default function SecurityCard({ report }) {

    const security = report.security;

    if (!security) return null;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Security
            </h2>

            <p>Headers Found : {security.headers_found}</p>

            <p>Missing : {security.headers_missing}</p>

            <p>Security Score : {security.score}/100</p>

        </div>

    );

}