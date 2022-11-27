import React, {
  useState,
  useEffect,
  useRef,
  useMemo,
  useCallback,
} from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import "./ChatBox.css";
import "bootstrap-icons/font/bootstrap-icons.css";

export default function ChatBox() {
  const userMsgRef = useRef<any>(null);
  const [userMsg, setUserMsg] = useState("");
  const [displayMsg, setDisplayMsg] = useState([] as any);

  const delay = (ms: number | undefined) =>
    new Promise((resolve) => setTimeout(resolve, ms));

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
    <div className="chat-box-wrapper">
      <div className="chat-box">
        <Card>
          <div className="chat-inner-wrapper">
            <div className="chat-body">
              {displayMsg.map((msg: string) => (
                <div className="message text-wrap bg-secondary bg-opacity-25 rounded-4">
                  <div>{msg}</div>
                </div>
              ))}
            </div>
            <div className="bottom-bar">
              <div className="input-bar">
                <Form onSubmit={handleSubmit}>
                  <InputGroup>
                    <Form.Control
                      placeholder="type your concerns!"
                      aria-label="chatbox with two button addons"
                      ref={userMsgRef}
                      type="text"
                      onChange={(e) => setUserMsg(e.target.value)}
                    />
                    <Button variant="outline-primary" type="reset">
                      Reset
                    </Button>
                    <Button variant="outline-primary" type="submit">
                      Submit
                    </Button>
                  </InputGroup>
                </Form>
              </div>
              <div className="generate-button">
                <Link
                  className="btn btn-primary"
                  role="button"
                  to="/recommendations"
                >
                  Generate Report!
                </Link>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
