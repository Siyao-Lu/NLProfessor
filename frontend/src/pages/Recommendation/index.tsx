import React from "react";
import Recommendation from "./recommendation";

const RecommendationList = () => {
    return (
        <div>
            <Recommendation
                courses={[
                    {
                        basedOn: ["machine learning", "team"],
                        courseName: "Conversational AI",
                        courseDept: "EECS",
                        courseNum: 449,
                    },
                    {
                        basedOn: ["machine learning", "team"],
                        courseName: "Conversational AI",
                        courseDept: "EECS",
                        courseNum: 449,
                    },
                    {
                        basedOn: ["machine learning", "team"],
                        courseName: "Conversational AI",
                        courseDept: "EECS",
                        courseNum: 449,
                    },
                    {
                        basedOn: ["machine learning", "team"],
                        courseName: "Conversational AI",
                        courseDept: "EECS",
                        courseNum: 449,
                    },
                ]}
                basedOn={["junior", "machine learning", "team"]}
            />
        </div>
    );
};
export default RecommendationList;