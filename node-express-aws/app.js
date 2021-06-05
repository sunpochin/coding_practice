//jshint esversion:6
// app.js
require('dotenv').config();
const routes = require('./api/books');
const cors = require('cors');

const connectDB = require('./config/db');

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(cors({ origin: true, credentials: true }));

// app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
// app.use(bodyParser.json());
// app.use(express.static("public"));

// Connect Database
connectDB();

app.use("/api/books", books);
// app.use('/api', routes);

app.get('/', (req, res) => res.send('Hello world!'));

const port = process.env.PORT || 8082;

app.listen(port, () => console.log(`Server running on port ${port}`));
