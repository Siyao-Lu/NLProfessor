import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import axios from 'axios';
import { Link } from "react-router-dom";
import './ChatBox.css';
import "bootstrap-icons/font/bootstrap-icons.css";

export default function ChatBox() {
    const userMsgRef = useRef<any>(null);
    const [userMsg, setUserMsg] = useState("");
    const [displayMsg, setDisplayMsg] = useState([] as any);

    const delay = (ms: number | undefined) => new Promise(
        resolve => setTimeout(resolve, ms)
    );

    const sendMSG = useCallback(async () => {
        await delay(1000);
        const res = await axios.post(`/api/receive`, { userMsg: userMsg });
        console.log(res);
        console.log(userMsg);
        setDisplayMsg((list: any) => [...list, res.data]);
    }, [userMsg, setDisplayMsg]);

    useEffect(() => {
        const initBotMsg =
            "Hi, I am NLProfessor, your smart course recommender, to start off, what is your current class standing?";
        setDisplayMsg([initBotMsg]);
    }, []);

    const handleSubmit = (e: any) => {
        e.preventDefault();
        e.target.reset();
        setDisplayMsg((list: any) => [...list, userMsg]);
        sendMSG();
    };

    return (
        <div className="chat-box-div">
            <div className="chat-box">
                <h1>ChatBox</h1>
            </div>
            <div className="chat-body">
                {displayMsg.map((msg: string) => (
                    <div className="message">{msg}</div>
                ))}
            </div>
            <div className="userInputBar">
                <form onSubmit={handleSubmit}>
                    <input ref={userMsgRef} type="text" placeholder="type your concerns!" onChange={e => setUserMsg(e.target.value)} />
                    <input type="reset" defaultValue="Reset" />
                    <button type="submit">submit</button>
                </form>
            </div>
            <Link className="btn btn-secondary btn-lg" role="button" to="/recommendations">
                Generate Report!
            </Link>
        </div>
    );
}
