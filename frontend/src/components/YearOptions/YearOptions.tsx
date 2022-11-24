import React from "react";

import "./YearOptions.css";

const LearningOptions = (props: any) => {
    const options = [
        { text: "Freshman", id: 1 },
        { text: "Sophomore", id: 2 },
        { text: "Junior", id: 3 },
        { text: "Senior", id: 4 },
    ];

    const optionsMarkup = options.map((option) => (
        <button
            className="year-option-button"
            key={option.id}
        >
            {option.text}
        </button>
    ));

    return <div className="learning-options-container">{optionsMarkup}</div>;
};

export default LearningOptions;