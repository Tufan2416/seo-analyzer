export default function LinkCard({ report }) {

    const links = report?.result?.links;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold mb-4">
                Links
            </h2>

            <p>Internal : {links?.internal_links}</p>

            <p>External : {links?.external_links}</p>

            <p>Total : {links?.total_links}</p>

        </div>

    );

}