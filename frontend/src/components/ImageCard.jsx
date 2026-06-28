export default function ImageCard({ report }) {

    const images = report?.result?.images;

    return (

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg w-full overflow-hidden">

            <h2 className="text-xl font-bold mb-4">
                Images
            </h2>

            <p>Total Images : {images?.total_images}</p>

            <p>Missing ALT : {images?.missing_alt}</p>

            <br />

            <p>{images?.status}</p>

        </div>

    );

}