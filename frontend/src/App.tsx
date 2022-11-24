import React from "react";
import {
  Recommendation,
  CourseRec,
} from "./pages/recommendations/recommendation";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

function App() {
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
        basedOn={["juniro", "machine learning", "team"]}
      />
    </div>
  );
}

export default App;
