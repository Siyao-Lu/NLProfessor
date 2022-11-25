import React from "react";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";
import background from "./background.png";
import preview from "./preview.png";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./front.css";

const Front = () => {
  return (
    <div className="front-wrapper">
      <img className="background-img" src={background} alt="background" />
      <div className="front-content-wrapper">
        <div className="front-texts">
          <h1>Build Instant & Personalized Course Schedules</h1>
          <p>Automate the way you search through course guide and Atlas</p>
          <Link className="btn btn-primary" role="button" to="/chat">
            Try Now! <i className="bi bi-arrow-right-circle"></i>
          </Link>
        </div>
        <img className="preview-img" src={preview} alt="background" />
      </div>
    </div>
  );
};
export default Front;
