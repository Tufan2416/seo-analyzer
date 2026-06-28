export default function TechnicalCard({ report }) {

    const tech = report?.result?.technical;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Technical SEO
            </h2>

            <p>HTTPS : {tech?.https ? "Yes" : "No"}</p>

            <p>Robots : {tech?.robots_txt ? "Yes" : "No"}</p>

            <p>Sitemap : {tech?.sitemap_xml ? "Yes" : "No"}</p>

            <p>Mobile : {tech?.mobile_friendly ? "Yes" : "No"}</p>

        </div>

    );

}