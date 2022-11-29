import React, { useState, useEffect } from "react";
import axios from "axios";
import Recommendation from "./recommendation";

const RecommendationList = () => {
  const [data, setData] = useState();
  useEffect(() => {
    axios
      .get(
        `https://427f-2601-400-8001-2a70-cc0-7893-368b-8933.ngrok.io/report/`
      )
      .then((res) => {
        setData(res.data);
      });
  }, []);
  return (
    <div>
      {data && (
        <Recommendation courses={data["courses"]} basedOn={data["basedOn"]} />
      )}
    </div>
  );
};
export default RecommendationList;
