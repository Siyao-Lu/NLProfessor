import React, { useState, useEffect } from "react";
import axios from "axios";
import Recommendation from "./recommendation";

const RecommendationList = () => {
  const [data, setData] = useState();
  useEffect(() => {
    axios
      .get(`https://de5e-35-3-45-49.ngrok.io/report/`, {
        headers: {
          "ngrok-skip-browser-warning": "69420",
          "Access-Control-Allow-Origin": "*",
        },
      })
      .then((res) => {
        console.log(res.data);
        setData(res.data);
      });
  }, []);
  return (
    <div>
      {data && (
        <Recommendation
          courses={data["courses"]}
          basedOn={data["basedOn"]}
          name={data["name"]}
        />
      )}
    </div>
  );
};
export default RecommendationList;
