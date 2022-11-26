import React from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import ProgressBar from "react-bootstrap/ProgressBar";
import Accordion from "react-bootstrap/Accordion";
import "./RecCourse.css";

type AppProps = {
  basedOn: string[];
  courseName: string;
  courseDept: string;
  courseDesc: string;
  courseNum: number;
  workload: number;
};

export const RecCourse = ({
  basedOn,
  courseName,
  courseDept,
  courseDesc,
  courseNum,
  workload,
}: AppProps) => {
  return (
    <Card className="rec-card text-center">
      <Card.Header>Recommended based on {basedOn.join(", ")}</Card.Header>
      <Card.Body>
        <Card.Title>
          {courseDept} {courseNum}: {courseName}
        </Card.Title>
        <Card.Text>
          <Accordion flush>
            <Accordion.Item eventKey="0">
              <Accordion.Header>Detailed description</Accordion.Header>
              <Accordion.Body>{courseDesc}</Accordion.Body>
            </Accordion.Item>
          </Accordion>
        </Card.Text>
        {workload === 0 ? (
          <div className="no-data-placeholder text-muted">
            <i className="bi bi-exclamation-triangle"></i> workload data
            unavaliable
          </div>
        ) : (
          <ProgressBar
            now={(workload * 100) / 4}
            label={`Workload: ${(workload * 100) / 4}%`}
          />
        )}
        <br />
        <div>
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
        </div>
      </Card.Body>
    </Card>
  );
};
