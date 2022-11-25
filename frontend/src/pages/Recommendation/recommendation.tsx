import React from "react";
import { RecCourse } from "../../components/RecCourse/RecCourse";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import './recommendation.css';

export type CourseRec = {
  basedOn: string[];
  courseName: string;
  courseDept: string;
  courseNum: number;
};

type AppProps = {
  courses: CourseRec[];
  basedOn: string[];
};

const Recommendation = ({ courses, basedOn }: AppProps) => {
  return (
    <div className="rec-page">
      <div className="rec-title">
        <div>
          <h1 className="text-center">Your personalized recommendations</h1>
        </div>
        <div className="text-muted text-center">
          Key words: {basedOn.join(", ")}
        </div>
      </div>
      <div className="rec-cards">
        {courses.map((course) => (
          <RecCourse
            basedOn={course.basedOn}
            courseName={course.courseName}
            courseDept={course.courseDept}
            courseNum={course.courseNum}
          />
        ))}
      </div>
    </div>
  );
};
export default Recommendation;
