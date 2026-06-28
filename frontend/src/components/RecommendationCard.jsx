export default function RecommendationCard({ report }) {

    const result = report?.result;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold mb-4">
                Recommendations
            </h2>

            <ul className="list-disc ml-5 space-y-2">

                {!result?.technical?.sitemap_xml &&
                    <li>Add a sitemap.xml</li>}

                {result?.images?.missing_alt > 0 &&
                    <li>Add ALT text to images</li>}

                {result?.headings?.h1_count > 1 &&
                    <li>Use only one H1 tag</li>}

                {result?.meta?.title?.status !== "Good" &&
                    <li>Optimize title length</li>}

                {result?.meta?.meta_description?.status !== "Good" &&
                    <li>Optimize meta description</li>}

            </ul>

        </div>

    );

}