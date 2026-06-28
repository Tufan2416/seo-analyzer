import ScoreCard from "./ScoreCard";
import PerformanceCard from "./PerformanceCard";
import MetaCard from "./MetaCard";
import HeadingCard from "./HeadingCard";
import ImageCard from "./ImageCard";
import LinkCard from "./LinkCard";
import TechnicalCard from "./TechnicalCard";
import ContentCard from "./ContentCard";
import RecommendationCard from "./RecommendationCard";
import SocialCard from "./SocialCard";
import CoreWebVitalsCard from "./CoreWebVitalsCard";
import IndexabilityCard from "./IndexabilityCard";
import SecurityCard from "./SecurityCard";
import StructuredDataCard from "./StructuredDataCard";

export default function Dashboard({ report }) {

    return (

        <div className="mt-10 w-full max-w-7xl">

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                <ScoreCard report={report} />
                <PerformanceCard report={report} />
                <MetaCard report={report} />

                <HeadingCard report={report} />
                <ImageCard report={report} />
                <TechnicalCard report={report} />
                <SecurityCard report={report} />

                <IndexabilityCard report={report} />

                <LinkCard report={report} />
                <ContentCard report={report} />
                <RecommendationCard report={report} />

                <SocialCard report={report} />
                <StructuredDataCard report={report} />

                <CoreWebVitalsCard report={report} />
                
            </div>

        </div>

    );

}