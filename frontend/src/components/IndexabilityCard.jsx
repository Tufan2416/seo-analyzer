export default function IndexabilityCard({ report }) {

    const data = report?.result?.indexability;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold mb-4">
                Indexability
            </h2>

            <p>
                Indexable :
                {data?.indexable ? " ✅ Yes" : " ❌ No"}
            </p>

            <p>
                Meta Robots :
                {data?.meta_robots || " None"}
            </p>

            <p>
                Noindex :
                {data?.noindex ? " Yes" : " No"}
            </p>

            <p>
                Nofollow :
                {data?.nofollow ? " Yes" : " No"}
            </p>

            <p>
                X-Robots-Tag :
                {data?.x_robots_tag || " None"}
            </p>

        </div>

    );

}