export default function ScoreCard({ report }) {

    const score = report?.result?.score?.overall_score ?? 0;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold">
                Overall SEO Score
            </h2>

            <div className="text-6xl mt-6 font-bold text-blue-400">
                {score}
            </div>

            <p className="text-gray-400 mt-2">
                out of 100
            </p>

        </div>

    );

}