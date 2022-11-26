import React from "react";
import { Link } from "react-router-dom";
import background from "./background.png";
import preview from "./preview.png";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./front.css";

const Front = () => {
  return (
    <div className="front-wrapper">
      <img className="background-img" src={background} alt="background" />
      <div className="front-content-wrapper">
        <div className="front-texts">
          <h1 className="front-title">
            Build Instant & Personalized Course Schedules
          </h1>
          <p className="front-description">
            Automate the way you search through course guide and Atlas
          </p>
          <Link className="btn btn-dark btn-lg" role="button" to="/chat">
            Try Now! <i className="bi bi-arrow-right-circle"></i>
          </Link>
        </div>
        <img className="preview-img" src={preview} alt="background" />
      </div>
    </div>
  );
};
export default Front;
