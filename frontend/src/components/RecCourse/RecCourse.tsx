import React from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import './RecCourse.css';

type AppProps = {
  basedOn: string[];
  courseName: string;
  courseDept: string;
  courseNum: number;
};

export const RecCourse = ({
  basedOn,
  courseName,
  courseDept,
  courseNum,
}: AppProps) => {
  return (
    <Card className="rec-card text-center">
      <Card.Header>Recommended based on {basedOn.join(", ")}</Card.Header>
      <Card.Body>
        <Card.Title>
          {courseDept} {courseNum}: {courseName}
        </Card.Title>
        <Card.Text></Card.Text>
        <a
          href={`https://atlas.ai.umich.edu/course/${courseDept} ${courseNum}`}
          target="_blank"
          rel="noreferrer"
        >
          <Button variant="primary">
            <i className="bi bi-box-arrow-up-right"></i> Atlas
          </Button>
        </a>{" "}
        <a
          href={`https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=w_23_2420&department=${courseDept}&catalog=${courseNum}`}
          target="_blank"
          rel="noreferrer"
        >
          <Button variant="primary">
            <i className="bi bi-box-arrow-up-right"></i> Course Guide
          </Button>
        </a>
      </Card.Body>
    </Card>
  );
};
