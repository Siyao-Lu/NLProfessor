const express = require("express");
const receive = express.Router();
const axios = require("axios").default;
const dialogflow = require("@google-cloud/dialogflow");

// Instantiates a session client
const sessionClient = new dialogflow.SessionsClient();

const DIALOGFLOW_PROJECT_ID = "smart-advisor-ympd";

receive.post("/api/receive", async (req, res) => {
  const body = req.body;
  console.log(body);
  // dialogueflow communicate, get data

  const sessionPath = sessionClient.projectAgentSessionPath(
    DIALOGFLOW_PROJECT_ID,
    body.sessionId
  );
  const request = {
    session: sessionPath,
    queryInput: {
      text: {
        text: body.userMsg,
        languageCode: "en-US",
      },
    },
  };

  const responses = await sessionClient.detectIntent(request);

  console.log(JSON.stringify(responses));

  const responseStr = responses[0].queryResult.fulfillmentText.replace(
    ", ,",
    ", "
  );

  res.json(responseStr);
});

module.exports = receive;
