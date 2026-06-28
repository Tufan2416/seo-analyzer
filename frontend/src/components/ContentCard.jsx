export default function ContentCard({ report }) {

    const content = report?.result?.content;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Content
            </h2>

            <p>Words : {content?.word_count}</p>

            <p>Keyword : {content?.keyword_checked}</p>

            <p>Occurrences : {content?.keyword_occurrences}</p>

            <p>{content?.readability}</p>

        </div>

    );

}