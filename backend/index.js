require('dotenv').config();
const express = require("express");
const PORT = process.env.PORT;
const bodyParser = require("body-parser");
const cors = require("cors");
const send = require('./send');
const receive = require('./receive');

const app = express();

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(send);
app.use(receive);

app.listen(PORT, () => {
    console.log(`server is listening on ${PORT}`);
});

// const server = app.listen(PORT, () => {
//     console.log(`server is listening on ${PORT}`);
// });

// const io = require('socket.io')(server, {
//     pingTimeout: 60000,
//     cors: {
//         origin: "http://localhost:3000",
//     },
// });

// i.on("connection", (socket) => {
//     console.log("connected to socket.io");
//     // socket.on('setup', (userData) => )
// })

module.exports = app;


