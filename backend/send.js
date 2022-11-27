const express = require('express');
const send = express.Router();
const json_data = require('./sample.json');

send.get("/api/send", (req, res) => {
    res.json(json_data);
});

module.exports = send;