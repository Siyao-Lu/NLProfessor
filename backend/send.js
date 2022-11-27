const express = require('express');
const send = express.Router();
const axios = require('axios').default;

send.get("/api/send", (req, res) => {
    res.json("Sent!");
});

module.exports = send;