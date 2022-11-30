import React from "react";
import { RecCourse } from "../../components/RecCourse/RecCourse";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./recommendation.css";
import styles from "./rec-nav.module.css";

export type CourseRec = {
  basedOn: string[];
  name: string;
  courseDept: string;
  desc: string;
  number: number;
  workload: number;
};

type AppProps = {
  courses: CourseRec[];
  basedOn: string[];
  name: string;
};

const Recommendation = ({ courses, basedOn, name }: AppProps) => {
  return (
    <div className="rec-page">
      <style>
        {
          ".navbar { background-color: #F1F6FD !important; box-shadow: 0 0 .5em rgba(0, 0, 0, .5);"
        }
      </style>
      <div className="rec-title">
        <div>
          <h1 className="text-center">
            {name.charAt(0).toUpperCase() + name.slice(1)}'s personalized
            recommendations
          </h1>
        </div>
        <div className="text-muted text-center">
          Key words: {basedOn.join(", ")}
        </div>
      </div>
      <div className="rec-cards">
        {courses.map((course) => (
          <RecCourse
            basedOn={course.basedOn}
            courseName={course.name}
            courseDept={course.courseDept}
            courseNum={course.number}
            courseDesc={course.desc}
            workload={course.workload}
          />
        ))}
      </div>
    </div>
  );
};
export default Recommendation;
