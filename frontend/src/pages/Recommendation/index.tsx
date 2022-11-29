import React, { useState, useEffect } from "react";
import axios from "axios";
import Recommendation from "./recommendation";

const RecommendationList = () => {
  const [data, setData] = useState();
  useEffect(() => {
    axios.get(`http://localhost:3001/api/send`).then((res) => {
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
