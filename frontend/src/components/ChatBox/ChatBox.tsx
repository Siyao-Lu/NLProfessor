import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import UserInputBar from './InputBar';
import './ChatBox.css';

export default function ChatBox() {
    // const chatRef = useRef(null);
    // const [msg, setMsg] = useState("");
    // useEffect(() => {
    //     var initMsg =
    //         "Hi, I am NLProfessor, your smart course recommender, to start off, what is your current class standing?";
    //     setMsg(initMsg);
    // }, []);

    return (
        <div className="chat-box-div">
            <div className="chat-box">
                <h1>ChatBox</h1>
            </div>
            <UserInputBar />
        </div>
    );
}
