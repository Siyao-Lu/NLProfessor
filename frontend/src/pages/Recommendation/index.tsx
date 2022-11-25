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
            basedOn: ["junior", "team"],
            courseName: "Web Systems",
            courseDept: "EECS",
            courseNum: 485,
          },
          {
            basedOn: ["machine learning"],
            courseName: "Intro Natural Language processing",
            courseDept: "EECS",
            courseNum: 487,
          },
          {
            basedOn: ["junior"],
            courseName: "Intro Algorithms",
            courseDept: "EECS",
            courseNum: 477,
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
