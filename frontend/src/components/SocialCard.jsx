export default function SocialCard({ report }) {

    const social = report?.social;

    const ogPresent = social?.open_graph
        ? Object.keys(social.open_graph).length
        : 0;

    const twitterPresent = social?.twitter
        ? Object.keys(social.twitter).length
        : 0;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">

            <h2 className="text-xl font-bold mb-4">
                Social SEO
            </h2>

            <p>
                Open Graph :
                {ogPresent > 0 ? " ✅ Present" : " ❌ Missing"}
            </p>

            <p>
                Twitter Cards :
                {twitterPresent > 0 ? " ✅ Present" : " ❌ Missing"}
            </p>

            <br />

            <p>
                Open Graph Tags : {ogPresent}
            </p>

            <p>
                Twitter Tags : {twitterPresent}
            </p>

        </div>

    );

}