export default function MetaCard({ report }) {

    const meta = report?.result?.meta;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Meta Tags
            </h2>

            <p>Title Length: {meta?.title?.length}</p>
            <p>{meta?.title?.status}</p>

            <br />

            <p>Description Length: {meta?.meta_description?.length}</p>
            <p>{meta?.meta_description?.status}</p>

        </div>

    );

}