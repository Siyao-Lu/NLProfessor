const express = require('express');
const receive = express.Router();
const axios = require('axios').default;

receive.post("/api/receive", (req, res) => {
    const body = req.body;
    console.log(body);
    // dialogueflow communicate, get data 
    res.json("Received!");
})

module.exports = receive;